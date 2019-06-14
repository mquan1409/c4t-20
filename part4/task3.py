a = input("Ten dang nhap? ")
while True:
    c = input("email? ")
    if c.find('@')!=-1:break
while True:
    b1 = input("Mat khau? ")
    b2 = input("Nhap lai mat khau? ")
    if b1 == b2 and len(b1) > 8 and any(char.isdigit() for char in b1) and not b1.isdigit(): break

print("Done")