x=float(input("Please Enter The Number = "))
n=int(input("Please Enter The Number Of Steps = "))
xx=x
x=(x*3.142)/(180)
t=1
s=-1
sum=0
sum=sum+t
for i in range(1,n):
    t=(x*x*t*s)/((2*i)+(2*(i-1)))
    sum=t+sum
print("Cosine Value Of",xx,"Is",sum)
print("Thank You")
