from code.encrypt_decrypt import *
from Crypto.Random import get_random_bytes

def test_encryptdecrypt():
    data=open('data/data.txt','r')
    key=get_random_bytes(16)
    lines=data.readlines()
    for line in lines:
        encryptedMsg=encrypt(key, line.encode())
        decryptedMsg=decrypt(encryptedMsg, key)
        msg=decryptedMsg[0].decode("utf8")
        assert line==msg