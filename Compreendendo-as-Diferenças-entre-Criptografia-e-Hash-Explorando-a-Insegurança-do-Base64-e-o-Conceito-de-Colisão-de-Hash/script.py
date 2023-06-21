import hashlib


def calculate_md5(data):
    md5_hash = hashlib.md5()
    md5_hash.update(data.encode('utf-8'))
    return md5_hash.hexdigest()


def calculate_sha1(data):
    sha1_hash = hashlib.sha1()
    sha1_hash.update(data.encode('utf-8'))
    return sha1_hash.hexdigest()


def calculate_sha256(data):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8'))
    return sha256_hash.hexdigest()


# Exemplo de uso
message = "Hello, World!"
md5_hash = calculate_md5(message)
sha1_hash = calculate_sha1(message)
sha256_hash = calculate_sha256(message)


print("MD5 Hash:", md5_hash)
print("SHA-1 Hash:", sha1_hash)
print("SHA-256 Hash:", sha256_hash)
