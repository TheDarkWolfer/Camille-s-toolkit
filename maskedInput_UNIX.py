import sys, tty, termios, msvcrt

def masked_input(prompt="Enter your password: "):
    if "linux" in sys.platform:
        password = ""
        print(prompt, end="", flush=True)

        # Disable terminal echo (hide user input)
        old_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())

        try:
            while True:
                char = sys.stdin.read(1)

                # Stop input on newline (ASCII value: 10)
                if ord(char) == 10:
                    print()
                    break

                # Backspace (ASCII value: 127)
                elif ord(char) == 127:
                    if len(password) > 0:
                        password = password[:-1]
                        print("\b \b", end="", flush=True)  # Erase the last character from the screen
                else:
                    password += char
                    print("*", end="", flush=True)  # Print an asterisk instead of the actual character
        finally:
            # Restore terminal settings
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

        return password
    else:
        password = ""
        print(prompt, end="", flush=True)

        while True:
            char = msvcrt.getch().decode('utf-8')

            # Stop input on Enter key (ASCII value: 13)
            if ord(char) == 13:
                print()
                break

            # Backspace (ASCII value: 8)
            elif ord(char) == 8:
                if len(password) > 0:
                    password = password[:-1]
                    print("\b \b", end="", flush=True)  # Erase the last character from the screen
            else:
                password += char
                print("*", end="", flush=True)  # Print an asterisk instead of the actual character

        return password

import msvcrt  # For Windows-specific console input
import getpass

def masked_input(prompt="Enter your password: "):
    password = ""
    print(prompt, end="", flush=True)

    while True:
        char = msvcrt.getch().decode('utf-8')

        # Stop input on Enter key (ASCII value: 13)
        if ord(char) == 13:
            print()
            break

        # Backspace (ASCII value: 8)
        elif ord(char) == 8:
            if len(password) > 0:
                password = password[:-1]
                print("\b \b", end="", flush=True)  # Erase the last character from the screen
        else:
            password += char
            print("*", end="", flush=True)  # Print an asterisk instead of the actual character

    return password

# Example usage:
# entered_password = masked_input("Enter your password: ")
