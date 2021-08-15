import random

char_ = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()_-+={[}]|\:;<,>.?/"
passwd = ""

count = int(input("Enter Password Length: "))
x = 0

while x != count:
    passwd = passwd + str(random.choice(char_))
    x += 1
print(passwd)