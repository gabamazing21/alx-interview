#!/usr/bin/python3
"""this module for solcing interview questions"""


def island_perimeter(grid):
    """
    calculate the perimeter of an island in a grid where:
    - 0 represent water
    - 1 represent landing
    - Grid is rectangular and surrounded by water
    - only one island exists (or none)
    - No lakes inside the island

    Args:
      grid (List[List[int]]): A rectangular grids of 0s and 1s

    Returns:
      ints: The perimeter of the island

    """

    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            # Only procedd land cells
            if grid[row][col] == 1:
                cell_perimeter = 4

                if row > 0 and grid[row - 1][col] == 1:
                    cell_perimeter -= 1

                if row < rows - 1 and grid[row + 1][col] == 1:
                    cell_perimeter -= 1

                if col > 0 and grid[row][col - 1] == 1:
                    cell_perimeter -= 1

                if col < cols - 1 and grid[row][col + 1] == 1:
                    cell_perimeter -= 1

                perimeter += cell_perimeter
    return perimeter
