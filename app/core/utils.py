import base64
import hmac
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
private_key = os.getenv("PRIVATE_KEY")
private_key = private_key.encode('utf-8') if private_key else None

# If the environment variable is not set, default to a hardcoded value and print a warning
if private_key is None:
    private_key = b'default_private_key'
    print("\033[91m/!\\ WARNING: PRIVATE_KEY not set in .env file. Using default (unsafe) value. /!\\\033[0m")
    print("\033[91m/!\\     Please set the PRIVATE_KEY in your .env file for production use.     /!\\\033[0m")
    print("\033[91m/!\\     === THIS IS NOT SECURE AND SHOULD NOT BE USED IN PRODUCTION. ===     /!\\\033[0m")


# NOTE: Any changes to the encryption/decryption/signing/verification logic should be reflected in the API documentation and examples, as well as in docstrings in /api/v1/endpoints/crypto.py
def encode(data: str) -> str:
    """
    Encode a string using base64 encoding.
    """
    encoded_bytes = base64.b64encode(data.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

def decode(data: str) -> str:
    """
    Decode a base64 encoded string.
    """
    decoded_bytes = base64.b64decode(data.encode('utf-8'))
    return decoded_bytes.decode('utf-8')

def sign(data: str) -> str:
    """
    Sign a string using HMAC with SHA256.
    """
    return hmac.new(private_key, data.encode('utf-8'), 'sha256').hexdigest()

def verify(data: str, signature: str) -> bool:
    """
    Verify a string using HMAC with SHA256.
    """
    expected_signature = sign(data)
    return hmac.compare_digest(expected_signature, signature)