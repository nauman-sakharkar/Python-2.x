a=int(input("Please Enter the Number = "))
n1=0
n2=1
sum=1
output=[0,1]
if a==0:
    print("Fabonicci Sequence Is 0")
    print("Sum of Fabonicci Sequence = 0")
elif a<0:
    print("Plese enter a positive integer")
else:
    for i in range(1,a):
        n=n1+n2
        sum=n1+n2
        n1=n2
        n2=n
        output.append(n)
    print("Fabonicci Sequence:") 
    print(output)
    print("Fabonicci Value of ",a,"Is",sum)
    print("Thank You")
