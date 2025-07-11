import secrets
import string

def generate_short_code(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))

# Example usage
short_code = generate_short_code()
print(short_code)
