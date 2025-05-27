# Advanced Usage

## Basic Cracking
```bash
python src/hash_cracker.py 5f4dcc3b5aa765d61d8327deb882cf99 md5 wordlists/common.txt
```

## Saving Results
```bash
python src/hash_cracker.py <hash> <type> wordlists/common.txt -o results.txt
```

## Supported Algorithms
- MD5
- SHA1
- SHA256
- SHA512
- SHA3-256
- BLAKE2b
