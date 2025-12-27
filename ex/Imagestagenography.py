from PIL import Image

DELIMITER = "#####"

def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

def encode_image(input_image, output_image, secret_message):
    image = Image.open(input_image).convert("RGB")
    pixels = image.load()

    secret_message += DELIMITER
    binary_data = text_to_binary(secret_message)

    data_index = 0
    data_len = len(binary_data)
    width, height = image.size

    for y in range(height):
        for x in range(width):
            if data_index < data_len:
                r, g, b = pixels[x, y]

                r = (r & ~1) | int(binary_data[data_index])
                data_index += 1

                if data_index < data_len:
                    g = (g & ~1) | int(binary_data[data_index])
                    data_index += 1

                if data_index < data_len:
                    b = (b & ~1) | int(binary_data[data_index])
                    data_index += 1

                pixels[x, y] = (r, g, b)
            else:
                image.save(output_image)
                print("[+] Message hidden successfully.")
                return

    image.save(output_image)
    print("[+] Message hidden successfully.")

def decode_image(stego_image):
    image = Image.open(stego_image)
    pixels = image.load()

    width, height = image.size
    binary_data = ""

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)

    decoded_text = binary_to_text(binary_data)
    message = decoded_text.split(DELIMITER)[0]

    print("[+] Hidden message:")
    print(message)

def main():
    print("\nIMAGE STEGANOGRAPHY (LSB METHOD)")
    print("1. Encode Message")
    print("2. Decode Message")

    choice = input("Choose option (1/2): ")

    if choice == "1":
        input_image = input("C:\Users\Nisarg\OneDrive\Desktop\ex\123.png ")
        output_image = input("C:\Users\Nisarg\OneDrive\Desktop\ex\123.png ")
        message = input("heyy ")
        encode_image(input_image, output_image, message)

    elif choice == "2":
        stego_image = input("C:\Users\Nisarg\OneDrive\Desktop\ex\123.png ")
        decode_image(stego_image)

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
