import pygame as pg
import random
import time
from scripts import chunk
from scripts import SpriteLoader
from scripts import chunk_mng as c_mng
from perlin_noise import PerlinNoise
import matplotlib.pyplot as plt


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
    seed = random.randint(100, 99999)
    SpriteLoader.init()
    sprites = SpriteLoader.get_sprites()
    s_atlas = SpriteLoader.get_atlas()
    s_all = [sprites, s_atlas]
    root.fill(grey)
    chunk_width = 64
    cur_pos = [0, -15]
    chunks = {0 : chunk.Chunk(0, -15, chunk_width, seed, s_all, sprite_size)}
    chunks.update({-1 : chunk.Chunk(0 - chunk_width, -15, chunk_width, seed - chunk_width, s_all, sprite_size)})
    chunks.update({1 : chunk.Chunk(0 + chunk_width, -15, chunk_width, seed + chunk_width, s_all, sprite_size)})
    chunks.update({-2: chunk.Chunk(0 - 2 * chunk_width, -15, chunk_width, seed - 2 * chunk_width, s_all, sprite_size)})
    chunks.update({2: chunk.Chunk(0 + 2 * chunk_width, -15, chunk_width, seed + 2 * chunk_width, s_all, sprite_size)})

    fps_counter = 0
    t = time.time()
    c_mng.m_init(chunks,sprites['single_player_test.png'])

    while True:
        chunks, root = c_mng.manage(root, cur_pos[0], chunk_width)
        f_t = time.time()
        if f_t - t > 1:
            #saver.save_world(data, chunks, path)
            print(fps_counter)
            fps_counter = 0
            t = f_t
        fps_counter +=1
        pg.display.update()
        root.fill(grey)

        for event in pg.event.get():
            match event.type:
                case pg.QUIT:
                    c_mng.threads_started = False
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
        if key_pressed(pg.K_ESCAPE):
            c_mng.threads_started = False
            exit()
        if left:
            c_mng.move(1, 0)
            cur_pos[0] -= 0.2
        elif right:
            c_mng.move(-1, 0)
            cur_pos[0] += 0.2
        if up:
            c_mng.move(0, 1)
            cur_pos[1] += 0.2
        elif down:
            c_mng.move(0, -1)
            cur_pos[1] -= 0.2

if __name__ == '__main__':



    # noise = PerlinNoise(octaves=10, seed=0)
    # pis = [[noise([x / 256, y / 256]) for x in range(256)] for y in range(256)]
    # plt.imshow(pis, cmap='gray')
    # plt.show()
    main()
