import math
import threading
from scripts import chunk

cur_chunks = []



def manage(root, cur_pos_x, chunks, chunk_width):
    global cur_chunks

    cur_chunks = []

    cur_chunk_pos = math.floor(cur_pos_x / chunk_width) # must be rounded down

    if math.floor(chunks[0].x / chunk_width) + 1 > cur_chunk_pos:
        x = chunks[0].x - chunk_width
        chunks[0].seed -= chunk_width
        n_sprites = [chunks[0].sprites, chunks[0].s_atlas]
        n_chunk = chunk.Chunk(x, chunks[0].y, chunk_width, chunks[0].seed, n_sprites, chunks[0].sprite_size)
        chunks.insert(0, n_chunk)

    if math.floor(chunks[-1].x / chunk_width) - 1 < cur_chunk_pos:
        x = chunks[-1].x + chunk_width
        chunks[-1].seed += chunk_width
        n_sprites = [chunks[0].sprites, chunks[0].s_atlas]
        n_chunk = chunk.Chunk(x, chunks[-1].y, chunk_width, chunks[-1].seed, n_sprites, chunks[-1].sprite_size)
        chunks.append(n_chunk)

    cur_chunks = [chunks[cur_chunk_pos - 1], chunks[cur_chunk_pos], chunks[cur_chunk_pos + 1]]


    for c in cur_chunks:
        root = c.draw(root)

    move(0, 0)

    return chunks, root


def move(move_x, move_y):
    global cur_chunks
    cur_chunks[1].move(move_x, move_y)

    cur_chunks[0].move(move_x, move_y)

    cur_chunks[-1].move(move_x, move_y)
    return



