import re
import random

def uwuify(text, face_probability=0.5):
    # Replace certain characters to add cuteness
    text = text.replace('r', 'w').replace('l', 'w')
    
    # Add 'uwu' faces with specified probability
    uwu_faces = ['(・`ω´・)', 'UwU', '(ฅ\'ω\'ฅ)', 'owo', '(*^ω^)', '(つ✧ω✧)つ']
    text = re.sub(r'\b\w+\b', lambda x: random.choice(uwu_faces) + ' ' + x.group(0), text)
    
    # Add 'nyaa~' or 'mew~' randomly for fun
    if random.random() < face_probability:
        text += ' nyaa~'
    else:
        text += ' mew~'
    
    return text

if __name__ == "__main__":
    input_text = input("Enter text to uwuify: ")
    probability = float(input("Enter probability of uwu face (0.0 to 1.0): "))
    uwu_text = uwuify(input_text, face_probability=probability)
    print(uwu_text)
