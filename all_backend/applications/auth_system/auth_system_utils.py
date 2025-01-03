from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, HashingError
from dotenv import load_dotenv
import datetime
import os
import jwt
import logging


logger= logging.getLogger('django')


# PASSWORD HASHING #

_hasher= PasswordHasher(
    time_cost=3, # Number of iterations (higher=slower)
    memory_cost=64*1034, # Memory allocation for hashing, in kibibytes (64 MB)
    parallelism=4, # Number of parallel threads
    hash_len=32, # Length of generated hash
    salt_len=16, # length of random salt
)

def hash_password(password:str)->str:
    """
    Hashes a string using custom Argon2 configuration.
    :param password: string of letters, numbers, signs or a possible mix of them.
    :return: A string containing generated hash.
    :raises: HashingError if hashing fails.
    """

    try:
        return _hasher.hash(password)
    except HashingError as hash_error:
        logger.error(f'Error hashing password: {hash_error}')
        raise


def verify_password(password:str, hashed:str)->bool:
    """
    Verifies a password string against a hash using custom Argon2 configuration.
    :param password: A string containing user given password.
    :param hashed: The hash to be validated against.
    :returns: True if password matches hash | False if there is a mismatch.
    :raises: VerifyMismatchError if password does not match hash.
    """

    try:
        return _hasher.verify(hashed, password)
    except VerifyMismatchError:
        logger.warning('Password verification failed!')
        return False
    except Exception as exc:
        logger.error(f'Error verifying password: {exc}')
        raise


# TOKEN/SESSION MANAGEMENT #

load_dotenv()

# Secret Key for signing tokens
JWT_SECRET= os.getenv('JWT_SECRET_KEY')
JWT_ALGORITHM= 'HS256'
JWT_EXP_DELTA_SECONDS= 3600 # Token validity=1h

def generate_token(user_id=int)-> str:
    """
    Generates a JWT token for a user.
    :param user_id: An integer identifier of the user.
    :return: The generated token.
    :raises:
    """

    try:
        payload={
            'user_id': user_id,
            'exp': datetime.datetime.now() + datetime.timedelta(seconds=JWT_EXP_DELTA_SECONDS),
        }
        token= jwt.encode(payload, JWT_SECRET, algorithm= JWT_ALGORITHM)
        return token
    except Exception as exc:
        logger.error(f'Error generating token: {exc}')
        raise

def decode_token(token:str)-> str:
    """
    Decodes and validates a JWT token.
    :param token: The string to decode.
    :return: The decoded payload if valid.
    :raises:
        jwt.ExpiredSignatureError: if  the token has expired.
        jwt.InvalidTokenError: if the token is invalid.
    """

    try:
        payload= jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        logger.warning(f'Token has expired. Token: {token}')
        raise
    except jwt.InvalidTokenError:
        logger.warning(f'Error: invalid token! Token: {token}')
        raise