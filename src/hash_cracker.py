import hashlib
import argparse
import time
from typing import Optional

def calculate_hash(word: str, hash_type: str) -> Optional[str]:
    """Calculate hash of a word using specified algorithm."""
    hash_func = {
        'md5': hashlib.md5,
        'sha1': hashlib.sha1,
        'sha256': hashlib.sha256,
        'sha512': hashlib.sha512,
        'sha3_256': hashlib.sha3_256,
        'blake2b': hashlib.blake2b
    }.get(hash_type.lower())
    
    if not hash_func:
        return None
    
    try:
        return hash_func(word.encode()).hexdigest()
    except Exception as e:
        print(f"[-] Error calculating hash: {e}")
        return None

def load_wordlist(wordlist_path: str) -> list:
    """Load wordlist from file."""
    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"[-] Wordlist file not found: {wordlist_path}")
        return []
    except Exception as e:
        print(f"[-] Error loading wordlist: {e}")
        return []

def crack_hash(target_hash: str, hash_type: str, wordlist: list, output_file: str = None) -> Optional[str]:
    """Attempt to crack the hash using provided wordlist."""
    start_time = time.time()
    attempts = 0
    found_password = None
    
    print(f"[*] Starting hash cracking for {hash_type.upper()} hash")
    print(f"[*] Target hash: {target_hash}")
    print(f"[*] Words to try: {len(wordlist):,}")
    
    for word in wordlist:
        attempts += 1
        digest = calculate_hash(word, hash_type)
        
        if not digest:
            continue
            
        if digest == target_hash.lower():
            found_password = word
            break
            
    elapsed = time.time() - start_time
    
    if output_file:
        with open(output_file, 'a') as f:
            f.write(f"\n{'='*50}\n")
            f.write(f"Hash Cracking Results - {time.ctime()}\n")
            f.write(f"Target Hash: {target_hash}\n")
            f.write(f"Hash Type: {hash_type.upper()}\n")
            f.write(f"Attempts: {attempts:,}\n")
            f.write(f"Time Elapsed: {elapsed:.2f} seconds\n")
            
            if found_password:
                f.write(f"[+] CRACKED! Password: {found_password}\n")
            else:
                f.write("[-] Password not found in wordlist\n")
    
    if found_password:
        print(f"\n[+] Hash cracked in {elapsed:.2f} seconds after {attempts:,} attempts!")
        print(f"[+] Password found: {found_password}")
    else:
        print(f"\n[-] Password not found after {attempts:,} attempts ({elapsed:.2f} seconds)")
    
    return found_password

def main():
    parser = argparse.ArgumentParser(description="Ethical Password Hash Cracker for Penetration Testing")
    parser.add_argument("hash", help="Target hash to crack")
    parser.add_argument("type", help="Hash algorithm (md5, sha1, sha256, sha512, etc.)")
    parser.add_argument("wordlist", help="Path to wordlist file")
    parser.add_argument("-o", "--output", help="Output file to save results", default="results.txt")
    args = parser.parse_args()
    
    wordlist = load_wordlist(args.wordlist)
    if not wordlist:
        return
    
    crack_hash(args.hash, args.type, wordlist, args.output)

if __name__ == "__main__":
    main()
