import hashlib

HASH_FILE = "../tools/sample_hash.txt"
WORDLIST_FILE = "../tools/wordlist.txt"
OUTPUT_FILE = "../results/cracked_password.txt"

def load_hash():
    with open(HASH_FILE, "r") as f:
        return f.readline().strip()

def dictionary_attack(target_hash):
    with open(WORDLIST_FILE, "r", encoding="latin-1") as wordlist:
        for word in wordlist:
            password = word.strip()
            hashed = hashlib.md5(password.encode()).hexdigest()
            if hashed == target_hash:
                return password
    return None

def main():
    print("🔍 Loading target hash...")
    target_hash = load_hash()

    print("🚀 Starting dictionary attack...")
    result = dictionary_attack(target_hash)

    if result:
        print(f"🎉 Password cracked: {result}")
        with open(OUTPUT_FILE, "w") as f:
            f.write(f"Cracked password: {result}\n")
    else:
        print("❌ Password not found. Try a bigger wordlist.")

if __name__ == "__main__":
    main()
