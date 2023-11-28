import time

def progressBar(text:str,delay:float):

    RESET   =    '\033[0m'
    RED = '\033[31m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    """
    Progress bar function, makes the program prettier ^.^
    I know it's useless in this case, but it's still pretty !
    """
    for i in range(25):
        print(f"{text}|{CYAN}{i*4}{RESET}%|[{f'{RED}-{RESET}' * i}{f'{WHITE}-{RESET}' * (25 - (i+1))}]", end="\r")
        time.sleep(delay)