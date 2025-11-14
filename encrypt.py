from cryptography.fernet import Fernet

def question():
    while True:
        q = input('Encrypt or Decrypt [e/d]? ').lower()

        if q == 'e':
            encry = input ('Message to encrypt: ').encode()
            keyE = Fernet.generate_key()
            fernet = Fernet(keyE)
            encmessage = fernet.encrypt(encry)
            print(f'Enccrypted: ', {encmessage.decode()})
            print(f'Save this key: ', {keyE.decode()})

        elif q == 'd':
            keyD = input ('Key used in the encryption: ').encode()
            dernet = Fernet(keyD)
            decry = input ('Message to decrypt: ').encode()
            decmessage = dernet.decrypt(decry)
            print(f'Decrypted message: {decmessage.decode()}')

        else:
            print('Invalid option. Please enter "e" for encrypt or "d" for decrypt.')
            continue
        return