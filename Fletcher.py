from bitarray import bitarray
import numpy as np

def fletcher(message):
    blocks = []
    bytes_list = []
    
    bits_list = list(message)

    split = np.array_split(bits_list, len(bits_list)/8)
    for array in split:
        byte = ''
        for bite in array:
            byte = byte + str(bite)
        blocks.append(ord(bitarray(byte).tobytes()))

    c1 = 0
    c2 = 0

    for number in blocks:
        c1 = c1 + number
        c2 = c2 + c1
    
    c1 = c1 % 256
    c2 = c2 % 256
    
    return c1, c2

def fletcher_checksum(message, c1_o, c2_o):
    c1, c2 = fletcher(message)
    same = False
    
    if c1 == c1_o and c2 == c2_o:
        same = True
    
    return same