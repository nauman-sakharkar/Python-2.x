a=int(input("Enter The Start Number = "))
b=int(input("Enter The End Number = "))
for i in range(a,b+1):
    j=i
    r=0
    o=0
    s=0
    if i<99 or i>1000:
        print("Please Enter The Correct Range")
        break
    else:
        r=i%10
        r1=r**3
        i=i//10
        p=i%10
        p1=p**3
        i=i//10
        s=i%10
        s1=s**3
        f=r1+p1+s1
        if f==j:
            print("The",f," Is A Armstrong Number")
        else:
            continue    
print("Thank You")

        
