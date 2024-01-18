def reshape_the_matrix(matrix, r, c):
    n = len(matrix)
    m = len(matrix[0])

    total = m * n

    if r * c != total:
        return matrix

    result = [[0 for i in range(c)] for j in range(r)]

    for y in range(0, r):
        for x in range(0, c):
            index = y * c + x
            yy = index // m
            xx = index % m

            result[y][x] = matrix[yy][xx]

    return result
