k = "version".encode("utf-8").hex() + 5 * ("00")
print(k)
k = bytes.fromhex(k)
print(bytes.decode(k,"utf-8"))
