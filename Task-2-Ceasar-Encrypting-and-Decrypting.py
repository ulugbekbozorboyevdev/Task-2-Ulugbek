a= input('enter a word: ')
shiftingamount= int(input('enter a shifting amount: '))
asking=input('do you want to encrypt or decrypt? (e/d): ')

if asking == 'd':
    shiftingamount = -shiftingamount

def encrypt(b):

    encrypted=''

    for letter in b:
        if not letter.isalpha():
                    encrypted += letter
                    continue
        base = 65 if letter.isupper() else 97
        ceaser_f= (ord(letter) - base +shiftingamount)%26 + base
        encrypted += chr(ceaser_f)
    return encrypted

print(encrypt(a))