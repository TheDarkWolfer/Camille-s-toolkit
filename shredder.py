import os

def shred(file_path: str,passes=10):
    """
    Shred a file using the DoD 5220.22-M method.
    Required libraries: os
    """

    RED = '\033[91m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

    file_size = os.path.getsize(file_path)
    pass_size = file_size // passes

    with open(file_path, 'rb+') as file:
        for i in range(passes):
            file.seek(i * pass_size)
            file.write(b'\x00' * pass_size)

    print("["+RED+"+"+RESET+"]"+" Shredded file: " + BLUE + file_path)