# Set 1 Exercise 5 cryptopals

import binascii


def get_xor_key_bytes(key):
    return bytearray(key)


def get_plaintext_bytes(plaintext):
    return bytearray(plaintext)


def encrypt_with_rotating_xor_key(key, plaintext):
    plaintext_bytes = get_plaintext_bytes(plaintext)
    xor_key = get_xor_key_bytes(key)
    key_length = len(xor_key)
    ciphertext = bytearray()

    for index, value in enumerate(plaintext_bytes):
        ciphertext.append(value ^ xor_key[index % key_length])

    return binascii.hexlify(ciphertext)


print encrypt_with_rotating_xor_key('ICE',"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal")
