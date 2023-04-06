import noise
from scripts import enums

def gen(chunk_pos, chunk_width, amplifier=15, noise_gen_val = 0.50000, chunk_height = 256):
    chunk = []

    for y in range(chunk_height):
        chunk_x = []
        for x in range(chunk_width):
            chunk_x.append(enums.Block.air)

        chunk.append(chunk_x)

    height_map = []
    for x in range(0, chunk_width):
        height = noise.pnoise1(((x + chunk_width * chunk_pos) * noise_gen_val / (256 -  x * noise_gen_val)), repeat = 9999999) * amplifier
        height_map.append(int(height) + 100)
    for y in range(chunk_height):
        for x in range(chunk_width):
            if height_map[x] == y:
                chunk[y][x] = enums.Block.grass

                for z in range(chunk_height):
                    if z > y:
                        chunk[z][x] = enums.Block.stone
    return chunk

