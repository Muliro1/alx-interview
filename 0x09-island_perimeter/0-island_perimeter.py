#!/usr/bin/python3
"""Module for Island Perimeter
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in the grid.

    Args:
        grid (list of list of int): The grid representing the island.

    Returns:
        int: The perimeter of the island.
    """
    # Determine the number of rows and columns in the grid
    rows = len(grid)
    cols = len(grid[0])

    # Initialize the perimeter variable to 0
    perimeter = 0

    # Loop through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # Check if the current cell represents land
            if grid[i][j] == 1:
                # Check the top edge
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1  # Add 1 to the perimeter for each top edge

                # Check the bottom edge
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1  # Add 1 to the perimeter for each bottom edge

                # Check the left edge
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1  # Add 1 to the perimeter for each left edge

                # Check the right edge
                if j == cols-1 or grid[i][j+1] == 0:
                    perimeter += 1  # Add 1 to the perimeter for each right edge

    # Return the total perimeter
    return perimeter
