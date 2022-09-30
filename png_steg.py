"""
CSC2004 CSF AC1 STEGANOGRAPHY
Authors: Alastair, Aaron, Kah Jun, Mathan, Nicole

This program hides Files Inside Images ( any type of binary files such as audio, pdf or images)
but if the data we want to hide is bigger than the eighth of the image, might be corrupted

How it works
Steganography encoder/decoder, this Python scripts encode binary files within images.

optional arguments:
  -h, --help            show this help message and exit
  -t TEXT, --text TEXT  The text data to encode into the image, this only should be specified for encoding
  -f FILE, --file FILE  The file to hide into the image, this only should be specified while encoding
  -e ENCODE, --encode ENCODE
                        Encode the following image
  -d DECODE, --decode DECODE
                        Decode the following image
  -b N_BITS, --n-bits N_BITS
                        The number of least significant bits of the image to encode

python allstego.py -e imagename -f filename -b 1 (-b is optional)

"""
# importing of the required libraries
import cv2
import numpy as np
import os
import argparse


# 1. Function to convert into binary format using tuple.
def to_bin(data):
    if isinstance(data, str):
        return ''.join([format(ord(i), "08b") for i in data])
    elif isinstance(data, bytes):
        return ''.join([format(i, "08b") for i in data])
    elif isinstance(data, np.ndarray):
        return [format(i, "08b") for i in data]
    elif isinstance(data, int) or isinstance(data, np.uint8):
        return format(data, "08b")
    else:
        raise TypeError("Type not supported.")


# 2. Encoder function to encode the file to the cover image. Default LSB is 2. User can manipulte in CLI
def encode(image_name, payload, n_bits=2):
    # read the image
    image = cv2.imread(image_name)
    # retrive the max bytes to encode
    n_bytes = image.shape[0] * image.shape[1] * 3 * n_bits // 8
    print("[*] Maximum bytes to encode:", n_bytes)
    print("[*] Data size:", len(payload))
    # prompt error if its insufficient to encode payload within cover
    if len(payload) > n_bytes:
        raise ValueError(f"[!] Insufficient bytes ({len(payload)}), need bigger image or less data.")
    print("[*] Encoding data...")
    # add delimiter  criteria
    if isinstance(payload, str):
        payload += "====="
    elif isinstance(payload, bytes):
        payload += b"====="
    data_index = 0
    # convert data to binary using the earlier function
    binary_payload_data = to_bin(payload)
    # size of data to hide
    data_len = len(binary_payload_data)
    for bit in range(1, n_bits + 1):
        for row in image:
            for pixel in row:
                # convert RGB values to binary format
                r, g, b = to_bin(pixel)
                # modify the least significant bit only if there is still data to store
                if data_index < data_len:
                    if bit == 1:
                        # LSB of red bit
                        pixel[0] = int(r[:-bit] + binary_payload_data[data_index], 2)
                    elif bit > 1:
                        # replace the LSB bit of red pixel with the data bit
                        pixel[0] = int(r[:-bit] + binary_payload_data[data_index] + r[-bit + 1:], 2)
                    data_index += 1
                if data_index < data_len:
                    if bit == 1:
                        # LSB of green bit
                        pixel[1] = int(g[:-bit] + binary_payload_data[data_index], 2)
                    elif bit > 1:
                        # replace the LSB bit of green pixel with the data bit
                        pixel[1] = int(g[:-bit] + binary_payload_data[data_index] + g[-bit + 1:], 2)
                    data_index += 1
                if data_index < data_len:
                    if bit == 1:
                        # LSB of Blue bit
                        pixel[2] = int(b[:-bit] + binary_payload_data[data_index], 2)
                    elif bit > 1:
                        # replace the LSB bit of Blue pixel with the data bit
                        pixel[2] = int(b[:-bit] + binary_payload_data[data_index] + b[-bit + 1:], 2)
                    data_index += 1
                # if data is encoded, break loop
                if data_index >= data_len:
                    break
    return image


# 3. Decoder function that decode the file from the cover image. Default LSB is 1. User can manipulte in CLI
def decode(image_name, n_bits=1, in_bytes=False):
    print("[+] Decoding...")
    # read the image
    image = cv2.imread(image_name)
    binary_data = ""
    # iterate through to retrive the hidden data
    for bit in range(1, n_bits + 1):
        for row in image:
            for pixel in row:
                r, g, b = to_bin(pixel)
                binary_data += r[-bit]
                binary_data += g[-bit]
                binary_data += b[-bit]

    # split into 8-bits
    all_bytes = [binary_data[i: i + 8] for i in range(0, len(binary_data), 8)]
    # convert from bits to characters. Since data to decode is in binary form, take it as array instead of a string
    if in_bytes:

        decoded_data = bytearray()
        for byte in all_bytes:
            # append the data after converting from binary to prevent corruption
            decoded_data.append(int(byte, 2))
            if decoded_data[-5:] == b"=====":
                # break loop if matches delimeter
                break
    else:
        decoded_data = ""
        for byte in all_bytes:
            decoded_data += chr(int(byte, 2))
            if decoded_data[-5:] == "=====":
                break
    return decoded_data[:-5]


def run_encode(image_file: str, payload_file: str, num_bits: int):
    with open(payload_file, "rb") as f:
        payload_data = f.read()
    input_image = image_file
    filename, ext = image_file.split(".")
    output_image = f"{filename}encoded.{ext}"
    print(output_image)
    # encode the data into the image
    encoded_image = encode(image_name=input_image, payload=payload_data, n_bits=num_bits)
    # save the output image (encoded image)
    cv2.imwrite(output_image, encoded_image)
    return "[+] Saved encoded image."


def run_decode(image_file: str, num_bits: int, out_file: str):
    decoded_data = decode(image_file, n_bits=num_bits, in_bytes=True)
    with open(out_file, "wb") as f:
        f.write(decoded_data)
    return 'Data decoded!'
