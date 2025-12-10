# https://adventofcode.com/2025/day/7

def parse_input(filename):
    with open(filename, 'r') as f:
        lines = [line.rstrip('\n') for line in f]

    # beam_arr from first line (line 0)
    first_line = lines[0]
    beams = [1 if c == 'S' else 0 for c in first_line]

    # splitter_arr from odd lines after the first (lines 2,4,...)
    splitters = []
    for i in range(2, len(lines), 2):
        row = [1 if c == '^' else 0 for c in lines[i]]
        splitters.append(row)
    return beams, splitters

def first(filename):
    beams, splitters = parse_input(filename)
    count = 0
    for line in splitters:        
        beam_indices = [i for i, v in enumerate(beams) if v == 1]
        for idx in beam_indices:
            if line[idx] == 1:
                beams[idx] = 0
                count += 1
                if idx - 1 >= 0:
                    beams[idx - 1] = 1
                if idx + 1 < len(beams):
                    beams[idx + 1] = 1

    return count

def second(filename):
    beams, splitters = parse_input(filename)
    width = len(beams)
    start = beams.index(1)
    memo = {}

    def dp(pos, row):
        if (pos, row) in memo:
            return memo[(pos, row)]
        if row == len(splitters):
            return 1
        if splitters[row][pos] == 1:
            total = 0
            if pos - 1 >= 0:
                total += dp(pos - 1, row + 1)
            if pos + 1 < width:
                total += dp(pos + 1, row + 1)
            memo[(pos, row)] = total
            return total
        else:
            result = dp(pos, row + 1)
            memo[(pos, row)] = result
            return result

    return dp(start, 0)

print('Part 1: ', first(filename='input'))
print('Part 2: ', second(filename='input'))