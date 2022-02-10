

def o_win(matrix):
    # check horizontal for win
    o_count = 0
    for row in matrix:
        for char in row:
            if char == 0:
                o_count += 1
        if o_count == 3:
            return True
        else:
            o_count = 0

    # check vertical for win
    for i in range(3):
        for j in range(3):
            if matrix[j][i] == 0:
                o_count += 1
        if o_count == 3:
            return True
        else:
            o_count = 0

    # check diagonals for win
    for i in range(3):
        if matrix[i][i] == 0:
            o_count += 1
    if o_count == 3:
        return True
    else:
        o_count = 0
    for i in range(3):
        if matrix[i][abs(i-2)] == 0:
            o_count += 1
    if o_count == 3:
        return True
    return False
            

def x_win(matrix):
    # check horizontal for win
    x_count = 0
    for row in matrix:
        for char in row:
            if char == 1:
                x_count += 1
        if x_count == 3:
            return True
        else:
            x_count = 0

    # check vertical for win
    for i in range(3):
        for j in range(3):
            if matrix[j][i] == 1:
                x_count += 1
        if x_count == 3:
            return True
        else:
            x_count = 0

    # check diagonals for win
    for i in range(3):
        if matrix[i][i] == 1:
            x_count += 1
    if x_count == 3:
        return True
    else:
        x_count = 0
    for i in range(3):
        if matrix[i][abs(i-2)] == 1:
            x_count += 1
    if x_count == 3:
        return True
    return False
