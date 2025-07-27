from dataclasses import dataclass
import sys

@dataclass(frozen=True)
class Letters:
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"


def main():
    text = input("Text: ")
    for value in hack_cipher(text).values():
        print(value)


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


def hack_cipher(text: str) -> str:
    options: dict = {key: cipher(text, key) for key in range(1, 25)} 

    with open("./dictonary", "r") as file:
        words: set = {word.strip() for word in file}

    for key, value in options.items():
        possible_words = value.split(" ")

        valid_words[key] = 0

        for possible_word in possible_words:
            if possible_word.lower() in words:
                valid_words[key] += 1

    for key, value in options.items():


    return options


if __name__ == "__main__":
    main()
