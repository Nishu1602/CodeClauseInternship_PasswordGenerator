import random
import string

def generate_password(length, use_numbers=True, use_symbols=True):
    characters = string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the length of the password: "))
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    
    password = generate_password(length, use_numbers, use_symbols)
    print("Generated Password:", password)

if __name__== "__main__":
    main()