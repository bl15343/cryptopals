#Fixed XOR

def fixed_xor(buf1, buf2):
    bin_buf1 = bytearray.fromhex(buf1)
    bin_buf2 = bytearray.fromhex(buf2)

    result_buf = bytearray(len(bin_buf1))

    for i in range(len(bin_buf1)):
        result_buf[i] = bin_buf1[i] ^ bin_buf2[i]

    return bytes(result_buf).hex()

print('Result from fixed_xor', fixed_xor('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965'))