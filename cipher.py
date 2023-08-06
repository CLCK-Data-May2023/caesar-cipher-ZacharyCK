# Caesar Cipher
def caesar_encrypt(plaintext, shift):
    cipher_text = ""
    for letter in plaintext:

        # The python string isalpha() method is used to check whether the string consists of alphabets.
        if letter.isalpha():
            # get encrypted character with this formula
            base = ord('A') if letter.isupper() else ord('a')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            cipher_text += shifted_char

        else:
            # return character if not an actual letter
            cipher_text += letter

    return cipher_text


# Decrypting function
def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

# Keep looping until break
while True:
    cipher_shift = int(input("Enter the Number of Shift:"))
    if cipher_shift == 0:
        print("Please Input a valid shift Number")
        continue
    else:
        break

# Ask User for a Phrase
plaintext = input("Enter Phrase:")    

# Encrypts the Text
encrypted_text = caesar_encrypt(plaintext, cipher_shift)
print("Encrypted:", encrypted_text)

# Decrypts the Text
decrypted_text = caesar_decrypt(encrypted_text, cipher_shift)
print("Decrypted:", decrypted_text)# add your code here
