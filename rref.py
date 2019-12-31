A = [[1, 2, 5],
     [2, 4, 1],
     [2, 2, 2]]

B = [[1, 2],
     [2, 4],
     [2, 2]]

C = [[0, 3, 5],
     [2, 1, 2],
     [0, 4, 0]]


def matrix_organizer(matrix):
    ''' function for preparing the rows of a matrix to be able to get
        row reduced. On the diagonal should be as much > 0 numbers as possible'''
    columns = len(matrix[0])
    zero_indexes = []
    for row in range(columns):
        if matrix[row][row] == 0:
            zero_indexes.append(row)

    for row in matrix:
        for i in zero_indexes:
            if row[i] > 0:
                matrix = matrix[row[i]:] + matrix[:row[i]]

    return matrix


def rref(matrix):
    ''' function that row reduces any n*m matrix by using the
        Gauss-Jordan Elimination Algorithm '''

    # shift rows to get the right pivot first before row reducing
    matrix = matrix_organizer(matrix)

    rows = len(matrix)
    columns = len(matrix[0])
    pivot_entry = 0
    for row in range(columns):
        # reduce pivot to 1
        row_entries = len(matrix[row])
        if matrix[row][pivot_entry] != 0:
            pivot = matrix[row][pivot_entry]
            matrix[row][pivot_entry] = pivot * (1 / pivot)
            for i in range(pivot_entry+1, row_entries):
                matrix[row][i] = matrix[row][i] * (1 / pivot)

        # all entries directly below pivot to zero
        for next_row in range(row+1, rows):
            if matrix[next_row][pivot_entry] != 0:
                matrix[next_row][pivot_entry] = matrix[next_row][pivot_entry] - \
                    (matrix[next_row][pivot_entry]
                     * matrix[row][pivot_entry])

        # reduce all numbers above to zero to get the rref form
        for upper_row in range(0, row):
            if matrix[upper_row][pivot_entry] != 0:
                matrix[upper_row][pivot_entry] = matrix[upper_row][pivot_entry] - \
                    (matrix[upper_row][pivot_entry]
                     * matrix[row][pivot_entry])

        pivot_entry += 1

    return matrix


print(rref(C))
