alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar_cipher(start_text, shift_amount, cipher_enc_or_dec):
    result = ""
    if cipher_enc_or_dec == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alph:
            pos = alph.index(char)
            new_pos = pos + shift_amount
            result += alph[new_pos]
        else:
            result += char
    print(f'This is the {cipher_enc_or_dec}d result: {result}')


from ascii_art import logo
print(logo)

end_of_game = False

while not end_of_game:
    enc_or_dec = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar_cipher(start_text=text, shift_amount=shift, cipher_enc_or_dec=enc_or_dec)

    play_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if play_again == "no":
        end_of_game = True
        print("Goodbye")