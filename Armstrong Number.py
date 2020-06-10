a=int(input("Enter The Number = "))
b=a
if a>99 and a<1000:
    r=a%10
    r1=r**3
    a=a//10
    p=a%10
    p1=p**3
    a=a//10
    s=a%10
    s1=s**3
    f=r1+p1+s1
    if f==b:
        print("The Entered Number Is A Armstrong Number")
    else:
        print("The Entered Number Is Not A Armstrong Number")
else:
    print("Please Enter The Correct Number")
print("Thank You")
