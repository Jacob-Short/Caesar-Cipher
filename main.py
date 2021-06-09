alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

enc_or_dec = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar_cipher(start_text, shift_amount, cipher_enc_or_dec):
  result = ""
  if enc_or_dec == "decode":
      shift_amount *= -1
  for l in start_text:
    if l in alph:
        pos = alph.index(l)
        new_pos = pos + shift_amount
        result += alph[new_pos]
    else:
        result += l
  print(f"This is the {enc_or_dec}d result: {result}")

caesar_cipher(start_text=text, shift_amount=shift, cipher_enc_or_dec=enc_or_dec)