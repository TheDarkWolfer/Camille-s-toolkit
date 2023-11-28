import time
import os
import subprocess

def obliterate(file_path, passes=3):
    # Open the file in binary mode
    with open(file_path, 'rb+') as file:
        file_size = os.path.getsize(file_path)
        
        for _ in range(passes):
            # Overwrite the file with random data
            file.seek(0)
            file.write(os.urandom(file_size))
            file.flush()
            os.fsync(file.fileno())
        
        # Delete and truncate the file
        os.unlink(file_path)
        with open(file_path, 'wb'):
            pass

def progressBar(text:str,delay:float):

    RESET   =    '\033[0m'
    CYAN    =    '\033[96m'

    """
    Progress bar function, makes the program prettier ^.^
    I know it's useless in this case, but it's still pretty !
    """
    for i in range(25):
        print(f"|{text}|{CYAN}{i*4}{RESET}%|[{'#' * i}{'_' * (25 - (i+1))}]", end="\r")
        time.sleep(delay)

#define colors as such : COLOR = '\033[COLORm'
#where COLOR is the color you want
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
PURPLE = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
BLINK = '\033[5m'
INVERT = '\033[7m'
HIDE = '\033[8m'
STRIKETHROUGH = '\033[9m'
DEFAULT_FONT = '\033[10m'
FONT1 = '\033[11m'
FONT2 = '\033[12m'
FONT3 = '\033[13m'
FONT4 = '\033[14m'
FONT5 = '\033[15m'
MAGNIFYING_GLASS = '\U0001F50D'
SKULL = '\U0001F480'

while True:
    exit()
exit()
#this is to make sure you don't accidentally execute this script


progressBar(text=f"[{RED}{BOLD}{SKULL}{RESET}] Deleting all traces... Bye bye ! [{RED}{BOLD}{SKULL}{RESET}]", delay=0.1)
subprocess.call("sudo sync && sudo sysctl -w vm.drop_caches=3") #Clear the ram
with open("/proc/sys/vm/drop_caches", "w") as f:
    f.write("3\n") #clear the swap
progressBar(text=f"[{RED}{SKULL}{RESET}] Shredding the file", delay=0.1)
obliterate(os.path.basename(__file__),50)                       #Delete the file securely (see the function above)
try:
    subprocess.call(f"shred -n 50 -z -u {os.path.basename(__file__)}") #Shred the file
except:
    pass
subprocess.run(['shutdown', '-h', 'now'])                       #Shut the computer down instantly