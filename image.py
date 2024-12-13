import hashlib
from PIL import Image

def calculate_hash(file_path, hash_algo='sha512'):
    """Calculate the hash of a filee"""
    hasher = getattr(hashlib, hash_algo)()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def modify_image_to_match_prefix(input_image, output_image, desired_prefix, hash_algo='sha512'):
    """Modify image to the desired prefix"""
    print(f"Starting with input image: {input_image}")
    try:
        img = Image.open(input_image)
        img.show()
    except Exception as e:
        print(f"Error opening input image: {e}")
        return
    try:
        img.save(output_image, format='PNG')
        print(f"Image saved to {output_image}")
    except Exception as e:
        print(f"Error saving initial outut image: {e}")
        return


    with open(output_image, 'r+b') as f:
        content = bytearray(f.read())
        print(f"Attempting to modify hash to match desired prefix {desired_prefix}")
        for i in range(len(content)):
            original_byte = content[i]
            for j in range(256):
                content[i] = j
                f.seek(0)
                f.write(content)
                current_hash = calculate_hash(output_image, hash_algo)
                if current_hash.startswith(desired_prefix):
                    print(f"Success: Hash modified to match desired prefix {desired_prefix}")
                    print(f"Final hash: {current_hash}")
                    return
            content[i] = original_byte
    print(f"Failed: Could not modify hash to match desired prefix {desired_prefix}")
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <input_image> <desired_prefix> <output_image>")
    else:
        input_image, desired_prefix, output_image = sys.argv[1], sys.argv[2], sys.argv[3]
        modify_image_to_match_prefix(input_image, output_image, desired_prefix.strip("0x"))