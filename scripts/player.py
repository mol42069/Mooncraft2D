import pygame as pg

class Player:

    def __init__(self, sprite=None, pos=None):

        if pos is None:
            pos = [0, 0]
        self.pos = pos
        if sprite is None:
            print('ERROR: Player has no sprite!')
            exit()
        self.sprite = sprite
        self.sprite = pg.transform.scale(self.sprite, (50, 100))
        self.rec = self.sprite.get_rect()
        self.rec.topleft = [self.pos[0] - 25, self.pos[1] - 50]
        self.act_pos = [
                        1920 / 2 - 25,
                        1080 / 2 - 50
                        ]
        self.a_rec = self.sprite.get_rect()
        self.a_rec.topleft = self.pos

        return

    def draw(self, root):
        root.blit(self.sprite, self.act_pos)
        return root