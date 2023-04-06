import pygame as pg
import random
from scripts import chunk
from scripts import SpriteLoader


grey = (50, 50, 50)


def main():
    pg.init()
    screen_size = (1920, 1080)
    root = pg.display.set_mode(screen_size)
    sprite_size = 50
    seed = random.randint(100, 999)
    sl = SpriteLoader.init()
    sprites = SpriteLoader.get_sprites()
    root.fill(grey)
    c_pos = [10, -85]
    chunks = chunk.Chunk(0, 32, seed, sprites, sprite_size)

    while True:

        pg.display.update()
        root.fill(grey)



        for event in pg.event.get():
            match event.type:
                    case pg.KEYDOWN:
                        match event.key:
                            case pg.K_w:
                                c_pos[1] += 1
                            case pg.K_s:
                                c_pos[1] -= 1
                            case pg.K_a:
                                c_pos[0] += 1
                            case pg.K_d:
                                c_pos[0] -= 1

                    case pg.QUIT:
                        exit()

        chunks.draw(root, c_pos[0], c_pos[1])


if __name__ == '__main__':
    main()
