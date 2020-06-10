a=int(input("Enter the Number = "))
if a>1:
    for i in range(2,a):
        if a%i==0:
            print(a,"is Not a Prime Number")
            print(i,"times",a//i,"is",a)
            break
    else:
        print(a,"is a Prime Number")
else:
    print(a,"is a Prime Number")    
print("Thank You")
