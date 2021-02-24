import string

def cipher_cipher_using_lookup(text,  key, characters = string.ascii_lowercase, decrypt=False):

    if key < 0:

        print("key cannot be negative")

        return None

    n = len(characters)

    if decrypt==True:

        key = n - key

    table = str.maketrans(characters, characters[key:]+characters[:key])
    
    translated_text = text.translate(table)
    
    return translated_text

plaintext = input('Plaintext: ')

encrypted = cipher_cipher_using_lookup(plaintext, 3, string.ascii_letters , decrypt=False)

print('Cyphertext: {}.'.format(encrypted))