# https://adventofcode.com/2025/day/5

def read_ranges_and_ids(filename):
    ranges = []
    ids = []
    with open(filename, 'r') as file:
        lines = [line.rstrip('\n') for line in file]
    blank_idx = lines.index('')
    for line in lines[:blank_idx]:
        start, end = map(int, line.split('-'))
        ranges.append((start, end))
    for line in lines[blank_idx+1:]:
        if line:
            ids.append(int(line))
    return ranges, ids

def first(filename):
    ranges, ids = read_ranges_and_ids(filename)
    count = 0
    for id in ids:
        for start, end in ranges:
            if start <= id <= end:
                count += 1
                break
    return count

def second(filename):
    ranges, _ = read_ranges_and_ids(filename)
    
    if not ranges:
        return 0
    # Sort ranges by start
    ranges.sort()
    merged = [ranges[0]]    
    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    # Sum the lengths of merged ranges
    total = sum(end - start + 1 for start, end in merged)
    return total

print('Part 1: ', first(filename='input'))
print('Part 2: ', second(filename='input'))