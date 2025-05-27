# Test Data Documentation

## Purpose
This directory contains sample hashes for testing the cracker's functionality.

## Sample Hashes Table
| Algorithm | Plaintext  | Hash |
|-----------|------------|------|
| MD5       | "hello"    | `5d41402abc4b2a76b9719d911017c592` |
| SHA1      | "password" | `5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8` |
| SHA256    | "admin123" | `240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9` |
| SHA512    | "test123"  | `ecd71870d1963316a97e3ac3408c9835ad8cf0f3c1bc703527c30265534f75ae` |

## Usage in Tests
These hashes are used by:
- `test_hashes.py` for unit testing
- Integration tests
- CI/CD pipeline verification

## Security Notice
These are intentionally weak hashes of common passwords, only for testing the tool's functionality. Never use these passwords in real systems.

## Regenerating Test Hashes
To create new test hashes:

```bash
echo -n "plaintext" | openssl dgst -sha256
