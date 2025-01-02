import secrets
import string

def generate_key(length:int=64)-> str:
    """
    Generates a cryptographically secure random key.
    Default length is 64 characters unless otherwise defined.
    :param length: Default key character length.
    :return: a 64 string character long encrypted key.
    """

    # define the characters to choose from (uppercase, lowercase, digits, punctuation)
    alphabet= string.ascii_letters + string.digits + string.punctuation

    # generate a random key with the specified length from the defined character options given
    key= ''.join(secrets.choice(alphabet)
                 for _ in range(length))

    return key

new_key= generate_key(64)

print(f"GENERATED KEY:{new_key}")