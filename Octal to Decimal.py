a=int(input("Please Enter Your Octal Number = "))
j=1
o=0
while True :
    if a<1:
        break
    else:
        s=a%10
        o=o+s*j
        a=a//10
        j=j*8
print("Converted Number :",o)
