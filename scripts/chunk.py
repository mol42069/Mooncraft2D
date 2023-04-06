from scripts import world_gen
from scripts import block
import pygame as pg

light_blue = (0, 60, 100)                       # sky color

class Chunk:

    def __init__(self, x, y, width, seed, sprites, sprite_size):
        self.surface = pg.Surface((width * sprite_size, 256 * sprite_size))         # we make the bg sky color!
        self.surface.fill(light_blue)
        self.x = x                       # only x because a chunk will go from top to bottom
        self.y = y
        self.width = width
        self.seed = seed
        self.sprites = sprites
        self.sprite_size = sprite_size
        self.loaded = True
        self.contents = []  # 2d array must be init to the size of 1 chunk
        self.blocks = []
        self.gen_chunk()

        return

    def load(self):
        # TODO: load saved chunk

        return

    def unload(self):
        # TODO: save chunk then delete in program
        return

    def save_chunk_img(self):
        return

    def draw(self, root, pos_x, pos_y):
        root.blit(self.surface, (pos_x, pos_y))
        return root

    def gen_chunk(self):
        this_col = []
        self.contents = world_gen.gen(self.x + self.seed, self.width)
        for y, col in enumerate(self.contents):
            this_col = []
            for x, cell in enumerate(col):
                if cell.value != 999:
                    this_sp = self.sprites[cell.value]
                    b = block.Block(cell, this_sp, (x, y), self.sprite_size)
                    this_col.append(b)
                    self.surface = b.draw(self.surface, (x * self.sprite_size, y * self.sprite_size))

                else:
                    this_col.append(None)

        self.blocks.append(this_col)
        return
