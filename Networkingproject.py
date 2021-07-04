import hashlib

result = hashlib.md5(b'Hello world')
print("The byte equivalent of hash is : ", end ="")

print(result.hexdigest())


print("SHA-256:", hashlib.sha256(b'Hello world').hexdigest())

print("SHA-3-256:", hashlib.sha3_256(b'Hello world').hexdigest())

print("BLAKE2c:", hashlib.blake2s(b'Hello world').hexdigest())
