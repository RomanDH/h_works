def encrypt(str, int):
    """
    Encrypts with Caesar's Cipher.
    :param str
    :param int
    :return encrypt str
    """
    index_result = []
    encrypt_result = []

    for i in str:
        index = ord(i)
        index_result.append(index + int)
    for j in index_result:
        encrypt_result.append(chr(j))
    return ''.join(encrypt_result)


def decrypt(str, int):
    """
    Decipher Caesar Cipher.
    :param str == def.encrypt(str, ...)
    :param int == def.encrypt(..., int)
    :return decrypt str
    """
    index_result = []
    decrypt_result = []

    for i in str:
        index = ord(i)
        index_result.append(index - int)
    for j in index_result:
        decrypt_result.append(chr(j))
    return ''.join(decrypt_result)

