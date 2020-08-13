import json
from base64 import b64encode
from Crypto.Cipher import AES
from base64 import b64decode
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
import logging

json_k = ['nonce', 'header', 'ciphertext', 'tag', 'salt']

def encrypt(key, msg):

    try:
        header = b"header"
        salt = get_random_bytes(16)
        #####generate encrypted key using pbkdf
        encryptedKey = PBKDF2(key, salt, 32, count=1000000, hmac_hash_module=SHA512)
        encrpyted = AES.new(encryptedKey, AES.MODE_GCM)
        encrpyted.update(header)
        ciphertext, tag = encrpyted.encrypt_and_digest(msg)
        y = encrpyted.nonce, header, ciphertext, tag, salt
        i = 0
        json_v = []
        for x in y:
            json_v.append(b64encode(x).decode('utf-8'))
            i += 1
        result = json.dumps(dict(zip(json_k, json_v)))
    except ValueError as e:
        raise ValueError('Decryption Failed! Security Alert!!: %s' % logging.ERROR)
    return result

def decrypt(json_resut_from_encrypt, key):
    try:
        json_resut_from_encrypt = json_resut_from_encrypt.replace("}{", "},,{")
        plaintext = []
        for json_decrypt_obj in json_resut_from_encrypt.split(",,"):
            b64 = json.loads(json_decrypt_obj.encode())
            i = 0
            json_value = {}
            for k in json_k:
                json_value[k] = (b64decode(b64[k]))
                i += 1
            encryptedKey = PBKDF2(key, json_value['salt'], 32, count=1000000, hmac_hash_module=SHA512)
            cipher = AES.new(encryptedKey, AES.MODE_GCM, nonce=json_value['nonce'])
            cipher.update(json_value['header'])
            plaintext.append(cipher.decrypt_and_verify(json_value['ciphertext'], json_value['tag']))
    except ValueError as e:
        raise ValueError('Encryption Failed! Security Alert!!: %s' % logging.ERROR)
    return plaintext