a=int(input("Please Enter Your Naumber = "))
rev=0
g=0
h=0
rev2=0
while a>0:
    r=a%10
    rev=rev*10+r
    a=a//10
while rev>0:
    g=rev%10
    if g>0:
        h=h*10+g
    rev=rev//10
print("Your Requested Number Is ",h)
print("Thank Your")
