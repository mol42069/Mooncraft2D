import pygame as pg
import random
import time
from scripts import chunk
from scripts import saver
from scripts import SpriteLoader


grey = (50, 50, 50)

def key_pressed(input_key):
    keys_pressed = pg.key.get_pressed()
    if keys_pressed[input_key]:
        return True
    else:
        return False

def create_save(save_name):
    path = './resources/worldSaves/'
    csv_file = path + save_name + '.csv'
    with open(csv_file, 'a+') as file:
        file.write('')

def load_save(save_name):

    return




def main():

    save_name = input('YOUR SAVE NAME:')
    create_save(save_name)
    pg.init()
    screen_size = (1920, 1080)
    root = pg.display.set_mode(screen_size)
    sprite_size = 50
    seed = random.randint(100, 999)
    SpriteLoader.init()
    sprites = SpriteLoader.get_sprites()
    s_atlas = SpriteLoader.get_atlas()
    s_all = [sprites, s_atlas]
    root.fill(grey)
    chunks = [chunk.Chunk(90, -1000, 64, seed, s_all, sprite_size, save_name)]
    fps_counter = 0
    t = time.time()
    data = [['Items etc']]
    path = './resources/worldSaves/' + save_name + '.csv'

    while True:
        f_t = time.time()
        if f_t - t > 1:
            saver.save_world(data, chunks, path)
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
            chunks[0].move(10, 0)
        elif right:
            chunks[0].move(-10, 0)

        if up:
            chunks[0].move(0, 10)
        elif down:
            chunks[0].move(0, -10)

        chunks[0].draw(root)


if __name__ == '__main__':
    main()
