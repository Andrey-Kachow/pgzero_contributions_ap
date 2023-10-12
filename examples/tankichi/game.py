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


class Directions:
    RIGHT = 0
    UP = 1
    LEFT = 2
    DOWN = 3
    

class AbstractTank:

    IDLE = 4
    MOVING = 5
    DESTROYED = 6

    REGULAR_SPEED = 3

    def __init__(self, x, y, actor):
        self.speed = AbstractTank.REGULAR_SPEED
        self.direction = Directions.UP
        self.state = AbstractTank.IDLE
        self.actor = actor
        actor.top_left = x, y

    def draw(self):
        self.actor.draw()

    def shoot(self):
        spawn_points = {
            Directions.UP: self.actor.midtop,
            Directions.DOWN: self.actor.midbottom,
            Directions.LEFT: self.actor.midleft,
            Directions.RIGHT: self.actor.midright
        }
        x, y = spawn_points[self.direction]
        bullet = Bullet(x, y, self.direction)
        bullets.append(bullet)


class PlayerTank(AbstractTank):
    pass


class Bullet:
    RADIUS = 4
    SPEED = 5

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = Bullet.SPEED

    def draw(self):
        x, y, r = self.x, self.y, Bullet.RADIUS
        screen.draw.filled_rect(Rect((x - r, y - r), (2 * r + 1, 2 * r + 1)), color=(255, 0, 0) )


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
bullets = []


direction_keymap = {
    keys.W: Directions.UP,
    keys.A: Directions.LEFT,
    keys.S: Directions.DOWN,
    keys.D: Directions.RIGHT
}

direction_keymap_flags = {
    keys.W: False,
    keys.A: False,
    keys.S: False,
    keys.D: False 
}


def draw():
    for i, y in enumerate(range(0, HEIGHT, tile_size)):
        for j, x in enumerate(range(0, WIDTH, tile_size)):
            tilemap[i][j](x, y)

    player.draw()
    for bullet in bullets:
        bullet.draw()


def update_player():
    if player.state == AbstractTank.MOVING:
        if player.direction == Directions.UP:
            player.actor.top -= player.speed
        elif player.direction == Directions.DOWN:
            player.actor.top += player.speed
        elif player.direction == Directions.LEFT:
            player.actor.right -= player.speed
        elif player.direction == Directions.RIGHT:
            player.actor.right += player.speed

def update_bullet(bullet):
    if bullet.direction == Directions.UP:
        bullet.y -= bullet.speed
    elif bullet.direction == Directions.DOWN:
        bullet.y += bullet.speed
    elif bullet.direction == Directions.LEFT:
        bullet.x -= bullet.speed
    elif bullet.direction == Directions.RIGHT:
        bullet.x += bullet.speed


def update():
    update_player()
    for bullet in bullets:
        update_bullet(bullet)


def on_key_down(key):
    if key not in direction_keymap:
        return
    direction_keymap_flags[key] = True
    player.direction = direction_keymap[key]
    player.state = AbstractTank.MOVING

def on_key_up(key):
    if key == keys.SPACE:
        player.shoot()
    if key not in direction_keymap:
        return
    direction_keymap_flags[key] = False
    if player.direction == direction_keymap[key]:
        for key_press, is_pressed in direction_keymap_flags.items():
            if is_pressed:
                player.direction = direction_keymap[key_press]
                break
        else:
            player.state = AbstractTank.IDLE

