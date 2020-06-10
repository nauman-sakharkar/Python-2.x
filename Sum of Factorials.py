a=int(input("Please Enter Your Number = "))
b=int(input("Please Enter Your Number = "))
sum=0
for i in range(a,b+1):
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    print("Factorial of ",j," = ",fact)
    sum=sum+fact
print("Sum of Factorials = ",sum)
print("Thank You")
