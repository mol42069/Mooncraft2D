import pygame as pg
import random
import time
from scripts import chunk
from scripts import SpriteLoader


grey = (50, 50, 50)

def key_pressed(input_key):
    keys_pressed = pg.key.get_pressed()
    if keys_pressed[input_key]:
        return True
    else:
        return False


def main():
    pg.init()
    screen_size = (1920, 1080)
    root = pg.display.set_mode(screen_size)
    sprite_size = 50
    seed = random.randint(100, 999)
    SpriteLoader.init()
    sprites = SpriteLoader.get_sprites()
    root.fill(grey)
    c_pos = [90, -1000]
    chunks = chunk.Chunk(0, c_pos[1], 64, seed, sprites, sprite_size)
    fps_counter = 0
    t = time.time()

    while True:
        f_t = time.time()
        if f_t - t > 1:
            print(fps_counter)
            fps_counter = 0
            t = f_t
        fps_counter +=1
        pg.display.update()
        root.fill(grey)

        for event in pg.event.get():
            match event.type:
                case pg.QUIT:
                    exit()
        if key_pressed(pg.K_d):
            right = True
        else:
            right = False
        if key_pressed(pg.K_a):
            left = True
        else:
            left = False
        if key_pressed(pg.K_w):
            up = True
        else:
            up = False
        if key_pressed(pg.K_s):
            down = True
        else:
            down = False
        if left:
            c_pos[0] += 10
        elif right:
            c_pos[0] -= 10

        if up:
            c_pos[1] += 10
        elif down:
            c_pos[1] -= 10

        chunks.draw(root, c_pos[0], c_pos[1])


if __name__ == '__main__':
    main()
