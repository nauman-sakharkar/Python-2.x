a=int(input("Pleate Enter Your Starting Number = "))
b=int(input("Pleate Enter Your Ending Number = "))
sum=0
count=0
for i in range(a,b+1):
    if i%2==0:
        print("",i)
        sum=sum+i
        count=count+1
print("Your Even Number's Sum Is ",sum)
print("Your Even Number's Count Is ",count)
print("Thank You")
        
