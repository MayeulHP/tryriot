from app.core.utils import encode, decode, sign, verify # For abstraction
from typing import Any, Dict
import json

def encode_obj(obj: Dict[str, Any]) -> Dict[str, str]:
    """
    Encrypts a JSON object, by encrypting all properties at depth 1.
    """
    try:
        
        for key, value in obj.items():
            if isinstance(value, dict):
                json_str = json.dumps(value, indent=None, sort_keys=True)
                obj[key] = encode(json_str)
            else:
                obj[key] = encode(str(value))
        return obj
    except Exception as e:
        raise ValueError(f"Encryption failed: {str(e)}")
    
def decode_obj(obj: Dict[str, str]) -> Dict[str, Any]:
    """
    Decrypts a JSON object, by decrypting all properties at depth 1.
    """
    try:
        for key, value in obj.items():
            decoded_value = decode(value)
            if decoded_value.startswith('{') and decoded_value.endswith('}'):
                try:
                    obj[key] = json.loads(decoded_value)
                except json.JSONDecodeError:
                    obj[key] = decoded_value
            else:
                obj[key] = decoded_value
        return obj
    except Exception as e:
        raise ValueError(f"Decryption failed: {str(e)}")
    
def sign_obj(obj: Dict[str, Any]) -> str:
    """
    Signs a JSON object with the server's secret key.
    """
    try:
        json_str = json.dumps(obj, indent=None, sort_keys=True)
        return sign(json_str)
    except Exception as e:
        raise ValueError(f"Signing failed: {str(e)}")
    
def verify_obj(obj: Dict[str, Any], signature: str) -> bool:
    """
    Verifies a JSON object's signature with the server's secret key.
    """
    try:
        json_str = json.dumps(obj, indent=None, sort_keys=True)
        return verify(json_str, signature)
    except Exception as e:
        raise ValueError(f"Verification failed: {str(e)}")
    