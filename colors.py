#Color Codes:
#
#    Foreground Colors:
#        30: Black
#        31: Red
#        32: Green
#        33: Yellow
#        34: Blue
#        35: Magenta
#        36: Cyan
#        37: White
#    Background Colors:
#        40: Black
#        41: Red
#        42: Green
#        43: Yellow
#        44: Blue
#        45: Magenta
#        46: Cyan
#        47: White
# Exemple : "\033[41;97m Hello, World! \033[0m"
# \033[41;97m : Red background with white text (refer to above color codes)
# \033[0m : Reset the color

print("\033[40;47mHello, World!\033[0m");exit()

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
PURPLE = '\033[35m'
CYAN = '\033[36m'
GOLD = '\033[38;5;214m'
WHITE = '\033[37m'
BLACK = '\033[30m'
ORANGE = '\033[38;5;208m'
CRIMSON = '\033[38;5;196m'
RESET = '\033[0m'
BOLD = '\033[1m'

MAGNIFYING_GLASS = '\U0001F50D'
SKULL   =    '\u2620\ufe0f'

colors = [RED,GREEN,YELLOW,BLUE,PURPLE,CYAN,WHITE,ORANGE,CRIMSON]

UNDERLINE = '\033[4m'
OBFUSCATE = '\033[3m'
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