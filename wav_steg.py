import binascii
import itertools

import utility


def encode_message(list_of_hex: list, message: str, num_bits: int = 1):
    """Function takes in a list of hex, message and num_bits. Replaces in place the list_of_hex with message
    using num_bits"""
    message_counter = 0
    length_of_message = len(message)
    if length_of_message % num_bits != 0:
        message += (num_bits - (length_of_message % num_bits)) * '0'
    for i in range(43, len(list_of_hex)):
        if message_counter < length_of_message:
            if num_bits == 1:
                current_byte = utility.convert_byte_hex_to_bin(list_of_hex[i])
                replaced_byte = utility.encode_bit_0(current_byte, message[message_counter])  # Replace bit 0
                message_counter += 1
                list_of_hex[i] = utility.convert_bin_to_hex(replaced_byte)
            elif num_bits == 2:
                current_byte = utility.convert_byte_hex_to_bin(list_of_hex[i])
                replaced_byte = utility.encode_bit_0(current_byte, message[message_counter])  # Replace bit 0
                message_counter += 1
                replaced_byte = utility.encode_bit_1(replaced_byte, message[message_counter])  # Replace bit 1
                message_counter += 1
                list_of_hex[i] = utility.convert_bin_to_hex(replaced_byte)
            elif num_bits == 3:
                current_byte = utility.convert_byte_hex_to_bin(list_of_hex[i])
                replaced_byte = utility.encode_bit_0(current_byte, message[message_counter])  # Replace bit 0
                message_counter += 1
                replaced_byte = utility.encode_bit_1(replaced_byte, message[message_counter])  # Replace bit 1
                message_counter += 1
                replaced_byte = utility.encode_bit_2(replaced_byte, message[message_counter])  # Replace bit 2
                message_counter += 1
                list_of_hex[i] = utility.convert_bin_to_hex(replaced_byte)
            elif num_bits == 4:
                current_byte = utility.convert_byte_hex_to_bin(list_of_hex[i])
                replaced_byte = utility.encode_bit_0(current_byte, message[message_counter])  # Replace bit 0
                message_counter += 1
                replaced_byte = utility.encode_bit_1(replaced_byte, message[message_counter])  # Replace bit 1
                message_counter += 1
                replaced_byte = utility.encode_bit_2(replaced_byte, message[message_counter])  # Replace bit 2
                message_counter += 1
                replaced_byte = utility.encode_bit_3(replaced_byte, message[message_counter])  # Replace bit 3
                message_counter += 1
                list_of_hex[i] = utility.convert_bin_to_hex(replaced_byte)
            elif num_bits == 5:
                current_byte = utility.convert_byte_hex_to_bin(list_of_hex[i])
                replaced_byte = utility.encode_bit_0(current_byte, message[message_counter])  # Replace bit 0
                message_counter += 1
                replaced_byte = utility.encode_bit_1(replaced_byte, message[message_counter])  # Replace bit 1
                message_counter += 1
                replaced_byte = utility.encode_bit_2(replaced_byte, message[message_counter])  # Replace bit 2
                message_counter += 1
                replaced_byte = utility.encode_bit_3(replaced_byte, message[message_counter])  # Replace bit 3
                message_counter += 1
                replaced_byte = utility.encode_bit_4(replaced_byte, message[message_counter])  # Replace bit 4
                message_counter += 1
                list_of_hex[i] = utility.convert_bin_to_hex(replaced_byte)
            elif num_bits == 6:
                current_byte = utility.convert_byte_hex_to_bin(list_of_hex[i])
                replaced_byte = utility.encode_bit_0(current_byte, message[message_counter])  # Replace bit 0
                message_counter += 1
                replaced_byte = utility.encode_bit_1(replaced_byte, message[message_counter])  # Replace bit 1
                message_counter += 1
                replaced_byte = utility.encode_bit_2(replaced_byte, message[message_counter])  # Replace bit 2
                message_counter += 1
                replaced_byte = utility.encode_bit_3(replaced_byte, message[message_counter])  # Replace bit 3
                message_counter += 1
                replaced_byte = utility.encode_bit_4(replaced_byte, message[message_counter])  # Replace bit 4
                message_counter += 1
                replaced_byte = utility.encode_bit_5(replaced_byte, message[message_counter])  # Replace bit 5
                message_counter += 1
                list_of_hex[i] = utility.convert_bin_to_hex(replaced_byte)
            elif num_bits == 7:
                current_byte = utility.convert_byte_hex_to_bin(list_of_hex[i])
                replaced_byte = utility.encode_bit_0(current_byte, message[message_counter])  # Replace bit 0
                message_counter += 1
                replaced_byte = utility.encode_bit_1(replaced_byte, message[message_counter])  # Replace bit 1
                message_counter += 1
                replaced_byte = utility.encode_bit_2(replaced_byte, message[message_counter])  # Replace bit 2
                message_counter += 1
                replaced_byte = utility.encode_bit_3(replaced_byte, message[message_counter])  # Replace bit 3
                message_counter += 1
                replaced_byte = utility.encode_bit_4(replaced_byte, message[message_counter])  # Replace bit 4
                message_counter += 1
                replaced_byte = utility.encode_bit_5(replaced_byte, message[message_counter])  # Replace bit 5
                message_counter += 1
                replaced_byte = utility.encode_bit_6(replaced_byte, message[message_counter])  # Replace bit 6
                message_counter += 1
                list_of_hex[i] = utility.convert_bin_to_hex(replaced_byte)
            elif num_bits == 8:
                current_byte = utility.convert_byte_hex_to_bin(list_of_hex[i])
                replaced_byte = utility.encode_bit_0(current_byte, message[message_counter])  # Replace bit 0
                message_counter += 1
                replaced_byte = utility.encode_bit_1(replaced_byte, message[message_counter])  # Replace bit 1
                message_counter += 1
                replaced_byte = utility.encode_bit_2(replaced_byte, message[message_counter])  # Replace bit 2
                message_counter += 1
                replaced_byte = utility.encode_bit_3(replaced_byte, message[message_counter])  # Replace bit 3
                message_counter += 1
                replaced_byte = utility.encode_bit_4(replaced_byte, message[message_counter])  # Replace bit 4
                message_counter += 1
                replaced_byte = utility.encode_bit_5(replaced_byte, message[message_counter])  # Replace bit 5
                message_counter += 1
                replaced_byte = utility.encode_bit_6(replaced_byte, message[message_counter])  # Replace bit 6
                message_counter += 1
                replaced_byte = utility.encode_bit_7(replaced_byte, message[message_counter])  # Replace bit 7
                message_counter += 1
                list_of_hex[i] = utility.convert_bin_to_hex(replaced_byte)


