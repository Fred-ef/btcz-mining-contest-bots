
#from binascii import hexlify, unhexlify
import hashlib

def validAddress(address):
    hex_address=toHex(address)
    hash1=hashlib.sha256(bytes.fromhex(hex_address[0:-8])).hexdigest()
    hash2=hashlib.sha256(bytes.fromhex(hash1)).hexdigest()
    if hash2[0:8]==hex_address[-8:]:
        return True
    else:
        return False

b58_digits = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def fromHex(b):
    """Encode bytes to a base58-encoded string"""

    # Convert big-endian bytes to integer
    #n = int('0x0' + hexlify(b).decode('utf8'), 16)
    n = int('0x0' + b, 16)

    # Divide that integer into bas58
    res = []
    while n > 0:
        n, r = divmod (n, 58)
        res.append(b58_digits[r])
    res = ''.join(res[::-1])

    # Encode leading zeros as base58 zeros
    import sys
    czero = b'\x00'
    if sys.version > '3':
        # In Python3 indexing a bytes returns numbers, not characters.
        czero = 0
    pad = 0
    for c in b:
        if c == czero: pad += 1
        else: break
    return b58_digits[0] * pad + res

def toHex(s):
    """Decode a base58-encoding string, returning bytes"""
    if not s:
        return b''

    # Convert the string to an integer
    n = 0
    for c in s:
        n *= 58
        if c not in b58_digits:
            return ""
        digit = b58_digits.index(c)
        n += digit

    # Convert the integer to bytes
    h = '%x' % n
    if len(h) % 2:
        h = '0' + h
    #res = unhexlify(h.encode('utf8'))
    res = h

    # Add padding back.
    #pad = 0
    #for c in s[:-1]:
    #    if c == b58_digits[0]: pad += 1
    #    else: break
    #return b'\x00' * pad + res
    return res