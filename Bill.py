u=int(input("Please Enter The Unit = "))
a=0
if u<=100:
    a=a+100+(u*2)
if u>100 and u<=200:
    a=a+100+200+((u-100)*4)
if u>200 and u<=300:
    a=a+100+200+400+((u-200)*6)
if u>300 and u<=400:
    a=a+100+200+400+600+((u-300)*8)
if u>400:
    u=u-400
    a=a+100+200+400+600+800+(u*10)
if a>2000:
    a=a+(a-2000)*.1
print("Your Bill Amount Is ",a)
print("Please Pay Before 10th September 2016")
print("Thank You")
