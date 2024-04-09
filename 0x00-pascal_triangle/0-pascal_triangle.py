#!/usr/bin/python3
"""
Pascal's triangle
"""


def pascal_triangle(n):
    """
    pascal's triangle
    """
    empty_list = [[]]
    if n <= 0:
        return empty_list
    my_list = []
    while n > 0:
        for i in range(n):
            temp_list = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    temp_list.append(1)
                else:
                    temp_list.append(my_list[i - 1] [j - 1] + my_list[i - 1] [j])
            my_list.append(temp_list)
        n -= 1
        break
    return(my_list)
