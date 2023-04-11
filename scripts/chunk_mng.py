import math
from scripts import chunk

def manage(cur_pos_x, chunks, chunk_width): 

cur_chunk_pos = math.floor(cur_pos_x / chunk_width) # must be rounded down
If chunks[0].x > cur_chunk_pos:
    x = chunks[0].x - chunk_width
    n_sprites = [chunks[0].sprites, chunks[0].s_atlas]
    n_chunk = Chunk(x, chunks[0].y, chunk_width, chunks[0].seed, n_sprites, chunks[0].sprite_size)
    chunks.insert(0, n_chunk)
    cur_chunk_pos += 1
    
elif chunks[-1] < cur_chunk_pos:
    x = chunks[-1].x + chunk_width
    n_sprites = [chunks[0].sprites, chunks[0].s_atlas]
    n_chunk = Chunk(x, chunks[0].y, chunk_width, chunks[0].seed, n_sprites, chunks[0].sprite_size)
    chunks.append(n_chunk)


cur_chunks = [chunks[cur_chunk_pos - 1], chunks[cur_chunk_pos], chunks[cur_chunk_pos + 1]] 

return cur_chunks


