# import noise
from scripts import enums
from perlin_noise import PerlinNoise
import matplotlib.pyplot as plt

def gen(chunk_pos, chunk_width, chunk_height = 256, seed=9999999):
    chunk = []
    max_x = 128
    seed += chunk_pos * chunk_width

    for y in range(chunk_height):
        chunk_x = []
        for x in range(chunk_width):
            chunk_x.append(enums.Block.air)

        chunk.append(chunk_x)

    height_map = []
    noise = PerlinNoise(octaves=10, seed=seed)
    for x in range(0, chunk_width):
        height = noise((x + chunk_width * chunk_pos) / max_x) * 15 + 100
        height_map.append(int(height) + 100)
    for y in range(chunk_height):
        for x in range(chunk_width):
            if height_map[x] == y:
                chunk[y][x] = enums.Block.grass

                for z in range(chunk_height):
                    if z > y:
                        chunk[z][x] = enums.Block.stone
    return chunk

