import random

chars = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*"
length = int(input("Enter Length: "))
password = ""

for a in range(length):
    password += random.choice(chars)

print(password)
