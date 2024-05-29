#!/usr/bin/python3
""" doc doc doc """


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise

    The algorithm first swaps the elements of each row and column
    and then reverses each row.
    """
    m = len(matrix)

    # Swap elements of each row and column
    for i in range(m):
        for j in range(i, m):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    # Reverse each row
    for i in range(m):
        matrix[i] = matrix[i][::-1]