def decode_message(list_of_hex: list, len_message: int, num_bits: int = 1):
    """Function takes in a list of hexadecimal values in byte format, length of the message (in terms of
    the number of characters) and number of bits per message (defaults to 1).
     Returns a list of binary values (1's and 0's)"""
    binary_list = []
    current_len = 0
    for i in range(43, len(list_of_hex)):
        if current_len < len_message * 8:
            if num_bits == 1:
                current_byte = utility.convert_byte_hex_to_bin(list_of_hex[i])
                binary_list.append(current_byte[7])  # inserts bit 0
                current_len += 1
            elif num_bits == 2:
                current_byte = utility.convert_byte_hex_to_bin(list_of_hex[i])
                binary_list.append(current_byte[7])  # inserts bit 0
                current_len += 1
                binary_list.append(current_byte[6])  # inserts bit 1
                current_len += 1
            elif num_bits == 3:
                current_byte = utility.convert_byte_hex_to_bin(list_of_hex[i])
                binary_list.append(current_byte[7])  # inserts bit 0
                current_len += 1
                binary_list.append(current_byte[6])  # inserts bit 1
                current_len += 1
                binary_list.append(current_byte[5])  # inserts bit 2
                current_len += 1
            elif num_bits == 4:
                current_byte = utility.convert_byte_hex_to_bin(list_of_hex[i])
                binary_list.append(current_byte[7])  # inserts bit 0
                current_len += 1
                binary_list.append(current_byte[6])  # inserts bit 1
                current_len += 1
                binary_list.append(current_byte[5])  # inserts bit 2
                current_len += 1
                binary_list.append(current_byte[4])  # inserts bit 3
                current_len += 1
            elif num_bits == 5:
                current_byte = utility.convert_byte_hex_to_bin(list_of_hex[i])
                binary_list.append(current_byte[7])  # inserts bit 0
                current_len += 1
                binary_list.append(current_byte[6])  # inserts bit 1
                current_len += 1
                binary_list.append(current_byte[5])  # inserts bit 2
                current_len += 1
                binary_list.append(current_byte[4])  # inserts bit 3
                current_len += 1
                binary_list.append(current_byte[3])  # inserts bit 4
                current_len += 1
            elif num_bits == 6:
                current_byte = utility.convert_byte_hex_to_bin(list_of_hex[i])
                binary_list.append(current_byte[7])  # inserts bit 0
                current_len += 1
                binary_list.append(current_byte[6])  # inserts bit 1
                current_len += 1
                binary_list.append(current_byte[5])  # inserts bit 2
                current_len += 1
                binary_list.append(current_byte[4])  # inserts bit 3
                current_len += 1
                binary_list.append(current_byte[3])  # inserts bit 4
                current_len += 1
                binary_list.append(current_byte[2])  # inserts bit 5
                current_len += 1
            elif num_bits == 7:
                current_byte = utility.convert_byte_hex_to_bin(list_of_hex[i])
                binary_list.append(current_byte[7])  # inserts bit 0
                current_len += 1
                binary_list.append(current_byte[6])  # inserts bit 1
                current_len += 1
                binary_list.append(current_byte[5])  # inserts bit 2
                current_len += 1
                binary_list.append(current_byte[4])  # inserts bit 3
                current_len += 1
                binary_list.append(current_byte[3])  # inserts bit 4
                current_len += 1
                binary_list.append(current_byte[2])  # inserts bit 5
                current_len += 1
                binary_list.append(current_byte[1])  # inserts bit 6
                current_len += 1
            elif num_bits == 8:
                current_byte = utility.convert_byte_hex_to_bin(list_of_hex[i])
                binary_list.append(current_byte[7])  # inserts bit 0
                current_len += 1
                binary_list.append(current_byte[6])  # inserts bit 1
                current_len += 1
                binary_list.append(current_byte[5])  # inserts bit 2
                current_len += 1
                binary_list.append(current_byte[4])  # inserts bit 3
                current_len += 1
                binary_list.append(current_byte[3])  # inserts bit 4
                current_len += 1
                binary_list.append(current_byte[2])  # inserts bit 5
                current_len += 1
                binary_list.append(current_byte[1])  # inserts bit 6
                current_len += 1
                binary_list.append(current_byte[0])  # inserts bit 7
                current_len += 1
        else:
            break
    return binary_list


