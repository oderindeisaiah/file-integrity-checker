import hashlib
import os
from datetime import datetime

HASH_DB = "hashes.db"
LOG_FILE = "integrity.log"


def compute_hash(file_path: str) -> str:
    """Compute SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def load_hashes() -> dict:
    """Load stored file hashes."""
    hashes = {}
    if os.path.exists(HASH_DB):
        with open(HASH_DB, "r") as file:
            for line in file:
                path, hash_value = line.strip().split("|")
                hashes[path] = hash_value
    return hashes


def save_hashes(hashes: dict):
    """Save file hashes to disk."""
    with open(HASH_DB, "w") as file:
        for path, hash_value in hashes.items():
            file.write(f"{path}|{hash_value}\n")


def log_event(message: str):
    """Log integrity events."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as log:
        log.write(f"[{timestamp}] {message}\n")


def main():
    hashes = load_hashes()

    print("=== File Integrity Checker ===")
    file_path = input("Enter file path to monitor: ").strip()

    if not os.path.exists(file_path):
        print("File does not exist.")
        return

    current_hash = compute_hash(file_path)

    if file_path not in hashes:
        hashes[file_path] = current_hash
        save_hashes(hashes)
        log_event(f"Tracking started for {file_path}")
        print("File registered for integrity monitoring.")
        return

    if hashes[file_path] == current_hash:
        print("Integrity check passed. No changes detected.")
    else:
        print("WARNING: File integrity compromised!")
        log_event(f"MODIFICATION DETECTED: {file_path}")
        hashes[file_path] = current_hash
        save_hashes(hashes)


if __name__ == "__main__":
    main()