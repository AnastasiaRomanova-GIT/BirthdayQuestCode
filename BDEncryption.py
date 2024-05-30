def encrypt_message(message, shift):
    alphabet = list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
    encrypted_message = ""
    
    for char in message.upper():
        if char in alphabet:
            old_index = alphabet.index(char)
            new_index = (old_index + shift) % len(alphabet)
            encrypted_message += alphabet[new_index]
        else:
            encrypted_message += char
    
    return encrypted_message

if __name__ == "__main__":
    # Введите ваше сообщение и сдвиг здесь
    message = "как обычно, в углу (на кухне)"
    shift = 2
    
    encrypted_message = encrypt_message(message, shift)
    print(encrypted_message.title())
