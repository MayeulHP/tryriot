import base64
from typing import Any, Dict
import json

def base64_encode(obj: Dict[str, Any]) -> Dict[str, str]:
    """
    Encrypts a JSON object, by encrypting all properties at depth 1.
    """
    try:
        
        for key, value in obj.items():
            if isinstance(value, dict):
                json_str = json.dumps(value, indent=None, sort_keys=True)
                obj[key] = base64.b64encode(json_str.encode()).decode()
            else:
                obj[key] = base64.b64encode(str(value).encode()).decode()
        return obj
    except Exception as e:
        raise ValueError(f"Encryption failed: {str(e)}")
    
def base64_decode(obj: Dict[str, str]) -> Dict[str, Any]:
    """
    Decrypts a JSON object, by decrypting all properties at depth 1.
    """
    try:
        for key, value in obj.items():
            decoded_value = base64.b64decode(value).decode()
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