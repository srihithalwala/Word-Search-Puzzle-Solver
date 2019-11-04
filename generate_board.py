import random
import string
import numpy as np


def make_grid():
    handle = open('usa.txt')
    words = handle.readlines()
    handle.close()

    words = [random.choice(words).upper().strip() for _ in range(5)]
    grid_size = 20
    grid = [['_' for _ in range(grid_size)] for _ in range(grid_size)]

    posibilities = ['leftright', 'updown', 'diagonalup', 'diagonaldown']
    for word in words:
        word_length = len(word)

        placed = False
        while not placed:
            position = random.choice(posibilities)
            # orientations
            if position == 'leftright':
                step_x = 1
                step_y = 0
            if position == 'updown':
                step_x = 0
                step_y = 1
            if position == 'diagonaldown':
                step_x = 1
                step_y = 1
            if position == 'diagonalup':
                step_x = 1
                step_y = -1
            # choosing a point
            x_position = random.randrange(grid_size)
            y_position = random.randrange(grid_size)
            # see if we can fit the word
            ending_x = x_position + word_length*step_x
            ending_y = y_position + word_length*step_y
            if ending_x < 0 or ending_x >= grid_size:
                continue
            if ending_y < 0 or ending_y >= grid_size:
                continue
            # if we fall out of grid dimensions we should restart the check
            # otherwise place the word
            failed = False  # checking with a boolean value
            for i in range(word_length):
                character = word[i]
                new_position_x = x_position + i*step_x
                new_position_y = y_position + i*step_y

                character_at_new_position = grid[new_position_x][new_position_y]
                if character_at_new_position != '_':
                    if character_at_new_position == character:
                        continue
                    else:
                        failed = True
                        break
            if failed:
                continue
            else:
                for i in range(word_length):
                    character = word[i]
                    new_position_x = x_position + i*step_x
                    new_position_y = y_position + i*step_y

                    grid[new_position_x][new_position_y] = character

                placed = True

    for x in range(grid_size):
        for y in range(grid_size):
            if grid[x][y] == '_':
                grid[x][y] = random.choice(string.ascii_uppercase)

    grid_arr = np.array(grid)
    return grid_arr, words



# grid = print_grid()
# for x in range(grid_size):
#     print('\t'*5+''.join(grid[x]))
# print(make_grid())
