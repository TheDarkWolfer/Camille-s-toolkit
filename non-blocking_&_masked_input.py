import sys
import asyncio
import tty
import termios

async def read_input():
    loop = asyncio.get_event_loop()
    char = await loop.run_in_executor(None, sys.stdin.read, 1)
    return char

async def masked_input(prompt="Enter your password: "):
    if "linux" in sys.platform:
        password = ""
        print(prompt, end="", flush=True)

        # Disable terminal echo (hide user input)
        old_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())

        try:
            while True:
                char = await read_input()

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
        raise NotImplementedError("Non-Linux platforms are not supported")

# Example usage:
async def main():
    entered_password = await masked_input("Enter your password: ")
    print("Entered password:", entered_password)

while True:
    print(f"Entered password: {asyncio.run(read_input())}")