n = 5
m = n + 2
F = n * m - n - m 
G = (n - 1) * (m - 1) // 2
LCM = n * m
key_sequence = [(LCM * G) % F, ((n + m) // 2) % 256, (n**2) % 8, (m**2) % 8]

def encrypt(message):
    encrypted = ""
    for i, char in enumerate(message):
        shift = key_sequence[i % len(key_sequence)]
        encrypted += chr((ord(char) + shift) % 256)
    return encrypted

def decrypt(cipher):
    decrypted = ""
    for i, char in enumerate(cipher):
        shift = key_sequence[i % len(key_sequence)]
        decrypted += chr((ord(char) - shift) % 256)
    return decrypted
while True:
    print(" Encryption/Decryption System")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")
    choice = input("Choose an option (1-3): ")

    if choice == "1":
        msg = input("Enter message to encrypt: ")
        encrypted_msg = encrypt(msg)
        print("Encrypted message:", encrypted_msg)
    elif choice == "2":
        cipher = input("Enter message to decrypt: ")
        decrypted_msg = decrypt(cipher)
        print("Decrypted message:", decrypted_msg)
    elif choice == "3":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
