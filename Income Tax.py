m=int(input("Please Enter Your Monthly Income = "))
a=m*12
print("Your Annual Income Is = ",a)
t=0
if a<300000:
    t=t+0
if a>300000 and a<=500000:
    t=t+((a-300000)*.1)
if a>500000 and a<=800000:
    t=t+20000+((a-500000)*.2)
if a>800000:
    t=t+20000+60000+((a-800000)*.3)
print("Your Tax Amount Is ",t)
print("Please Pay Before 10th September 2016")
print("Thank You")
