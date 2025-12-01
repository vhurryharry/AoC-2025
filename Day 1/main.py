# https://adventofcode.com/2025/day/1

MAXIMUM = 100

def first(filename):
    count = 0
    cur = 50

    with open(filename, 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            direction = line[0]
            number = int(line[1:])
            
            if direction == 'R':
                cur = (cur + number) % MAXIMUM
            elif direction == 'L':
                cur = (cur - number) % MAXIMUM

            if cur == 0:
                count += 1

    return count

def second(filename):
    count = 0
    cur = 50
    with open(filename, 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            direction = line[0]
            number = int(line[1:])
            if direction == 'R':
                count += ((cur + number) // MAXIMUM) - (cur // MAXIMUM)
                cur = (cur + number) % MAXIMUM
            elif direction == 'L':
                count += (-(cur - number) // MAXIMUM) - (-(cur) // MAXIMUM)
                cur = (cur - number) % MAXIMUM
    return count

print(second(filename='input'))