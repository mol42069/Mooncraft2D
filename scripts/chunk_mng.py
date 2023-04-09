
def manage(cur_pos_x, chunks):
    for chunk in chunks:
        if chunk.x > 1800 or chunk.x < -1800:
            chunk.loaded = False
        else:
            chunk.loaded = True
