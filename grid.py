# TODO: Generate paths to treats from center or to center, already made helper to locate mid
import numpy as np
import random
import sys

np.set_printoptions(threshold=np.inf)


def _get_diff(inpt_one: list, sub_inpt: list) -> list[int, int]:
    """ helper function to get diff of two [n, n] lists """
    # column integer is negative for now, might need to change
    return [int(inpt_one[0] - sub_inpt[0]), -abs(inpt_one[1] - sub_inpt[1])]


def _locate_mid(grid: np.ndarray) -> list:
    """ helper function to locate middle of grid """
    shape: list = list(grid.shape)
    for i, _ in enumerate(shape):
        shape[i] = shape[i] - int(2)

    row_mod: int = int(shape[0]) % 2
    if row_mod > 0:
        row_pos: int = round((int(shape[0]) / 2) + row_mod)
    elif row_mod == 0:
        row_pos: int = int(shape[0]) / 2

    col_mod: int = int(shape[1]) % 2
    if col_mod > 0:
        col_pos: int = round((int(shape[1]) / 2) + col_mod)
    elif col_mod == 0:
        col_pos: int = int(shape[1]) / 2

    return [row_pos, col_pos]


def gen_paths(grid: np.ndarray) -> np.ndarray:
    # works only for treat position in top left of matrix
    treat_pos: list[list] = [
        [0, 0]
    ]
    for treat in treat_pos:
        start: list = treat
        get_to: list = _locate_mid(grid=grid)

        go: bool = True
        while go:
            choice: str = str(random.choice(['down', 'right']))
            print('Choice: ', choice)
            if str(choice) == 'down':
                if start[0] < get_to[0]:
                    start[0] = int(start[0]) + 1
                    if start != get_to:
                        print(start, get_to)
                        grid[1:-1, 1:-1][start[0],
                                         start[1]] = np.byte(9)
            if str(choice) == 'right':
                if start[1] < get_to[1]:
                    start[1] = int(start[1]) + 1
                    if start != get_to:
                        print(start, get_to)
                        grid[1:-1, 1:-1][start[0], start[1]] = np.byte(9)
            if start == get_to:
                print(start, get_to)
                go = False

    return grid


def gen_treats(grid: np.ndarray) -> np.ndarray:
    """ generates treats at each corner of traversable area, using 4 """
    # generate the treats in the four corners of the map
    treat_pos: list[list] = [
        [[0, 0], [0, -1]],
        [[-1, 0], [-1, -1]],
    ]
    for pos in treat_pos:
        grid[1:-1, 1:-1][pos[0][0], pos[0][1]] = np.byte(4)
        grid[1:-1, 1:-1][pos[1][0], pos[1][1]] = np.byte(4)

    return grid


def gen_obstacles(grid: np.ndarray) -> np.ndarray:
    """ randomly generates obstacles, using 1 """
    with np.nditer(grid[1:-1, 1:-1], op_flags=['readwrite']) as ar:
        for x in ar:
            x[...] = random.choice([np.byte(1), np.byte(0)])

    return grid


def convert_boundaries(grid: np.ndarray) -> np.ndarray:
    """ converts boundaries of grid to walls, in this case 1 """
    for i, _ in enumerate(grid[0]):
        grid[0][i] = np.byte(1)
        grid[-1][i] = np.byte(1)

    for row in grid[1:-1]:
        row[0] = np.byte(1)
        row[-1] = np.byte(1)

    return grid


def create_grid(row: int = 25, column: int = 33) -> np.ndarray:
    """ creates a grid using np.ndarray zeros """
    # min grid size 5x10
    grid: np.ndarray = np.zeros(
        shape=(row, column), dtype=np.byte, order='c')

    return grid


if __name__ == "__main__":
    grid: np.ndarray = create_grid()
    grid = convert_boundaries(grid=grid)
    grid = gen_obstacles(grid=grid)
    grid = gen_treats(grid=grid)
    position: list = _locate_mid(grid=grid)
    grid[position[0], position[1]] = np.byte(7)
    print(gen_paths(grid=grid))
    print(position)
