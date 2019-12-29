# rref any matrix
A = [[1, 2, 5],
     [2, 4, 1],
     [2, 2, 2]]


def rref(matrix):
    ''' function that row reduces any n*m matrix '''
    matrix = matrix
    rows = len(matrix)

    # shift rows to get the right pivor first before rref algo below

    pivot_entrie = 0
    for row in range(rows):
        # reduce pivot to 1
        row_entries = len(matrix[row])
        if matrix[row][pivot_entrie] != 0:
            pivot = matrix[row][pivot_entrie]
            matrix[row][pivot_entrie] = pivot * (1 / pivot)
            for i in range(pivot_entrie+1, row_entries):
                matrix[row][i] = matrix[row][i] * (1 / pivot)
        # all entries directly below pivot to zero
        for next_row in range(row+1, rows):
            if matrix[next_row][pivot_entrie] != 0:
                matrix[next_row][pivot_entrie] = matrix[next_row][pivot_entrie] - \
                    (matrix[next_row][pivot_entrie]
                     * matrix[row][pivot_entrie])
        pivot_entrie += 1

    # add/substract below all pivots to get the rref form

    return matrix


print(A)
print(rref(A))
