import hashlib
from PIL import Image

def calculate_hash(file_path, hash_algo='sha512'):
    """Calculate the hash of a filee"""
    hasher = getattr(hashlib, hash_algo)()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

