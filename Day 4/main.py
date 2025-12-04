# https://adventofcode.com/2025/day/4

def read_2d_array(filename):
    arr = []
    with open(filename, 'r') as file:
        for line in file:
            arr.append([1 if c == '@' else 0 for c in line.strip()])
    return arr

# Count number of accessible rolls (1s) and compose new array
def count_accessible_rolls(arr):
    count = 0
    rows = len(arr)
    cols = len(arr[0]) if rows > 0 else 0
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    new_arr = []
    for r in range(rows):
        new_row = []

        for c in range(cols):
            new_col = arr[r][c]
            if arr[r][c] == 1:
                adj_sum = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        adj_sum += arr[nr][nc]
                if adj_sum < 4:
                    count += 1
                    new_col = 0
            new_row.append(new_col)

        new_arr.append(new_row)

    return count, new_arr

def first(filename):
    arr = read_2d_array(filename)
    count, _ = count_accessible_rolls(arr)
    return count

def second(filename):
    arr = read_2d_array(filename)
    total_count = 0
    while True:
        count, arr = count_accessible_rolls(arr)
        if count == 0:
            break
        total_count += count
    return total_count

print('Part 1: ', first(filename='input'))
print('Part 2: ', second(filename='input'))