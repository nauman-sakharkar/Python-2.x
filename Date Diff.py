print("▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄")
d=int(input("Please Enter The Date : "))
m=int(input("Please Enter The Month : "))
y=int(input("Please Enter The Year : "))
n=int(input("Please Enter Rhe Increment/Decrement : "))
s=input("Please Enter The Arithmetic Operation : ")
print("-------------------------------------------------")
if m>12 or d>31:
        print("Please Enter The Correct Date/Month(Range for Date(1-31) & Range for Month(1-12)")
elif s=="+":
    if m==2:
        if y%4==0:
            if d==29:
                d=1
                n=n-1
                d=d+n
                m=m+1
                print("Your Requested Date : ",d,"/",m,"/",y)
            elif d>29:
                print("Feb Doesn't Have more than 29 date (Leap Year)")
            else:
                d1=d+n
                if d1>29:
                    d=29-d
                    n=n-d
                    d=n
                    m=1+m
                    print("Your Requested Date : ",d,"/",m,"/",y)
                else:
                    d=d+n
                    print("Your Requested Date : ",d,"/",m,"/",y)
        elif d==28:
            d=1
            n=n-1
            d=d+n
            m=m+1
            print("Your Requested Date : ",d,"/",m,"/",y)
        elif d>28:
            d=d+n
            print("This Feb Doesn't Have more than 28 date (Not A Leap Year)")
        else:
            d1=d+n
            if d1>28:
                d=28-d
                n=n-d
                d=n
                m=1+m
                print("Your Requested Date : ",d,"/",m,"/",y)
            else:
                d=d+n
                print("Your Requested Date : ",d,"/",m,"/",y)
    elif m==12:
        if d==31:
            d=1
            n=n-1
            d=d+n
            m=1
            y=y+1
            print("Your Requested Date : ",d,"/",m,"/",y)
        else:
            d1=d+n
            if d1>31:
                d=31-d
                n=n-d
                d=n
                m=1
                y=y+1
                print("Your Requested Date : ",d,"/",m,"/",y)
            else:
                d=d+n
                print("Your Requested Date : ",d,"/",m,"/",y)
    elif m==1 or m==3 or m==5 or m==7 or m==10 or m==8:
        if d==31:
            d=1
            n=n-1
            d=d+n
            m=m+1
            print("Your Requested Date : ",d,"/",m,"/",y)
        else:
            d1=d+n
            if d1>31:
                d=31-d
                n=n-d
                d=n
                m=1+m
                print("Your Requested Date : ",d,"/",m,"/",y)
            else:
                d=d+n
                print("Your Requested Date : ",d,"/",m,"/",y)
    elif m==4 or m==6 or m==9 or m==11:
        if d==30:
            d=1
            n=n-1
            d=d+n
            m=m+1
            print("Your Requested Date : ",d,"/",m,"/",y)
        else:
            d1=d+n
            if d1>30:
                d=30-d
                n=n-d
                d=n
                m=1+m
                print("Your Requested Date : ",d,"/",m,"/",y)
            else:
                d=d+n
                print("Your Requested Date : ",d,"/",m,"/",y)
elif s=="-":
    if m==2:
        if y%4==0:
            if d==1:
                d=31-n+1
                m=m-1
                print("Your Requested Date : ",d,"/",m,"/",y)
            elif d>29:
                print("Feb Doesn't Have more than 29 date (Leap Year)")
            else:
                d1=d-n
                if d1<=0:
                    d=1-d
                    n=n+d-1
                    d=31-n
                    m=m-1
                    print("Your Requested Date : ",d,"/",m,"/",y)
                else:
                    d=d-n
                    print("Your Requested Date : ",d,"/",m,"/",y)
        elif d==1:
            d=31-n+1
            m=m-1
            print("Your Requested Date : ",d,"/",m,"/",y)
        elif d>28:
            d=d+n
            print("This Feb Doesn't Have more than 28 date (Not A Leap Year)")
        else:
            d1=d-n
            if d1<=0:
                d=1-d
                n=n+d-1
                d=31-n
                m=m-1
                print("Your Requested Date : ",d,"/",m,"/",y)
            else:
                d=d-n
                print("Your Requested Date : ",d,"/",m,"/",y)
    elif m==1:
        if d==1:
            d=31-n+1
            m=1
            y=y-1
            print("Your Requested Date : ",d,"/",m,"/",y)
        else:
            d1=d-n
            if d1<=0:
                d=1-d
                n=n+d-1
                d=31-n
                m=1
                y=y-1
                print("Your Requested Date : ",d,"/",m,"/",y)
            else:
                d=d-n
                print("Your Requested Date : ",d,"/",m,"/",y)
    elif m==3:
        if y%4==0:
            if d==1:
                d=29-n+1
                m=m-1
                print("Your Requested Date : ",d,"/",m,"/",y)
            else:
                d1=d-n
                if d1<=0:
                    d=1-d
                    n=n+d-1
                    d=29-n
                    m=m-1
                    print("Your Requested Date : ",d,"/",m,"/",y)
                else:
                    d=d-n
                    print("Your Requested Date : ",d,"/",m,"/",y)
        else:
            if d==1:
                d=28-n+1
                m=m-1
                print("Your Requested Date : ",d,"/",m,"/",y)
            else:
                d1=d-n
                if d1<=0:
                    d=1-d
                    n=n+d-1
                    d=28-n
                    m=m-1
                    print("Your Requested Date : ",d,"/",m,"/",y)
                else:
                    d=d-n
                    print("Your Requested Date : ",d,"/",m,"/",y)
                    
    elif m==5 or m==7 or m==10 or m==12:
        if d==1:
            d=30-n+1
            m=m-1
            print("Your Requested Date : ",d,"/",m,"/",y)
        else:
            d1=d-n
            if d1<=0:
                d=1-d
                n=n+d-1
                d=30-n
                m=m-1
                print("Your Requested Date : ",d,"/",m,"/",y)
            else:
                d=d-n
                print("Your Requested Date : ",d,"/",m,"/",y)
    elif m==8:
        if d==1:
            d=31-n+1
            m=m-1
            print("Your Requested Date : ",d,"/",m,"/",y)
        else:
            d1=d-n
            if d1<=0:
                d=1-d
                n=n+d-1
                d=31-n
                m=m-1
                print("Your Requested Date : ",d,"/",m,"/",y)
            else:
                d=d-n
                print("Your Requested Date : ",d,"/",m,"/",y)
print("-------------------------------------------------")
print("▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄")
