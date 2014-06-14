# Anurag Mukkara
# 11 June 2014
# cipher.py

phrase = raw_input("Enter the plaintext to be encryped: ")
shift_amount = input("Enter an integer shift amount: ")

def encrypt(a, shift_amount):
    asc2_code = ord(a)
    if 64 < asc2_code < 91:
        asc2_code = 65 + (asc2_code - 65 + shift_amount)%26
    elif 96 < asc2_code < 123:
        asc2_code = 97 + (asc2_code - 97 +  shift_amount)%26

    return chr(asc2_code)
    
encoded_phrase = ''
for c in phrase:
    encoded_phrase = encoded_phrase + encrypt(c, shift_amount)

print encoded_phrase
