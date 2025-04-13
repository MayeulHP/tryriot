from fastapi import APIRouter, HTTPException
from typing import Any, Dict
from app.services.cryptoService import encode_obj, decode_obj, sign_obj, verify_obj

router = APIRouter()

@router.post("/encrypt")
def encrypt(payload: Dict[str, Any]) -> Dict[str, str]:
    try:
        encrypted = encode_obj(payload)
        return encrypted
    except Exception as e:
        return {"error": str(e)}
    
@router.post("/decrypt")
def decrypt(payload: Dict[str, str]) -> Dict[str, Any]:
    try:
        decrypted = decode_obj(payload)
        return decrypted
    except Exception as e:
        return {"error": str(e)}
    
@router.post("/sign")
def sign(payload: Dict[str, Any]) -> Dict[str, str]:
    try:
        signature = sign_obj(payload)
        return {"signature": signature}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Signing failed: {str(e)}")
    
@router.post("/verify")
def verify(payload: Dict[str, Any]) -> Dict[str, Any]:
    try:
        signature = payload.pop("signature")
        is_valid = verify_obj(payload, signature)
        if is_valid:
            raise HTTPException(status_code=204)
        else:
            raise HTTPException(status_code=400, detail="Signature is invalid")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Verification failed: {str(e)}")