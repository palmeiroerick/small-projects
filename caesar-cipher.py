from dataclasses import dataclass
import sys

@dataclass(frozen=True)
class Letters:
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"


def main():
    text = input("Text: ")
    key = int(input("Key: "))
    print(cipher(text, key))


def cipher(text: str, key: int) -> str:
    if key < -25 or key > 25:
        sys.exit("The shift key must be between -25 and 25")

    cipher_text: list = []

    for char in text:
        if char.isupper():
            cipher_text.append(Letters.upper[(ord(char) - 65 + key) % 26])
        elif char.islower():
            cipher_text.append(Letters.lower[(ord(char) - 97 + key) % 26])
        else:
            cipher_text.append(char)

    return "".join(cipher_text)


def decipher(text: str, key: int) -> str:
    return cipher(text, key * -1)


def hackcipher():
    ...


if __name__ == "__main__":
    main()
