import hashlib
md5 = hashlib.md5()
print("finish")

md5.update(b'bobo!')
print(md5.hexdigest())
print(md5)