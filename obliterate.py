import os
from multiprocessing import Pool

def overwrite_chunk(args):
    file_path, chunk_start, chunk_end = args
    chunk_size = chunk_end - chunk_start

    with open(file_path, 'rb+') as file:
        file.seek(chunk_start)
        chunk_data = os.urandom(chunk_size)
        file.write(chunk_data)
        file.flush()
        os.fsync(file.fileno())

def obliterate(file_path, passes=3):
    file_size = os.path.getsize(file_path)
    chunk_size = file_size // passes

    with Pool() as pool:
        for _ in range(passes):
            chunk_start = _ * chunk_size
            chunk_end = chunk_start + chunk_size

            pool.map(overwrite_chunk, [(file_path, chunk_start, chunk_end)])

    os.unlink(file_path)
    with open(file_path, 'wb'):
        pass