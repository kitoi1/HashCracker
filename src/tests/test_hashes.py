import pytest
from hash_cracker import calculate_hash

def test_md5_hashing():
    assert calculate_hash("test", "md5") == "098f6bcd4621d373cade4e832627b4f6"

def test_sha256_hashing():
    assert calculate_hash("test", "sha256") == "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
