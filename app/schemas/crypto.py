from pydantic import RootModel
from typing import Dict, Any

class ValidJson(RootModel[Dict[str, Any]]):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "John Doe",
                    "age": 30,
                    "contact": {
                        "email": "john@example.com",
                        "phone": "123-456-7890"
                    }
                }
            ]
        }
    }
    
class EncryptedInput(RootModel[Dict[str, str]]):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "age": "MzA=",
                    "contact": "eyJlbWFpbCI6ICJqb2huQGV4YW1wbGUuY29tIiwgInBob25lIjogIjEyMy00NTYtNzg5MCJ9",
                    "name": "Sm9obiBEb2U="
                }
            ]
        }
    }

class EncryptOutput(RootModel[Dict[str, Any]]):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Sm9obiBEb2U=",
                    "age": "MzA=",
                    "contact": "eyJlbWFpbCI6ImpvaG5AZXhhbXBsZS5j..."
                }
            ]
        }
    }
    
class SigningOutput(RootModel[Dict[str, str]]):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "signature": "c2lnbmF0dXJlX3ZhbHVl"
                }
            ]
        }
    }
    
class VerifyInput(RootModel[Dict[str, Any]]):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "age": 30,
                    "contact": {
                        "email": "john@example.com",
                        "phone": "123-456-7890"
                    },
                    "name": "John Doe",
                    "signature": "fcfbfe1ea7042df3a6d18a1b52cd98436c6f81c29b42425d384cac366c2fae9c"
                }
            ]
        }
    }
