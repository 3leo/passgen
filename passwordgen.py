import random
import string

def generate_password(length, use_upper, use_lower, use_numbers, use_symbols):
    """
    Generates a random password based on user specifications.
    
    Args:
    length (int): Length of the password.
    use_upper (bool): Include uppercase letters if True.
    use_lower (bool): Include lowercase letters if True.
    use_numbers (bool): Include numbers if True.
    use_symbols (bool): Include symbols if True.
    
    Returns:
    str: The generated password.
    """
    
 
 # Start with an empty list of characters to choose from
    characters = ""
    
    # Add uppercase letters to our character list if required
    if use_upper:
        characters += string.ascii_uppercase
    
    # Add lowercase letters to our character list if required
    if use_lower:
        characters += string.ascii_lowercase
    
    # Add digits to our character list if required
    if use_numbers:
        characters += string.digits
    
    # Add symbols to our character list if required
    if use_symbols:
        characters += string.punctuation

    # Check if no character type was selected and raise an error
    if not characters:
        raise ValueError("At least one character type must be selected for the password.")

    # Randomly choose characters from the list 'characters' until we reach the desired 'length'
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main part of the script where we ask the user for their preferences
if __name__ == "__main__":
    # Ask the user how long they want the password to be
    length = int(input("Enter the desired password length: "))
    
    # Ask the user about including different types of characters
    use_upper = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_lower = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

    # Try generating the password, and handle any errors that might occur
    try:
        new_password = generate_password(length, use_upper, use_lower, use_numbers, use_symbols)
        print("Generated Password:", new_password)
    except ValueError as e:
        print(e)