def get_available_bits(list_of_hex: list):
    num_header = 0
    for i in range(43, len(list_of_hex)):
        num_header += 1
    return num_header


def write_secret_to_file(save_dir: str, filename: str, payload: str, num_bits: int = 1):
    """Function takes in 4 parameters: save_dir, filename, payload and num_bits. Opens the file using filename, writes
    payload to filename with num_bits and saves the resulting output to save_dir"""

    encode_list = utility.read_file_into_hex_list(filename)
    payload_list = utility.read_file_into_hex_list(payload)
    secret = ''.join(map(utility.convert_byte_hex_to_bin, payload_list))
    encode_message(encode_list, secret, num_bits)
    with open(f'{save_dir}/secret.wav', 'wb') as fw:
        fw.write(binascii.unhexlify(b''.join(encode_list)))


def get_secret_from_file(filename: str, msg_len: int, num_bits: int = 1, decoded_name: str = 'decode.txt'):
    """Function takes in the filename of the mp3 file which has a secret inside, the length of the secret message
    (in number of characters), number of bits to use and the filename to write as (Defaults to decode.txt).
     Returns the decoded secret"""

    decode_list = utility.read_file_into_hex_list(filename)
    decoded_byte = decode_message(decode_list, msg_len, num_bits)
    decoded_byte_list = [decoded_byte[i:i + 8] for i in range(0, len(decoded_byte), 8)]
    decoded_nested_hex_list = [[utility.convert_bin_to_hex(''.join(sublist))] for sublist in decoded_byte_list]
    decoded_hex_list = list(itertools.chain(*decoded_nested_hex_list))
    with open(decoded_name, 'wb') as filewrite:
        filewrite.write(binascii.unhexlify(b''.join(decoded_hex_list)))
    return f'File decoded as {decoded_name}!'
