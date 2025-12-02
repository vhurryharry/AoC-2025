# https://adventofcode.com/2025/day/2

def first(filename):
    sum = 0

    with open(filename, 'r') as file:
        line = file.readline().strip()
        ranges = line.split(',')
        for r in ranges:
            first, last = r.split('-')
            
            for i in range(int(first), int(last)+1):
                s = str(i)
                n = len(s)
                if n % 2 == 0 and s[:n//2] == s[n//2:]:
                    sum += i

    return sum


def second(filename):
    sum = 0

    with open(filename, 'r') as file:
        line = file.readline().strip()
        ranges = line.split(',')
        for r in ranges:
            first, last = r.split('-')
            
            for i in range(int(first), int(last)+1):
                s = str(i)
                n = len(s)
                for l in range(1, n//2+1):
                    if n % l == 0:
                        if s == s[:l] * (n // l):
                            sum += i
                            break

    return sum


print('Part 1: ', first(filename='input'))
print('Part 2: ', second(filename='input'))