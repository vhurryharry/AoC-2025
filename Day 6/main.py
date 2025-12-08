# https://adventofcode.com/2025/day/6

def read_matrix_and_ops(filename):
    matrix = []
    ops = []
    with open(filename, 'r') as file:
        lines = [line.strip('\n') for line in file if line.strip()]
    for line in lines[:-1]:
        row = line.split()
        matrix.append(row)
    ops = lines[-1].split()
    return matrix, ops, lines[:-1]


def calc_col(col, op):
    if op == '+':
        return sum(col)
    elif op == '*':
        prod = 1
        for val in col:
            prod *= val
        return prod
    return 0


def first(filename):
    matrix, ops, _ = read_matrix_and_ops(filename)    
    result = 0
    for i in range(len(ops)):
        op = ops[i]
        col = [int(matrix[j][i]) for j in range(len(matrix))]
        result += calc_col(col, op)

    return result

def second(filename):
    matrix, ops, lines = read_matrix_and_ops(filename)   

    lengths = []
    for i in range(len(ops)):
        max_length = 0
        for j in range(len(matrix)):
            length = len(matrix[j][i])
            if length > max_length:
                max_length = length
        lengths.append(max_length)

    matrix = []
    for i in range(len(lines)):
        row = []
        j = 0
        for k in range(len(lengths)):
            item = lines[i][j:j+lengths[k]]
            row.append(item)
            j += lengths[k] + 1
        matrix.append(row)

    result = 0
    for i in range(len(ops)):
        values = [0] * lengths[i]
        for j in range(lengths[i]):
            for k in range(len(lines)):
                if matrix[k][i][j] != ' ':
                    values[j] = values[j] * 10 + int(matrix[k][i][j])

        result += calc_col(values, ops[i])
    return result


print('Part 1: ', first(filename='input'))
print('Part 2: ', second(filename='input'))