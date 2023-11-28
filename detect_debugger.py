import sys
import platform
import ctypes
import os

def isDebugger():
    if platform.system() == "Darwin" and "lldb" in platform.uname().release:
        return True
    if platform.system() == "Windows" and "DBG" in platform.uname().release:
        return True
    if platform.system() == "Linux" and "gdb" in platform.uname().release:
        return True
    
    if platform.system() == "Windows":
        libc = ctypes.CDLL(None)
        libc.ptrace(31, 0, 0, 0)

        if ctypes.get_errnoa() != 0:
            return True
    
    if sys.gettrace() != None:
        return True
    
    return False