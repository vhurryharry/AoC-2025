# https://adventofcode.com/2025/day/3

def first(filename):
    sum = 0

    with open(filename, 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            digits = [int(d) for d in line]
            if len(digits) < 2:
                continue

            # Find largest in digits[0:n-1]
            max1 = max(digits[:-1])
            idx = digits.index(max1)
            # Find largest in digits[idx:]
            max2 = max(digits[idx+1:])
            
            sum += max1 * 10 + max2

    return sum


def second(filename):
    sum = 0
    NUM_DIGITS = 12

    with open(filename, 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            digits = [int(d) for d in line]
            if len(digits) < NUM_DIGITS:
                continue

            joltage = 0
            idx = -1
            n = len(digits)
            for i in range(NUM_DIGITS):
                # Find largest in digits[idx+1:n-NUM_DIGITS+i]
                # Fix: avoid shadowing built-in max function
                largest_digit = max(digits[idx+1:n-NUM_DIGITS+i+1])
                idx = digits.index(largest_digit, idx+1)
                joltage = joltage * 10 + largest_digit

            sum += joltage
    return sum


print('Part 1: ', first(filename='input'))
print('Part 2: ', second(filename='input'))