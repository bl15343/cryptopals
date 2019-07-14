#Set 1 Challenege 3 Single-byte XOR cipher

def find_single_byte_xor(str):
    byte_buf = bytearray.fromhex(str)

    histogram = dict()

    for char in byte_buf:
        if char not in histogram:
            histogram[char] = 1;
        else:
            histogram[char] += 1;

    #The most frequent occuring char is likely 'E'
    #If we xor the byte that is 'E' with 'E', we should
    #get the xor byte?

    highest_count = 0
    most_frequent = ''
    for key in histogram.keys():
        if histogram.get(key) > highest_count:
            highest_count = histogram.get(key)
            most_frequent = key

    #Find the most_frequent in the byte_buf

    #To do this automatically, we should have a list of most frequently used
    #characters, if you encounter one, add it to to the histogram
    #The character with the highest sum, is the likely candidate

    frequent_chars = (
        'E', 'T', 'A', 'O', 'I', 'N',
        ' ', 'S', 'H', 'R', 'D', 'L', 'U')

    highest_frequency_char = ''
    highest_frequency_count = 0

    for freq in frequent_chars:

        frequent_histogram = {
            'E' : 0,
            'T' : 0,
            'A' : 0,
            'O' : 0,
            'I' : 0,
            'N' : 0,
            ' ' : 0,
            'S' : 0,
            'H' : 0,
            'R' : 0,
            'D' : 0,
            'L' : 0,
            'U' : 0,
        }

        temp_buf = bytearray()
        temp_buf[:] = byte_buf

        xor_byte = temp_buf[temp_buf.find(most_frequent)] ^ ord(freq)

        for i in range(len(temp_buf)):
            temp_buf[i] = temp_buf[i] ^ xor_byte

        temp_string = temp_buf.decode()

        for char in temp_string:
            if char.upper() in frequent_histogram:
                frequent_histogram[char.upper()] += 1


        if highest_frequency_count < sum(frequent_histogram.values()):
            highest_frequency_count = sum(frequent_histogram.values())
            highest_frequency_char = freq


    return highest_frequency_char.encode()


print("The single byte XOR is", find_single_byte_xor('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'))