import math
import threading
import time
from scripts import chunk

cur_chunks = []
chunks = {}
cur_chunk_pos = 0
threads_started = False

def load():
    global cur_chunks, chunks, cur_chunk_pos, threads_started

    #print('cur_chunk_pos:' + str(cur_chunk_pos))
    chunk_width = chunks[0].width
    #print('chunk_pos: ' + str(math.floor(chunks[cur_chunk_pos].x / chunk_width)))

#    if math.floor(chunks[cur_chunk_pos].x / chunk_width) + 1 > cur_chunk_pos and cur_chunk_pos - 1 == -2:
#        x = chunks[0].x - chunk_width
#        n_sprites = [chunks[0].sprites, chunks[0].s_atlas]
#        n_chunk = chunk.Chunk(x, chunks[0].y, chunk_width, chunks[0].seed, n_sprites, chunks[0].sprite_size)
#        chunks.update({cur_chunk_pos - 1 : n_chunk})
#        print('load_right')
#
#    elif math.floor(chunks[cur_chunk_pos + 1].x / chunk_width) - 1 < cur_chunk_pos and cur_chunk_pos + 1 == 2:
#        x = chunks[-1].x + chunk_width
#        n_sprites = [chunks[0].sprites, chunks[0].s_atlas]
#        n_chunk = chunk.Chunk(x, chunks[-1].y, chunk_width, chunks[-1].seed, n_sprites, chunks[-1].sprite_size)
#        chunks.update({cur_chunk_pos + 1 : n_chunk})
#        print('load_left')
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

        try:
            chunks[cur_chunk_pos + 2]

        except KeyError:
            x = chunks[cur_chunk_pos].x + 2 * chunk_width
            n_sprites = [chunks[0].sprites, chunks[0].s_atlas]
            n_chunk = chunk.Chunk(x, chunks[cur_chunk_pos].y, chunk_width, chunks[-1].seed, n_sprites, chunks[-1].sprite_size)
            n_chunk.x = chunks[cur_chunk_pos].x + 2 * chunk_width
            chunks.update({cur_chunk_pos + 2 : n_chunk})
            print('load_left')

        try:
            cur_chunks = [chunks[cur_chunk_pos - 2], chunks[cur_chunk_pos - 1], chunks[cur_chunk_pos],
                          chunks[cur_chunk_pos + 1], chunks[cur_chunk_pos + 2]]
        except KeyError:
            print('KeyError')

        cur_chunks[0].x = cur_chunks[2].x - 2 * chunk_width
        cur_chunks[1].x = cur_chunks[2].x - chunk_width
        cur_chunks[3].x = cur_chunks[2].x + chunk_width
        cur_chunks[4].x = cur_chunks[2].x + 2 * chunk_width

        time.sleep(0.01)


def manage(root, cur_pos_x, chunk_width):
    global cur_chunks, chunks, cur_chunk_pos, threads_started

    cur_chunk_pos = math.floor(cur_pos_x / chunk_width) # must be rounded down
    #print(cur_chunk_pos)

    try:
        chunks[cur_chunk_pos + 1].y = chunks[cur_chunk_pos].y
        chunks[cur_chunk_pos - 1].y = chunks[cur_chunk_pos].y
        chunks[cur_chunk_pos + 2].y = chunks[cur_chunk_pos].y
        chunks[cur_chunk_pos - 2].y = chunks[cur_chunk_pos].y
    except IndexError:
        print('IndexError')
    except KeyError:
        print('KeyError')

    for c in cur_chunks:
        root = c.draw(root)

    return chunks, root

def m_init(s_chunk):
    global chunks, threads_started, cur_chunks
    chunks = s_chunk
    threads_started = True
    cur_chunks = [chunks[cur_chunk_pos - 1], chunks[cur_chunk_pos], chunks[cur_chunk_pos + 1]]
    thread = threading.Thread(target=load)
    thread.Daemon = True
    thread.start()

def move(move_x, move_y):
    global cur_chunks
    cur_chunks[0].move(move_x, move_y)
    cur_chunks[1].move(move_x,move_y)
    cur_chunks[2].move(move_x, move_y)
    cur_chunks[3].move(move_x, move_y)
    cur_chunks[4].move(move_x, move_y)
    return



