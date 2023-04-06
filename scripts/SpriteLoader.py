import pygame
import os
from scripts import enums

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #
#   Sprites in Single must be 100x100 big size can be converted later
#   Sheets in multi must be : TODO: figure out a good size
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #

sprites = {}
animation_sprites = {}
size_on_sheet = (100, 100)

def init(scale=30, bg_scale=(1920 * 1.5, 1080 * 1.5), path_single='./resources/sprites/blocks',
         path_multi='./resources/sprites/multi', path_ani = './resources/sprites/animations',
         path_bg = './resources/sprites/background'):

    load_single(path_single, scale)
    # load_multi(path_multi, scale)
    # load_animations(path_ani, scale)
    # load_bg(path_bg, bg_scale)
    return

def load_single(path, scale):
    global sprites
    sprite_dir = os.listdir(path)
    # load all Sprites in Single-Folder
    for file in sprite_dir:
        if '.' in file:                                             # we check if there is a '.' in the filename
            cur_sprite = pygame.image.load(path + '/' + file)             # because if there isn't it is another folder
            cur_sprite = pygame.transform.scale(cur_sprite, (scale, scale))
            sprites.update({'single_' + file : cur_sprite})
        else:
            new_dir = os.listdir(path + '/' + file)                       # we iterate over all files/dictionary
            for one_file in new_dir:
                if '.' in one_file:
                    cur_sprite = pygame.image.load(path + '/' + file + '/' + one_file)
                    cur_sprite = pygame.transform.scale(cur_sprite, (scale, scale))
                    sprites.update({'single_' + one_file : cur_sprite})
                else:
                    nn_dir = os.listdir(path + '/' + file + '/' + one_file)
                    for two_file in nn_dir:
                        if '.' not in two_file:
                            print('ERROR TO DEEP DIRECTORY IN "Sprites/Single"')
                            pass
                        else:
                            cur_sprite = pygame.image.load(path + '/' + file + '/' + one_file + '/' + two_file)
                            cur_sprite = pygame.transform.scale(cur_sprite, (scale, scale))
                            sprites.update({'single_' + two_file : cur_sprite})
    return

def load_multi(path, scale):
    global sprites
    sprite_dir = os.listdir(path)
    # load all Sprites in Single-Folder
    for file in sprite_dir:
        if '.' in file:                                             # we check if there is a '.' in the filename
            cur_sprite = pygame.image.load(path + '/' +  file)             # because if there isn't it is another folder
            cur_sprite = pygame.transform.scale(cur_sprite, (scale, scale))
            sprites.update({'multi_' + file : cur_sprite})
        else:
            new_dir = os.listdir(path + '/' +  file)                       # we iterate over all files/dictionary
            for one_file in new_dir:
                if '.' in one_file:
                    cur_sprite = pygame.image.load(path + '/' +  file + '/' +  one_file)
                    cur_sprite = pygame.transform.scale(cur_sprite, (scale, scale))
                    sprites.update({'multi_' + one_file : cur_sprite})
                else:
                    nn_dir = os.listdir(path + '/' +  file + '/' +  one_file)
                    for two_file in nn_dir:
                        if '.' not in two_file:
                            print('ERROR TO DEEP DIRECTORY IN "Sprites/multi"')
                            pass
                        else:
                            cur_sprite = pygame.image.load(path + '/' +  file + '/' +  one_file + '/' +  two_file)
                            cur_sprite = pygame.transform.scale(cur_sprite, (scale, scale))
                            sprites.update({'multi_' + two_file : cur_sprite})
    return

def load_bg(path, scale):                # TODO: make the background resizeable so screensize
    global sprites                       # TODO: can be changed easily
    this_dir = os.listdir(path)
    for img in this_dir:
        cur_sprite = pygame.image.load(path + '/' + img)
        cur_sprite = pygame.transform.scale(cur_sprite, scale)
        sprites.update({'bg_' + img : cur_sprite})
    return

def load_animations(path, scale):
    ani_paths = os.listdir(path)
    for lost in ani_paths:
        b = path + '/' + lost
        a = os.listdir(b)
        for directory in a:
            d_path = b + '/' + directory
            d_folder = os.listdir(d_path)
            animation_folder = []
            for folder in d_folder:
                animation = []
                f_folder = d_path + '/' + folder
                ani = os.listdir(f_folder)
                for sprite in ani:
                    cur_sprite = pygame.image.load(f_folder + '/' + sprite)
                    cur_sprite = pygame.transform.scale(cur_sprite, (scale, scale))
                    animation.append(cur_sprite)
                animation_folder.append(animation)
            animation_sprites.update({directory : animation_folder})
    return

def get(sprite_name='filename', sprite_type='.png', is_multi=1, sheet_pos=enums.SheetPos.Empty):
    global sprites
    sprite_name += sprite_type
    if is_multi == 0:
        back = get_from_multi(sheet_pos, sprite_name)                   # we scale the sprite again
        return back
    elif is_multi == 1:
        back = sprites['single_' + sprite_name]
        if back is None:
            print('ERROR SPRITE NOT FOUND: ' + sprite_name)
            exit(404)
        else:
            return back
    elif is_multi == 2:
        back = sprites['bg_' + str(sprite_name)]
        if back is not None:
            return back
        else:
            print('ERROR SPRITE NOT FOUND: ' + sprite_name)
            exit(404)

def get_from_multi(sheet_pos=enums.SheetPos.Empty, sheet_name='name in sprite-dict'):
    global size_on_sheet
    sheet = sprites['multi_' + str(sheet_name)]
    rect = pygame.Rect(sheet_pos.value, size_on_sheet)
    image = pygame.Surface(rect.size).convert()
    image.blit(sheet, sheet_pos.value, rect)
    return image

def get_movement():
    return animation_sprites

def get_sprites():
    return sprites
