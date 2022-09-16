import binascii
import utility


def encode_message(list_of_hex: list, message: str, num_bits: int = 1):
    """Function takes in a list of hexadecimal values in byte format, a message in string format and number of bits
    to replace (defaults to 1). Replaces the bytes in place so there is no return"""
    message_counter = 0
    message = ''.join(f"{ord(i):08b}" for i in message)
    length_of_message = len(message)
    for i in range(len(list_of_hex)):
        if message_counter < length_of_message:
            if list_of_hex[i] == b'ff':
                if num_bits == 1:
                    current_byte = bin(int(list_of_hex[i + 2], 16))[2:].zfill(8)  # Gets the next 8 bits (17-24)
                    replaced_byte = utility.encode_bit_0(current_byte, message[message_counter])  # Replace bit 24
                    message_counter += 1
                    list_of_hex[i + 2] = utility.convert_bin_to_hex(replaced_byte)
                elif num_bits == 2:
                    current_byte = bin(int(list_of_hex[i + 2], 16))[2:].zfill(8)  # Gets the next 8 bits (17-24)
                    replaced_byte = utility.encode_bit_0(current_byte, message[message_counter])  # Replace bit 24
                    message_counter += 1
                    list_of_hex[i + 2] = utility.convert_bin_to_hex(replaced_byte)
                    # Encodes the next part of the header (Bits 25-32). As bit 27 and 28 affects the stereo, it will
                    # be encoded last
                    current_byte = bin(int(list_of_hex[i + 3], 16))[2:].zfill(8)  # Gets the next 8 bits (25-32)
                    replaced_byte = utility.encode_bit_0(current_byte, message[message_counter])  # Replace bit 32
                    message_counter += 1
                    list_of_hex[i + 3] = utility.convert_bin_to_hex(replaced_byte)
                elif num_bits == 3:
                    current_byte = bin(int(list_of_hex[i + 2], 16))[2:].zfill(8)  # Gets the next 8 bits (17-24)
                    replaced_byte = utility.encode_bit_0(current_byte, message[message_counter])  # Replace bit 24
                    message_counter += 1
                    list_of_hex[i + 2] = utility.convert_bin_to_hex(replaced_byte)
                    # Encodes the next part of the header (Bits 25-32). As bit 27 and 28 affects the stereo, it will
                    # be encoded last
                    current_byte = bin(int(list_of_hex[i + 3], 16))[2:].zfill(8)  # Gets the next 8 bits (25-32)
                    replaced_byte = utility.encode_bit_0(current_byte, message[message_counter])  # Replace bit 32
                    message_counter += 1
                    replaced_byte = utility.encode_bit_1(replaced_byte, message[message_counter])  # Replace bit 31
                    message_counter += 1
                    list_of_hex[i + 3] = utility.convert_bin_to_hex(replaced_byte)
                elif num_bits == 4:
                    current_byte = bin(int(list_of_hex[i + 2], 16))[2:].zfill(8)  # Gets the next 8 bits (17-24)
                    replaced_byte = utility.encode_bit_0(current_byte, message[message_counter])  # Replace bit 24
                    message_counter += 1
                    list_of_hex[i + 2] = utility.convert_bin_to_hex(replaced_byte)
                    # Encodes the next part of the header (Bits 25-32). As bit 27 and 28 affects the stereo, it will
                    # be encoded last
                    current_byte = bin(int(list_of_hex[i + 3], 16))[2:].zfill(8)  # Gets the next 8 bits (25-32)
                    replaced_byte = utility.encode_bit_0(current_byte, message[message_counter])  # Replace bit 32
                    message_counter += 1
                    replaced_byte = utility.encode_bit_1(replaced_byte, message[message_counter])  # Replace bit 31
                    message_counter += 1
                    replaced_byte = utility.encode_bit_2(replaced_byte, message[message_counter])  # Replace bit 30
                    message_counter += 1
                    list_of_hex[i + 3] = utility.convert_bin_to_hex(replaced_byte)
                elif num_bits == 5:
                    current_byte = bin(int(list_of_hex[i + 2], 16))[2:].zfill(8)  # Gets the next 8 bits (17-24)
                    replaced_byte = utility.encode_bit_0(current_byte, message[message_counter])  # Replace bit 24
                    message_counter += 1
                    list_of_hex[i + 2] = utility.convert_bin_to_hex(replaced_byte)
                    # Encodes the next part of the header (Bits 25-32). As bit 27 and 28 affects the stereo, it will
                    # be encoded last
                    current_byte = bin(int(list_of_hex[i + 3], 16))[2:].zfill(8)  # Gets the next 8 bits (25-32)
                    replaced_byte = utility.encode_bit_0(current_byte, message[message_counter])  # Replace bit 32
                    message_counter += 1
                    replaced_byte = utility.encode_bit_1(replaced_byte, message[message_counter])  # Replace bit 31
                    message_counter += 1
                    replaced_byte = utility.encode_bit_2(replaced_byte, message[message_counter])  # Replace bit 30
                    message_counter += 1
                    replaced_byte = utility.encode_bit_3(replaced_byte, message[message_counter])  # Replace bit 29
                    message_counter += 1
                    list_of_hex[i + 3] = utility.convert_bin_to_hex(replaced_byte)
                elif num_bits == 6:  # Expect audio difference from here on out
                    current_byte = bin(int(list_of_hex[i + 2], 16))[2:].zfill(8)  # Gets the next 8 bits (17-24)
                    replaced_byte = utility.encode_bit_0(current_byte, message[message_counter])  # Replace bit 24
                    message_counter += 1
                    list_of_hex[i + 2] = utility.convert_bin_to_hex(replaced_byte)
                    # Encodes the next part of the header (Bits 25-32). As bit 27 and 28 affects the stereo, it will
                    # be encoded last
                    current_byte = bin(int(list_of_hex[i + 3], 16))[2:].zfill(8)  # Gets the next 8 bits (25-32)
                    replaced_byte = utility.encode_bit_0(current_byte, message[message_counter])  # Replace bit 32
                    message_counter += 1
                    replaced_byte = utility.encode_bit_1(replaced_byte, message[message_counter])  # Replace bit 31
                    message_counter += 1
                    replaced_byte = utility.encode_bit_2(replaced_byte, message[message_counter])  # Replace bit 30
                    message_counter += 1
                    replaced_byte = utility.encode_bit_3(replaced_byte, message[message_counter])  # Replace bit 29
                    message_counter += 1
                    replaced_byte = utility.encode_bit_4(replaced_byte, message[message_counter])  # Replace bit 28
                    message_counter += 1
                    list_of_hex[i + 3] = utility.convert_bin_to_hex(replaced_byte)
                elif num_bits == 7:  # Expect audio difference from here on out
                    current_byte = bin(int(list_of_hex[i + 2], 16))[2:].zfill(8)  # Gets the next 8 bits (17-24)
                    replaced_byte = utility.encode_bit_0(current_byte, message[message_counter])  # Replace bit 24
                    message_counter += 1
                    list_of_hex[i + 2] = utility.convert_bin_to_hex(replaced_byte)
                    # Encodes the next part of the header (Bits 25-32). As bit 27 and 28 affects the stereo, it will
                    # be encoded last
                    current_byte = bin(int(list_of_hex[i + 3], 16))[2:].zfill(8)  # Gets the next 8 bits (25-32)
                    replaced_byte = utility.encode_bit_0(current_byte, message[message_counter])  # Replace bit 32
                    message_counter += 1
                    replaced_byte = utility.encode_bit_1(replaced_byte, message[message_counter])  # Replace bit 31
                    message_counter += 1
                    replaced_byte = utility.encode_bit_2(replaced_byte, message[message_counter])  # Replace bit 30
                    message_counter += 1
                    replaced_byte = utility.encode_bit_3(replaced_byte, message[message_counter])  # Replace bit 29
                    message_counter += 1
                    replaced_byte = utility.encode_bit_4(replaced_byte, message[message_counter])  # Replace bit 28
                    message_counter += 1
                    replaced_byte = utility.encode_bit_5(replaced_byte, message[message_counter])  # Replace bit 27
                    message_counter += 1
                    list_of_hex[i + 3] = utility.convert_bin_to_hex(replaced_byte)


