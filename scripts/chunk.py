from scripts import world_gen
from scripts import block
from scripts import enums
import pygame as pg
import math

light_blue = (0, 60, 100)                       # sky color

class Chunk:

    def __init__(self, x, y, width, seed, sprites, sprite_size):
        self.surface = pg.Surface((width * sprite_size, 256 * sprite_size))         # we make the bg sky color!
        self.surface.fill(light_blue)
        self.x = x                                          # only x because a chunk will go from top to bottom
        self.prev_chunk = None
        self.y = y
        self.width = width
        self.seed = seed
        self.sprites = sprites[0]
        self.s_atlas = sprites[1]
        self.sprite_size = sprite_size
        self.loaded = True
        self.contents = []                              # 2d array must be init to the size of 1 chunk
        self.blocks = []
        self.height_map = None
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


    def save_chunk(self, csv_data, chunk, chunk_data_begin=1, max_min = 2):
        self.get_contents()
        save_csv_data = [chunk, self.save_data]
        csv_data.insert(chunk_data_begin, save_csv_data)

        return csv_data

    def load(self):
        # TODO: load saved chunk

        return

    def move(self, move_x, move_y):
        #self.check_col()
        self.x += move_x
        self.y += move_y


    def draw(self, root):
        root.blit(self.surface, (self.x * self.sprite_size, self.y * self.sprite_size))
        return root

    def gen_chunk(self):
        this_row = []
        self.contents, self.height_map = world_gen.gen(self.x + self.seed, self.width)
        for y, row in enumerate(self.contents):
            this_row = []
            for x, cell in enumerate(row):
                if cell.value != 0:
                    this_sp = self.sprites[cell.value]
                    b = block.Block(cell, this_sp, (x, y), self.sprite_size)
                    this_row.append(b)
                    self.surface = b.draw(self.surface, (x * self.sprite_size, y * self.sprite_size))

                else:
                    this_row.append(None)

        self.blocks.append(this_row)

        return

    def ground_col(self, player, pot_pos):
        final_pos = None
        b_pos = [math.floor((pot_pos[0]/self.sprite_size) - self.x), math.floor((pot_pos[1]/self.sprite_size) - self.y)]
        pot_player_rec = player.rec
        pot_player_rec.topleft = [pot_pos[0] - self.sprite_size / 2, pot_pos[1] - self.sprite_size]

        if self.blocks[b_pos[0]][b_pos[1]].collides(pot_player_rec):
            final_pos = [
                            self.blocks[b_pos[0]][b_pos[1]].pos[0] * self.sprite_size + self.sprite_size / 2 + self.x,
                            player.pos[1]
                        ]
            return final_pos

        return  final_pos
        # because the player pos is in actual pixels and the blocks get their position in relation to the sprite they
        # are on and in what block they are in that chunk so for final_pos we must address this

    def col_g(self, player, cur_chunk_id):
        print(player.pos[0])
        print(cur_chunk_id)
        print(self.height_map)
        print(self.width)
        print(self.sprite_size)
        if player.pos[1] - 50 >= self.height_map[math.floor((player.pos[0] - cur_chunk_id * self.width) / self.sprite_size)] * 64:
            return True
        else:
            return False

        # for row in self.blocks:
        #     for cell in row:
        #         a = cell.collides(player.a_rec, [self.x / self.sprite_size, self.y / self.sprite_size])
        #         if a:
        #             return a