import binascii


def encode_bit_0(bin_str: str, bit: str):
    """Function takes in the byte (in terms of binary) to manipulate and a bit to encode (1 or 0). Changes bit 0.
     Returns the encoded value as a string """
    replaced_byte = bin_str[:-1] + bit  # Replaces bit 0 aka LSB
    return replaced_byte  # padding to ensure 2 digits


def encode_bit_1(bin_str: str, bit: str):
    """Function takes in the byte (in terms of binary) to manipulate and a bit to encode (1 or 0). Changes bit 1.
     Returns the encoded value as a string """
    replaced_byte = bin_str[:-2] + bit + bin_str[-1]  # Encodes bit 1
    return replaced_byte


def encode_bit_2(bin_str: str, bit: str):
    """Function takes in the byte (in terms of binary) to manipulate and a bit to encode (1 or 0). Changes bit 2.
     Returns the encoded value as a string """
    replaced_byte = bin_str[:-3] + bit + bin_str[-2:]  # Encodes bit 2
    return replaced_byte  # padding to ensure 2 digits


def encode_bit_3(bin_str: str, bit: str):
    """Function takes in the byte (in terms of binary) to manipulate and a bit to encode (1 or 0). Changes bit 3.
     Returns the encoded value as a string """
    replaced_byte = bin_str[:-4] + bit + bin_str[-3:]  # Encodes bit 3
    return replaced_byte  # padding to ensure 2 digits


def encode_bit_4(bin_str: str, bit: str):
    """Function takes in the byte (in terms of binary) to manipulate and a bit to encode (1 or 0). Changes bit 4.
     Returns the encoded value as a string """
    replaced_byte = bin_str[:-5] + bit + bin_str[-4:]  # Encodes bit 4
    return replaced_byte  # padding to ensure 2 digits


def encode_bit_5(bin_str: str, bit: str):
    """Function takes in the byte (in terms of binary) to manipulate and a bit to encode (1 or 0). Changes bit 5.
     Returns the encoded value as a string """
    replaced_byte = bin_str[:-6] + bit + bin_str[-5:]  # Encodes bit 5
    return replaced_byte  # padding to ensure 2 digits


def encode_bit_6(bin_str: str, bit: str):
    """Function takes in the byte (in terms of binary) to manipulate and a bit to encode (1 or 0). Changes bit 6.
     Returns the encoded value as a string """
    replaced_byte = bin_str[:-7] + bit + bin_str[-6:]  # Encodes bit 6
    return replaced_byte  # padding to ensure 2 digits


def encode_bit_7(bin_str: str, bit: str):
    """Function takes in the byte (in terms of binary) to manipulate and a bit to encode (1 or 0). Changes bit 7.
     Returns the encoded value as a string """
    replaced_byte = bin_str[:-8] + bit + bin_str[-7:]  # Encodes bit 7
    return replaced_byte  # padding to ensure 2 digits


def convert_bin_to_hex(bin_str: str):
    """Takes in a binary string (string of 1's and 0's) and formats it into the hexadecimal value"""
    return bytes(f'{int(bin_str, 2):x}', 'utf8').zfill(2)  # padding to ensure 2 digits


def convert_byte_hex_to_bin(hex_str: bytes):
    """Takes in a hex string in byte form and formats it into a binary string"""
    return bin(int(hex_str, 16))[2:].zfill(8)


def read_file_into_hex_list(file: str):
    with open(file, 'rb') as fileread:
        file_hex_str = binascii.hexlify(fileread.read())

    return [file_hex_str[i:i + 2] for i in range(0, len(file_hex_str), 2)]


def text_from_bits(bits, encoding='utf8', errors='surrogatepass'):
    """Function takes in a string of bits.
    Parameters that can be overriden: Encoding and errors
    Returns text from a list of binary values (1's and 0's)"""
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
