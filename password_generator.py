import secrets
import string

def generate_password(
    length=16,
    use_uppercase=True,
    use_digits=True,
    use_symbols=True
):
    """Generate a cryptographically secure password."""
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be enabled.")

    return ''.join(secrets.choice(characters) for _ in range(length))


if __name__ == "__main__":
    print("Your secure password:", generate_password(length=20))
