with open('inputs/day3.txt', 'r') as file:
    numbers = [line.strip() for line in file.readlines()]
    bits = [0] * len(numbers[0])
    for i in range(len(bits)):
        for number in numbers:
            bits[i] += int(number[i])
    bits_binary = ['1' if bit > len(numbers) / 2 else '0' for bit in bits]
    gamma = int("".join(bits_binary), 2)
    epsilon = int("".join(['0' if bit == '1' else '1' for bit in bits]), 2)
    
    print(gamma * epsilon)
    
    
    oxygen = numbers.copy()
    bits_oxygen = [0] * len(numbers[0])
    co2 = numbers.copy()
    bits_co2 = [0] * len(numbers[0])

    count = 0
    while len(oxygen) != 1:
        bits_oxygen = [0] * len(numbers[0])
        for i in range(len(bits)):
            for number in oxygen:
                bits_oxygen[i] += int(number[i])
        bits_oxygen_binary = ['1' if bit >= len(oxygen) / 2 else '0' for bit in bits_oxygen]
        oxygen = [num for num in oxygen if num[count] == bits_oxygen_binary[count]]
        count += 1

    count = 0
    while len(co2) != 1:
        bits_co2 = [0] * len(numbers[0])
        for i in range(len(bits)):
            for number in co2:
                bits_co2[i] += int(number[i])
        bits_co2_binary = ['0' if bit >= len(co2) / 2 else '1' for bit in bits_co2]
        co2 = [num for num in co2 if num[count] == bits_co2_binary[count]]
        count += 1
        

co2, oxygen = co2[0], oxygen[0]
print(int(co2, 2) * int(oxygen, 2))

    
