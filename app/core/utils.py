import base64
import hmac

# Secret key for HMAC signing
secret_key = b'very_secret_key'  # Should be taken from a .env file or secure storage in production

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
    return hmac.new(secret_key, data.encode('utf-8'), 'sha256').hexdigest()

def verify(data: str, signature: str) -> bool:
    """
    Verify a string using HMAC with SHA256.
    """
    expected_signature = sign(data)
    return hmac.compare_digest(expected_signature, signature)