def decode_message(list_of_hex: list, len_message: int, num_bits: int = 1):
    """Function takes in a list of hexadecimal values in byte format, length of the message (in terms of
    the number of characters) and number of bits per message (defaults to 1).
     Returns a list of binary values (1's and 0's)"""
    binary_list = ['0', 'b']
    current_len = 0
    for i in range(len(list_of_hex)):
        if list_of_hex[i] == b'ff':
            if current_len < len_message * 8:
                if num_bits == 1:
                    current_byte = bin(int(list_of_hex[i + 2], 16))[2:].zfill(8)  # Gets the next 8 bits (17-24)
                    binary_list.append(current_byte[-1])  # inserts bit 24 into list
                    current_len += 1
                elif num_bits == 2:
                    current_byte = bin(int(list_of_hex[i + 2], 16))[2:].zfill(8)  # Gets the next 8 bits (17-24)
                    binary_list.append(current_byte[-1])  # inserts bit 24 into list
                    current_len += 1
                    current_byte = bin(int(list_of_hex[i + 3], 16))[2:].zfill(8)  # Gets the next 8 bits (25-32)
                    binary_list.append(current_byte[-1])  # inserts bit 32 into list
                    current_len += 1
                elif num_bits == 3:
                    current_byte = bin(int(list_of_hex[i + 2], 16))[2:].zfill(8)  # Gets the next 8 bits (17-24)
                    binary_list.append(current_byte[-1])  # inserts bit 24 into list
                    current_len += 1
                    current_byte = bin(int(list_of_hex[i + 3], 16))[2:].zfill(8)  # Gets the next 8 bits (25-32)
                    binary_list.append(current_byte[-1])  # inserts bit 32 into list
                    current_len += 1
                    binary_list.append(current_byte[-2])  # inserts bit 31 into list
                    current_len += 1
                elif num_bits == 4:
                    current_byte = bin(int(list_of_hex[i + 2], 16))[2:].zfill(8)  # Gets the next 8 bits (17-24)
                    binary_list.append(current_byte[-1])  # inserts bit 24 into list
                    current_len += 1
                    current_byte = bin(int(list_of_hex[i + 3], 16))[2:].zfill(8)  # Gets the next 8 bits (25-32)
                    binary_list.append(current_byte[-1])  # inserts bit 32 into list
                    current_len += 1
                    binary_list.append(current_byte[-2])  # inserts bit 31 into list
                    current_len += 1
                    binary_list.append(current_byte[-3])  # inserts bit 30 into list
                    current_len += 1
                elif num_bits == 5:
                    current_byte = bin(int(list_of_hex[i + 2], 16))[2:].zfill(8)  # Gets the next 8 bits (17-24)
                    binary_list.append(current_byte[-1])  # inserts bit 24 into list
                    current_len += 1
                    current_byte = bin(int(list_of_hex[i + 3], 16))[2:].zfill(8)  # Gets the next 8 bits (25-32)
                    binary_list.append(current_byte[-1])  # inserts bit 32 into list
                    current_len += 1
                    binary_list.append(current_byte[-2])  # inserts bit 31 into list
                    current_len += 1
                    binary_list.append(current_byte[-3])  # inserts bit 30 into list
                    current_len += 1
                    binary_list.append(current_byte[-4])  # inserts bit 29 into list
                    current_len += 1
                elif num_bits == 6:
                    current_byte = bin(int(list_of_hex[i + 2], 16))[2:].zfill(8)  # Gets the next 8 bits (17-24)
                    binary_list.append(current_byte[-1])  # inserts bit 24 into list
                    current_len += 1
                    current_byte = bin(int(list_of_hex[i + 3], 16))[2:].zfill(8)  # Gets the next 8 bits (25-32)
                    binary_list.append(current_byte[-1])  # inserts bit 32 into list
                    current_len += 1
                    binary_list.append(current_byte[-2])  # inserts bit 31 into list
                    current_len += 1
                    binary_list.append(current_byte[-3])  # inserts bit 30 into list
                    current_len += 1
                    binary_list.append(current_byte[-4])  # inserts bit 29 into list
                    current_len += 1
                    binary_list.append(current_byte[-5])  # inserts bit 28 into list
                    current_len += 1
                elif num_bits == 7:
                    current_byte = bin(int(list_of_hex[i + 2], 16))[2:].zfill(8)  # Gets the next 8 bits (17-24)
                    binary_list.append(current_byte[-1])  # inserts bit 24 into list
                    current_len += 1
                    current_byte = bin(int(list_of_hex[i + 3], 16))[2:].zfill(8)  # Gets the next 8 bits (25-32)
                    binary_list.append(current_byte[-1])  # inserts bit 32 into list
                    current_len += 1
                    binary_list.append(current_byte[-2])  # inserts bit 31 into list
                    current_len += 1
                    binary_list.append(current_byte[-3])  # inserts bit 30 into list
                    current_len += 1
                    binary_list.append(current_byte[-4])  # inserts bit 29 into list
                    current_len += 1
                    binary_list.append(current_byte[-5])  # inserts bit 28 into list
                    current_len += 1
                    binary_list.append(current_byte[-6])  # inserts bit 27 into list
                    current_len += 1
            else:
                break
    return binary_list


