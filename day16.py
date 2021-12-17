"""
Type numbers:

 * 4 - literal
 * other - operator
"""


packet = open('inputs/day16test.txt').readline().strip()

packet_bin = ''
for char in packet:
    packet_bin += '0' * (4 - len(bin((int(char, 16)))[2:])) + bin((int(char, 16)))[2:]

sum_versions = 0

pointer = 0 # the current position being investigated
start = 0 # represents the beginning of the current packet

def read_literal(pointer):
    """
    * Reads a packet that represents a literal, with the argument being the pointer to the first of the type ID bits.
    * Returns the index of the first bit of the next packet
    """
    start = pointer - 3 # the starting position of the current packet, accounting for the 3 version bits
    pointer += 3 # moving pointer to the beginning of the first 5 bits.
    while packet_bin[pointer] == '1': # move 5 bits to the right while the current 5 bit group begins with a 1
        pointer += 5
    pointer += 5 # move through the last group of 5 bits
    return pointer


def read_operator(pointer):
    """
    * Reads a packet that represents the operator, adding all the subpackets' version numbers to the total.
    * The argument is a pointer to the first of the type ID bits.
    * Returns the index of the first bit of the packet after the current operator packet.    
    """
    global sum_versions
    pointer += 3 # moving pointer to the length type ID bit
    if packet_bin[pointer] == '0': # the next 15 bits represent the total length in bits of all the subpackets
        pointer += 1
        start = pointer # beginning of the bits representing the subpackets
        length = int(packet_bin[pointer : pointer + 16], 2)
        pointer += 15 # moving to the beginning of the first subpacket
        while (pointer - start) <= length - 6: # if there are less than 6 bits left, it cannot be a packet because it wont fit a version and type id.
            sum_versions += int(packet_bin[pointer : pointer + 3], 2)
            pointer += 3
            if str(packet_bin[pointer : pointer + 3]) == '100': # packet represents a literal
                print(pointer)
                pointer = read_literal(pointer)
                pointer += 3 # reading the version number of the next pointer
                print(pointer)


    else: # the next 11 bits represent the number of subpackets in this packet
        pass
    return pointer
                
print(packet_bin)
"""
while pointer < len(packet_bin):
    sum_versions += int(packet_bin[pointer : pointer + 3], 2)
    pointer += 3 # moving pointer from version number to type ID
    if str(packet_bin[pointer : pointer + 3]) == '100': # packet represents a literal
        read_literal()
    else: # packet represents an operator
        read_operator()
"""

print(read_operator(3))