from fastapi import APIRouter, HTTPException, Response
from typing import Any, Dict
from app.services.cryptoService import encode_obj, decode_obj, sign_obj, verify_obj
from app.schemas.crypto import ValidJson, EncryptedInput, EncryptOutput, SigningOutput, VerifyInput

router = APIRouter()

@router.post(
    "/encrypt",
    response_model=EncryptOutput,
    summary="Encrypt JSON object",
    description="Encrypts all first-level properties of a JSON object using Base64 encoding."
)
def encrypt(payload: ValidJson):
    try:
        encrypted = encode_obj(payload.root)
        return EncryptOutput(encrypted)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post(
    "/decrypt",
    response_model=ValidJson,
    summary="Decrypt JSON object",
    description="Decrypts all first-level properties of a JSON object using Base64 decoding."
)
def decrypt(payload: EncryptedInput) -> Dict[str, Any]:
    try:
        decrypted = decode_obj(payload.root)
        return decrypted
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Decrypting failed: {str(e)}")
    
@router.post(
    "/sign",
    response_model=SigningOutput,
    summary="Sign JSON object",
    description="Signs a JSON object using HMAC with SHA256."
)
def sign(payload: ValidJson) -> Dict[str, Any]:
    try:
        signature = sign_obj(payload.root)
        return SigningOutput(signature=signature)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Signing failed: {str(e)}")
    
@router.post(
    "/verify",
    summary="Verify JSON object signature",
    description="Verifies a JSON object's signature using HMAC with SHA256."
)
def verify(payload: VerifyInput) -> Dict[str, Any]:
    try:
        signature = payload.root.pop("signature")
        is_valid = verify_obj(payload.root, signature)
        if is_valid:
            return Response(status_code=204)
        else:
            raise HTTPException(status_code=400, detail="Signature is invalid")
    except HTTPException:
        raise  # Keep the HTTPException as is
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Verification failed: {str(e)}")
