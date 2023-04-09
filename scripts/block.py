import pygame as pg

class Block:

    def __init__(self, block_type, sprite, s_pos, sprite_size):
        self.type = block_type

        self.sprite_size = sprite_size
        self.sprite = pg.transform.scale(sprite, (sprite_size, sprite_size))
        self.pos = s_pos

    def get_data(self):
        data = [
            self.type,
            self.pos
        ]
        return data

    def destroy(self):
        del self
        return

    def draw(self, surface, pos):
        surface.blit(self.sprite, pos)

        return surface
