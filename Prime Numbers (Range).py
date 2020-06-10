a=int(input("Enter The Start Number = "))
b=int(input("Enter The Last Number = "))
c=[]
for i in range(a,b+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            c.append(str(i))
print(','.join(c),"Are the Prime Numbers In Given Range")
print("Thank You")
