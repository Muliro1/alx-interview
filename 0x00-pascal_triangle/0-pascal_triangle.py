#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    my_list = []
    if n <= 0:
        return my_list
    my_list = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(my_list[i - 1]) - 1):
            curr = my_list[i - 1]
            temp.append(my_list[i - 1][j] + my_list[i - 1][j + 1])
        temp.append(1)
        my_list.append(temp)
    return my_list
