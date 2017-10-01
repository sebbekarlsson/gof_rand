from gof_rand.utils import tobits
import numpy as np
from PIL import Image
import imageio


def get_new_grid(size=256):
    grid = []

    for x in range(0, size):
        grid.append([])
        
        for y in range(0, size):
            grid[x].append([])

    return grid

def populate_grid(grid, seed):
    seed_bits = tobits(seed)

    if len(seed_bits) < len(grid) * len(grid[0]):
        moving_index = 0
        for i, bit in enumerate(seed_bits):
            seed_bits.append(seed_bits[i])

            if len(seed_bits) >= len(grid) * len(grid[0]):
                break

    seed_bits_index = 0
    for x in range(0, len(grid)):
        for y in range(0, len(grid[x])):
            grid[x][y] = seed_bits[seed_bits_index]
            seed_bits_index += 1


    return grid

def get_random_number_from_grid(grid, times=1):
    number = 0
    im = np.zeros((len(grid), len(grid), 3), dtype=np.uint8)
    filenames = []
    images = []

    for i in range(times):
        for x in range(0, len(grid)):
            for y in range(0, len(grid[x])):
                bit_left = grid[max(0, x-1)][y]
                bit_right = grid[min(len(grid[x])-1, x+1)][y]
                bit_up = grid[x][max(0, y-1)]
                bit_down = grid[x][min(len(grid[y])-1, y+1)]
                bit = grid[x][y]

                counted = bit_left + bit_right + bit_up + bit_down

                if counted == 3:
                    grid[x][y] = 1

                if counted < 2 or counted > 3:
                    grid[x][y] = 0
        
        im = np.zeros((len(grid), len(grid), 3), dtype=np.uint8)        
        for x in range(0, len(grid)):
            for y in range(0, len(grid[x])):
                im[x][y] = 255 if grid[x][y] >= 1 else 0
                number += grid[x][y]

        
        img = Image.fromarray(im, 'RGB')
        #img.show()

        img.save('out/{}.jpg'.format(i))

        filenames.append('out/{}.jpg'.format(i))


    for filename in filenames:
        images.append(imageio.imread(filename))
        imageio.mimsave('out/movie.gif', images)
            
    return number
