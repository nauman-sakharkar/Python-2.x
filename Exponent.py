x=float(input("Please Enter The Number = "))
n=int(input("Please Enter The Number Of Steps = "))
t=1
sum=0
sum=sum+t
for i in range(1,n):
    t=(x*t)/(i)
    sum=t+sum
print("Exponential Value Of",x,"Is",sum)
print("Thank You")
