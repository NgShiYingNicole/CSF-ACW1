import binascii


def encode_message(list_of_hex: list, message: str):
    """Function takes in a list of hexadecimal values in byte format and a message in string format.
    Replaces the bytes in place so there is no return"""
    message_counter = 0
    message = ''.join(f"{ord(i):08b}" for i in message)
    length_of_message = len(message)
    for i in range(len(list_of_hex)):
        if list_of_hex[i] == b'ff':
            if message_counter < length_of_message:
                current_byte = bin(int(list_of_hex[i + 2], 16))[2:].zfill(8)  # Gets the next 8 bits (17-24)
                replaced_byte = bytes(current_byte[:-1] + message[message_counter], 'utf8')  # Replaces bit 24 (priv
                # bit) with message bit
                message_counter += 1
                list_of_hex[i + 2] = bytes(f'{int(replaced_byte, 2):x}', 'utf8').zfill(2)  # padding to ensure 2 digits


def decode_message(list_of_hex: list, len_message: int):
    """Function takes in a list of hexadecimal values in byte format and the length of the message (in terms of
    the number of characters). Returns a list of binary values (1's and 0's)"""
    binary_list = ['0', 'b']
    current_len = 0
    for i in range(len(list_of_hex)):
        if list_of_hex[i] == b'ff':
            if current_len < len_message * 8:
                current_byte = bin(int(list_of_hex[i + 2], 16))[2:].zfill(8)  # Gets the next 8 bits (17-24)
                binary_list.append(current_byte[-1])  # inserts bit 24 into list
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


def write_secret_to_file(filename: str, secret: str):
    """Function takes in the filename of mp3 file and the secret to be encoded inside. Writes the secret message
    into a new file called secret.mp3 which is created in the same directory"""
    with open(filename, 'rb') as fileread:
        encodehexstring = binascii.hexlify(fileread.read())

    encodelist = [encodehexstring[i:i + 2] for i in range(0, len(encodehexstring), 2)]
    encode_message(encodelist, secret)

    with open('secret.mp3', 'wb') as filewrite:
        filewrite.write(binascii.unhexlify(b''.join(encodelist)))


def get_secret_from_file(filename: str, msg_len: int):
    """Function takes in the filename of the mp3 file which has a secret inside and the length of the secret message
    (in number of characters). Returns the decoded secret"""
    with open(filename, 'rb') as f:
        decodehexstring = binascii.hexlify(f.read())

    decodelist = [decodehexstring[i:i + 2] for i in range(0, len(decodehexstring), 2)]
    decoded_byte = decode_message(decodelist, msg_len)
    decoded_string = ''.join(decoded_byte)
    return text_from_bits(decoded_string)
