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


class AbstractTank:

    RIGHT = 0
    UP = 1
    LEFT = 2
    DOWN = 3

    IDLE = 4
    MOVING = 5
    DESTROYED = 6

    def __init__(self, x, y, actor):
        self.orientation = AbstractTank.UP
        self.state = AbstractTank.IDLE
        self.actor = actor
        actor.top_left = x, y

    def draw(self):
        self.actor.draw()


class PlayerTank(AbstractTank):
    pass



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



player = PlayerTank(40, 40, Actor('tank'))



def draw():
    for i, y in enumerate(range(0, HEIGHT, tile_size)):
        for j, x in enumerate(range(0, WIDTH, tile_size)):
            tilemap[i][j](x, y)

    player.draw()

