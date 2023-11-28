import bcrypt, random, string

def compare_password_hash(password, hashed_password):
    """
    Compare a user-inputted password with a stored hashed password securely.
    """
    password = password.encode('utf-8')  # Encode the user-inputted password as bytes
    hashed_password = hashed_password.encode('utf-8')  # Encode the stored hashed password as bytes
    
    # Use bcrypt's secure hash comparison function
    return bcrypt.checkpw(password, hashed_password)

def hash_password(password):
    """
    Hash a password securely.
    """
    password = password.encode('utf-8')  # Encode the password as bytes
    
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password, salt)
    
    # Return the hashed password as a string
    return hashed_password.decode('utf-8')


print(f"Hashed password: {hash_password(input('Enter a password to hash: '))}")


if True:
    exit()


numbers = [i+1 for i in range(72)]

with open("hashes.txt","w") as h:
    for i in range(72):
        content = hash_password("".join(random.choice(string.ascii_letters) for i in range(10)))
        print_content = f'Hash n°{i+1} : {content}\n'
        score = random.choice(numbers)
        print("Remaining numbers : "+str(numbers)+"\n")
        numbers.remove(score)
        h.write(f"{score}:"+"'"+content+"',\n")
        print(print_content)
    h.close()
