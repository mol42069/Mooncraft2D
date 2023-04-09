
def manage(cur_pos_x, chunks, chunk_width): 

cur_chunk_pos = cur_pos_x / chunk_width # must be rounded up
If chunks[0].x > cur_chunk_pos:
    #gen chunks to the left
elif chunks[-1] < cur_chunk_pos:
    #gen chunks to the right 


cur_chunks = [chunks[cur_chunk_pos - 1], chunks[cur_chunk_pos], chunks[cur_chunk_pos + 1]] 

return cur_chunks


