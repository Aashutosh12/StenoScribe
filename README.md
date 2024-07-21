# StenoScribe

# Steganography with LSB Embedding and XOR Encryption

This Python script demonstrates a basic implementation of steganography using LSB (Least Significant Bit) embedding within image files. It encrypts data with a simple XOR cipher before embedding it into the RGB channels of pixels. The embedded data can then be extracted from the modified image, decrypted, and retrieved.

## Features

- **Embedding**: Embeds file metadata (size and name) and encrypted data into an image.
- **Extraction**: Extracts and decrypts embedded data from a modified image.
- **Encryption**: Uses a simple XOR cipher for data encryption before embedding.
- **Dependencies**: Relies on OpenCV for image manipulation and basic file handling operations.

## How it Works

1. **Embedding Process**:
   - Loads a vessel image and prepares data (file metadata and encrypted content).
   - Encrypts data with a passphrase using XOR encryption.
   - Splits encrypted data into bit sequences and embeds them into the least significant bits (LSBs) of RGB channels of consecutive pixels.
   - Saves the modified image with embedded data.

2. **Extraction Process**:
   - Loads a modified image containing embedded data.
   - Reads LSBs of RGB channels from pixels to reconstruct embedded bit sequences.
   - Combines bits into bytes and decrypts the data using the same XOR cipher and passphrase.
   - Retrieves and displays the decrypted data.
![snake](https://github.com/user-attachments/assets/56b4b780-0e89-4aba-b8d7-1b07bcba274c) 

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/steganography-lsb-xor.git
   cd steganography-lsb-xor
   ```

2. Install dependencies:
   ```bash
   pip install opencv-python
   ```

## Usage

- **Embedding Data**:
  ```bash
  python steganography.py embed path/to/vessel_image.jpg path/to/target_image.png path/to/file_to_embed.txt
  ```

- **Extracting Data**:
  ```bash
  python steganography.py extract path/to/modified_image.png
  ```

## Examples

- Embedding data into an image:
  ```bash
  python steganography.py embed images/vessel.jpg images/embedded.png files/secret.txt
  ```

- Extracting embedded data from an image:
  ```bash
  python steganography.py extract images/embedded.png
  ```

## Notes

- **File Size Limitation**: The current implementation is suitable for embedding small amounts of data due to the limitations of LSB steganography.
- **Security**: XOR encryption used here is basic and not suitable for high-security applications.
- **Contributions**: Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

