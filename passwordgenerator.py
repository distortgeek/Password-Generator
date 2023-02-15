import random

length = int(input("Enter the length of password you want : "))
a = 0
b = ''
lc = "abcdefghijklmnopqrstuvwxyz"
uc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
no = "1234567890"
sym = "~`!@#$%^&*()_-+=[]\|':;?/<>,."

if length > 0:
    while length > a:
        lst = [lc,uc,no,sym]
        x = random.choice(lst)
        y = random.choice(x)
        b = b+y
        a = a+1
    print("Your Password : ",b)
else:
    print("Length of password can't be zero.")

