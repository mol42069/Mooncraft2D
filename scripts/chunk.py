from scripts import world_gen
from scripts import block
from scripts import enums
import pygame as pg

light_blue = (0, 60, 100)                       # sky color

class Chunk:

    def __init__(self, x, y, width, seed, sprites, sprite_size):
        self.surface = pg.Surface((width * sprite_size, 256 * sprite_size))         # we make the bg sky color!
        self.surface.fill(light_blue)
        self.x = x                                          # only x because a chunk will go from top to bottom
        self.y = y
        self.width = width
        self.seed = seed
        self.sprites = sprites[0]
        self.s_atlas = sprites[1]
        self.sprite_size = sprite_size
        self.loaded = True
        self.contents = []                              # 2d array must be init to the size of 1 chunk
        self.blocks = []
        self.gen_chunk()
        self.save_data = []

        return

    def get_contents(self):
        data = []
        for row in self.contents:
            r_data = []
            for cell in row:
                match cell:
                    case enums.Block.dirt:
                        r_data.append(1)
                    case enums.Block.grass:
                        r_data.append(2)
                    case enums.Block.stone:
                        r_data.append(3)
                    case enums.Block.air:
                        r_data.append(0)
            data.append(r_data)
        self.save_data =  data


    def save_chunk(self, csv_data, chunk_data_begin=1):
        self.get_contents()
        if self.x < 0:
            csv_data.insert(chunk_data_begin, self.save_data)
        else:
            csv_data.append(self.save_data)

        return csv_data

    def load(self):
        # TODO: load saved chunk

        return

    def move(self, move_x, move_y):
        self.x += move_x
        self.y += move_y


    def draw(self, root):
        root.blit(self.surface, (self.x * self.sprite_size, self.y * self.sprite_size))
        return root

    def gen_chunk(self):
        this_col = []
        self.contents = world_gen.gen(self.x + self.seed, self.width)
        for y, col in enumerate(self.contents):
            this_col = []
            for x, cell in enumerate(col):
                if cell.value != 0:
                    this_sp = self.sprites[cell.value]
                    b = block.Block(cell, this_sp, (x, y), self.sprite_size)
                    this_col.append(b)
                    self.surface = b.draw(self.surface, (x * self.sprite_size, y * self.sprite_size))

                else:
                    this_col.append(None)

        self.blocks.append(this_col)
        return
