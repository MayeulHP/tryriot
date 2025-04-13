from fastapi import APIRouter
from typing import Any, Dict
from app.services.cryptoService import base64_encode, base64_decode

router = APIRouter()

@router.post("/encrypt")
def encrypt(payload: Dict[str, Any]) -> Dict[str, str]:
    try:
        encrypted = base64_encode(payload)
        return encrypted
    except Exception as e:
        return {"error": str(e)}
    
@router.post("/decrypt")
def decrypt(payload: Dict[str, str]) -> Dict[str, Any]:
    try:
        decrypted = base64_decode(payload)
        return decrypted
    except Exception as e:
        return {"error": str(e)}