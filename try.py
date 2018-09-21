from gol_rand.random import get_random_number
from gol_rand.utils import images_to_gif


number, images = get_random_number(
    grid_width=128,
    gof_intervals=60,
    create_images=True
)

print(images_to_gif(images))



print(number, images)
