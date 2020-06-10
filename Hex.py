a=list(input("Enter the Hecadecimal : "))
b={0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
a.reverse()
c=[]
dec=0
for i in range(len(a)):
    for j in b.keys():
        if a[i]==b[j]:
            dec=dec+(16**i)*j
print(dec)
