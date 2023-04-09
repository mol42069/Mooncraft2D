import csv

def save_world(data, chunks, path):
    csv_data = [data]
    for chunk in chunks:
        csv_data = chunk.save_chunk(csv_data, 1)

    save(csv_data, path)

def load(path):
    with open(path, 'r', newline='\n', encoding='utf-8') as file:
        csv_reader = csv.reader(file, delimiter=':')
        data = csv_reader
    return data

def save(data, path):               # path must include filename!

    with open(path, 'w', newline='\n', encoding='utf-8') as file:
        csv_writer = csv.writer(file, delimiter=':')
        csv_writer.writerows(data)

    return

