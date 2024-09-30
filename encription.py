import hashlib as a
from numpy import base_repr

def encrip(text):
    list1=(a.md5,a.sha224,a.sha256,a.sha384,a.sha512,a.sha3_224,a.sha3_256,a.sha3_384,a.sha3_512,a.blake2s,a.blake2b,a.md5)
    for i in range (11):
        h=list1[i]
        b = h(str(text).encode())#str to hash
        md5_hash = b.hexdigest()
        #print(md5_hash)
        d = int(md5_hash, 36)#hash to base 10
        for k in range (2,37):
            if k<36:
                g = base_repr(d, k)#base 2 to 35
                #print(g)
                j = list1[i+1](str(g).encode())#changing hash type
                m = j.hexdigest()
                #print(m)
                d = int(m, 36)#hash to base 10
            else:
                text=d
                #print(text)
        te = h(str(text).encode())
        text = te.hexdigest()
    return text
