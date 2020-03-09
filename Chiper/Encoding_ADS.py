from random import randint

string = "Version control system is fun"  # String to encrypt
shift = randint(0, 26)  # Randomly selects an integer between 0 and 26


def main():
    """
    Docstring
    """
    choice = input("Press 1 for Encryption\n"
                   "Press 2 for Decryption\n"
                   "Press 3 for Quiting the program\n")
    while True:
        if choice == "1":
            decrypt(x=string)
            main()
        elif choice == "2":
            ceasar_chipher()
            main()
        elif choice == "3":
            quit()
        else:
            return


def decrypt(x):  # Decrypt the string
    unencoded_string = ""  # Variable that has new shifted letters appended to it to form the complete string
    for i in x:  # Loops through each letter of the string
        unencoded_string += chr(ord(i) - shift)  # Uses the integer we got from random to shift the letters accordingly

    print(f"\nDecrypt string using caesar cipher shifting the letters {shift} times backward.\n"
          f"String to decrypt: {x}\nUnencoded string: {unencoded_string}")


def ceasar_chipher():  # Encodes the string
    encoded_string = ""  # Variable that has new shifted letters appended to it to form the complete string

    for i in string:  # Loops through each letter of the string
        encoded_string += chr(ord(i) + shift)  # Uses the integer we got from random to shift the letters accordingly

    print(f"Encoding string using caesar cipher shifting the letters {shift} times forward.\n"
          f"String to encode: {string}\nEncoded string: {encoded_string}\n")


if __name__ == "__main__":
    main()