def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    """Function takes in a string of bits.
    Parameters that can be overriden: Encoding and errors
    Returns text from a list of binary values (1's and 0's)"""
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'


def write_secret_to_file(filename: str, secret: str, num_bits: int = 1):
    """Function takes in the filename of mp3 file, secret to be encoded inside and number of bits to use.
    Writes the secret message into a new file called secret.mp3 which is created in the same directory"""
    with open(filename, 'rb') as fileread:
        encodehexstring = binascii.hexlify(fileread.read())

    encodelist = [encodehexstring[i:i + 2] for i in range(0, len(encodehexstring), 2)]
    encode_message(encodelist, secret, num_bits)

    with open('secret.mp3', 'wb') as filewrite:
        filewrite.write(binascii.unhexlify(b''.join(encodelist)))


def get_secret_from_file(filename: str, msg_len: int, num_bits: int = 1):
    """Function takes in the filename of the mp3 file which has a secret inside, the length of the secret message
    (in number of characters) and number of bits to use. Returns the decoded secret"""
    with open(filename, 'rb') as f:
        decodehexstring = binascii.hexlify(f.read())

    decodelist = [decodehexstring[i:i + 2] for i in range(0, len(decodehexstring), 2)]
    decoded_byte = decode_message(decodelist, msg_len, num_bits)
    decoded_string = ''.join(decoded_byte)
    return text_from_bits(decoded_string)
