import math
import threading
import time
from scripts import chunk
from scripts import saver
from scripts import player as pl

cur_chunks = []
chunks = {}
cur_chunk_pos = 0
threads_started = False
max_min = 2
move_x = 0
move_y = 0
move_m = [0, 0]
gravity = 0.3
momentum = 0.6
player = None
def load():
    global cur_chunks, chunks, cur_chunk_pos, threads_started, max_min
    chunk_width = chunks[0].width

    while True:
        if not threads_started:
            break

        try:
            chunks[cur_chunk_pos - 2]

        except KeyError:
            x = chunks[cur_chunk_pos].x -  2 * chunk_width
            n_sprites = [chunks[0].sprites, chunks[0].s_atlas]
            n_chunk = chunk.Chunk(x, chunks[cur_chunk_pos].y, chunk_width, chunks[0].seed, n_sprites, chunks[0].sprite_size)
            n_chunk.x = chunks[cur_chunk_pos].x - 2 * chunk_width
            chunks.update({cur_chunk_pos - 2 : n_chunk})
            print('load_right')
            save()

        try:
            chunks[cur_chunk_pos + 2]

        except KeyError:
            x = chunks[cur_chunk_pos].x + 2 * chunk_width
            n_sprites = [chunks[0].sprites, chunks[0].s_atlas]
            n_chunk = chunk.Chunk(x, chunks[cur_chunk_pos].y, chunk_width, chunks[-1].seed, n_sprites, chunks[-1].sprite_size)
            n_chunk.x = chunks[cur_chunk_pos].x + 2 * chunk_width
            chunks.update({cur_chunk_pos + 2 : n_chunk})
            print('load_left')
            save()

        try:
            cur_chunks = [chunks[cur_chunk_pos - 2], chunks[cur_chunk_pos - 1], chunks[cur_chunk_pos],
                          chunks[cur_chunk_pos + 1], chunks[cur_chunk_pos + 2]]
        except KeyError:
            # print('KeyError')
            pass

        cur_chunks[0].x = cur_chunks[2].x - 2 * chunk_width
        cur_chunks[1].x = cur_chunks[2].x - chunk_width
        cur_chunks[3].x = cur_chunks[2].x + chunk_width
        cur_chunks[4].x = cur_chunks[2].x + 2 * chunk_width

        if cur_chunk_pos - 2 < - max_min:
            max_min = -(cur_chunk_pos - 2)

        time.sleep(0.01)


def manage(root, cur_pos_x, chunk_width):
    global cur_chunks, chunks, cur_chunk_pos, threads_started, player
    cur_chunk_pos = math.floor(cur_pos_x / chunk_width) # must be rounded down
    #print(cur_chunk_pos)

    try:
        chunks[cur_chunk_pos + 1].y = chunks[cur_chunk_pos].y
        chunks[cur_chunk_pos - 1].y = chunks[cur_chunk_pos].y
        chunks[cur_chunk_pos + 2].y = chunks[cur_chunk_pos].y
        chunks[cur_chunk_pos - 2].y = chunks[cur_chunk_pos].y
    except IndexError:
        #print('IndexError')
        pass
    except KeyError:
        #print('KeyError')
        pass

    for c in cur_chunks:
        root = c.draw(root)

    root = player.draw(root)

    return chunks, root

def m_init(s_chunk, player_spites):
    global chunks, threads_started, cur_chunks, player
    chunks = s_chunk
    threads_started = True
    cur_chunks = [chunks[cur_chunk_pos - 1], chunks[cur_chunk_pos], chunks[cur_chunk_pos + 1]]
    p_pos = [1920 / 2 - 25, (1080 / 2 - 50) + 20 * 50]
    player = pl.Player(player_spites, p_pos)

    thread = threading.Thread(target=load)
    thread.Daemon = True
    thread.start()
    movement_thread = threading.Thread(target=movement)
    movement_thread.Daemon = True
    movement_thread.start()

def move(x, y):
    global move_x, move_y
    move_x = x
    move_y = y
    return

def movement():
    global threads_started, move_x, move_y, move_m, cur_chunks, momentum  # here we check if we have to move the screen
    on_ground = False
    while True:                  # while True so that we do this always
        if not threads_started:
            exit()
        if move_x == 0:     #TODO: We must check if the movement is legal
            if move_m[0] == 0:
                pass
            else:
                if move_m[0] < 0:
                    move_m[0] += momentum
                else:
                    move_m[0] -= momentum
        else:
            move_m[0] = 2 * move_x

        if move_y == 0:
            on_ground, move_m[1] = falling(move_m[1])

        elif move_y == 1 and on_ground:
            move_m[1] = -2                   # we ignore -1 for now because there is no negative jumping
            move_y = 0
            on_ground = False
        else:
            pass                            # we pass because we cant jump in the air maybe change later

        print(move_m)

        cur_chunks[0].move(move_m[0] / 100, move_m[1] / 100)
        cur_chunks[1].move(move_m[0] / 100, move_m[1] / 100)
        cur_chunks[2].move(move_m[0] / 100, move_m[1] / 100)
        cur_chunks[3].move(move_m[0] / 100, move_m[1] / 100)
        cur_chunks[4].move(move_m[0] / 100, move_m[1] / 100)
        time.sleep(0.001)


def falling(y_speed):
    global gravity
    final_pos = collide_ground(y_speed)
    print(final_pos)
    if not final_pos:
        on_ground = False
    else:
        on_ground = True
        y_speed = 0

    if not on_ground:
        if y_speed - gravity < -4.9:
            y_speed = -5
        else:
            y_speed -= gravity
    else:
        return True, 0

    return on_ground, y_speed

def collide_ground(y_speed):
    global player, cur_chunks, cur_chunk_pos
    # pot_position = player.pos
    # pot_position[1] += y_speed
    # final_pos= cur_chunks[2].ground_col(player, pot_position)             # if still falling final_pos is None
    final_pos = None
    final_pos = cur_chunks[2].col_g(player, cur_chunk_pos)

    return final_pos

def save():
    global chunks
    #print(chunks)
    saver.save_world([00, 12, 5,4], chunks)
    return

def load_chunk():



    return

