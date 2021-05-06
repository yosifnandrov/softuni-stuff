key = int(input())
interval = int(input())
decrypted = ""
for char in range(1, interval + 1):
    symbol = input()
    real = ord(symbol) + key
    decrypted += chr(real)
print(f"{decrypted}")