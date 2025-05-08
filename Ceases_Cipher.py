def encrypt(text, shift):
    
    cipher_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        if new_position > 25:
            new_position = 0 + (shift - 1)
            print(new_position)
            new_letter = alphabet[new_position]
        else:
            new_letter = alphabet[new_position]
        
        cipher_text +=new_letter
    print(cipher_text)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q','r', 's','t','u', 'v','w','x', 'y','z']

direction = input("Type 'ecncode' to encrypt, type 'decode' to decrypt:\n ")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
encrypt(text, shift)
