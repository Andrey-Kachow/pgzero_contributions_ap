import random

def grass_draw_func(x, y):
    screen.blit('grass', (x, y))


def rocks_draw_func(x, y):
    screen.blit('rocks', (x, y))


def generate_tile_draw_func():
    options = [
        grass_draw_func,
        rocks_draw_func
    ]
    selected_option_index = random.randint(0, len(options) - 1)
    return options[selected_option_index]



WIDTH = 500
HEIGHT = 500

white = (255, 255, 255)

tile_size = 20
tile_rows = HEIGHT // tile_size
tile_columns = WIDTH // tile_size

tilemap = []
for row in range(tile_rows):
    row_tiles = []
    for col in range(tile_columns):
        tile_draw_func = generate_tile_draw_func()
        row_tiles.append(tile_draw_func)
    tilemap.append(row_tiles)


def draw():
    for i, y in enumerate(range(0, HEIGHT, tile_size)):
        for j, x in enumerate(range(0, WIDTH, tile_size)):
            tilemap[i][j](x, y)

