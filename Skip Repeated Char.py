list=input("Please Enter Your List = ")
output=[]
output = [n for n in list if n not in output]
print("Your Requested List : ", ''.join(output))
print("Thank You")
