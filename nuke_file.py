import os
import random
from multiprocessing import Pool

def overwrite_chunk(args):
    file_path, chunk_start, chunk_end = args
    chunk_size = chunk_end - chunk_start

    # Initialize data with random values
    random_data = os.urandom(chunk_size)

    with open(file_path, 'rb+') as file:
        file.seek(chunk_start)
        file.write(random_data)
        file.flush()
        os.fsync(file.fileno())

def obliterate(file_path, passes=3):
    file_size = os.path.getsize(file_path)
    chunk_size = file_size // passes

    # Random passes to overwrite the data
    with Pool() as pool:
        for _ in range(passes):
            chunk_start = _ * chunk_size
            chunk_end = chunk_start + chunk_size

            pool.map(overwrite_chunk, [(file_path, chunk_start, chunk_end)])

    # Apply the "Clear" method pattern (alternating 0s and 1s)
    clear_pattern = b'\x00\xFF' * (chunk_size // 2)

    # Final single pass with the "Clear" method pattern
    with open(file_path, 'rb+') as file:
        for _ in range(file_size // chunk_size):
            chunk_start = _ * chunk_size
            file.seek(chunk_start)
            file.write(clear_pattern)
            file.flush()
            os.fsync(file.fileno())

    os.unlink(file_path)
    with open(file_path, 'wb'):
        pass
