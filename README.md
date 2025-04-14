# 🔐 Riot's super safe encryption API

A simple FastAPI-based API for encrypting, decrypting, signing, and verifying JSON payloads.

## 🧰 Features

- `/api/v1/crypto/encrypt`: Base64-encodes all top-level fields in a JSON object
- `/api/v1/crypto/decrypt`: Decodes previously encrypted fields
- `/api/v1/crypto/sign`: Signs a JSON object using the server's private key
- `/api/v1/crypto/verify`: Verifies a signature against the original payload

## 🚀 Quickstart

### Clone the repo

```bash
git clone git@github.com:MayeulHP/tryriot.git
cd tryriot
```

### Create and store the private key

```bash
echo "PRIVATE_KEY=your_private_key" > .env
```

> Make sure to replace `your_private_key` with your actual private key. You can generate a private key using the following command on Linux or MacOS:
```bash
openssl rand -hex 32
```
> This will generate a random 32-byte hexadecimal string that you can use as your private key. If no private key is provided, the server will use an unsafe default key and issue a warning.

## Run

### With uvicorn

```sh
pip install -r requirements.txt
uvicorn app.main:app --reload
```

or

### With Docker
    
```sh
docker build -t crypto-api .
docker run -p 8000:8000 crypto-api
```

### Access the Swagger at [http://localhost:8000/docs](http://localhost:8000/docs)

## 🧪 Testing

```sh
pip install -r requirements-test.txt
pytest
```

## 📬 API Usage

### Encrypting and Decrypting JSON Payloads

### POST /api/v1/crypto/encrypt

Request:
```json
{
  "name": "John",
  "age": 42
}
```

Response:

```json
{
  "name": "Sm9obiBEb2U=",
  "age": "NDI="
}
```

### POST /api/v1/crypto/decrypt

Request:
```json
{
  "name": "Sm9obiBEb2U=",
  "age": "NDI="
}
```

Response:
```json
{
  "name": "John",
  "age": 42
}
```

### Signing and Verifying JSON Payloads

### POST /api/v1/crypto/sign
Request:
```json
{
  "name": "John",
  "age": 42
}
```

Response:
```json
{
  "signature": "279fdcaac2f087f1ec82d8026b423e8320eb90265c81daba265b02e67c009fc5"
}
```

### POST /api/v1/crypto/verify

Request:
```json
{
  "age": 30,
  "contact": {
    "email": "john@example.com",
    "phone": "123-456-7890"
  },
  "name": "John Doe",
  "signature": "279fdcaac2f087f1ec82d8026b423e8320eb90265c81daba265b02e67c009fc5"
}
```

Responses:
- Code 204 (No Content): Signature is valid
- Code 400 (Bad Request): Signature is invalid