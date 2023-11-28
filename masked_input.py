import termios, sys, tty

def masked_input(prompt="Enter your password: "):
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
                print(f"*", end="", flush=True)  # Print an asterisk instead of the actual character
    finally:
        # Restore terminal settings
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

    return password

print(masked_input())