
ch=input("enter a character: ")
if ch>='0' and ch<='9':
    print("digit")
elif ch.isupper():
    print("upper case character")
elif ch.islower():
    print("lower case character")
else:
    print("special chracter")

