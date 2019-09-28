# Set 1 Exercise 6

#import base64
import binascii


def str_to_bin(text):
    return bin(int(binascii.hexlify(text), 16))

def get_hamming_distance(str1, str2):
    bin_str1 = str_to_bin(str1)
    bin_str2 = str_to_bin(str2)

    hamming_distance = 0

    for index, value in enumerate(bin_str1):
        if value != bin_str2[index]:
            hamming_distance += 1

    return hamming_distance


print get_hamming_distance('this is a test', 'wokka wokka!!!')
