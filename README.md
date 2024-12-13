# ImageHashSpoofing

## Overview

A Python script that modifies image bytes to generate a hash with a specific prefix, useful for cryptographic experiments and hash collision exploration.

## 🚀 Features

- Calculate file hashes using SHA-512 (default) or other hash algorithms
- Modify image bytes to generate a hash with a desired prefix
- Flexible command-line interface
- Support for different input and output image files

## 📋 Prerequisites

- Python 3.7+
- Pillow (PIL) library

## 🔧 Installation

1. Clone the repository
```bash
git clone https://github.com/carlkiptoo/image-hash-modifier.git
cd image-hash-modifier
```

2. Install dependencies
```bash
pip install Pillow
```

## 💡 Usage

### Command-Line Interface

```bash
python image_hash_modifier.py <input_image> <desired_prefix> <output_image>
```

### Example

```bash
python image_hash_modifier.py input.png 00000 output.png
```

This attempts to modify `input.png` to generate a hash starting with '00000'.

## 🛠️ Functions

### `calculate_hash(file_path, hash_algo='sha512')`

Calculates the hash of a file.

- **Parameters**:
  - `file_path`: Path to the file
  - `hash_algo`: Hash algorithm (default: 'sha512')

### `modify_image_to_match_prefix(input_image, output_image, desired_prefix, hash_algo='sha512')`

Modifies an image to generate a hash with a specific prefix.

- **Parameters**:
  - `input_image`: Source image path
  - `output_image`: Modified image save path
  - `desired_prefix`: Desired hash prefix
  - `hash_algo`: Hash algorithm (default: 'sha512')

##  Limitations

- Computationally intensive
- No guaranteed match for hash prefix
- Very slow for longer prefixes

##  Security Notes

- Experimental tool
- Not for cryptographic security
- Modifies image byte content

##  Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Disclaimer
This tool is for educational and experimental purposes only.
