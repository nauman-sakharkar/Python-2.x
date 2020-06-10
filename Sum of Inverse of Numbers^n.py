n=int(input("Enter the Number Of Times = "))
q=int(input("Enter The Number = "))
sum=0
for i in range(1,n+1):
    sum=sum+((1/q)**i)
print("",sum)
