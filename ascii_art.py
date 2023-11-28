import pyfiglet

def generate_ascii_art(text):
    """Ooh, pretty !"""
    ascii_art = pyfiglet.figlet_format(str(text))
    return ascii_art