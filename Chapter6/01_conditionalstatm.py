a=int(input("enter your age for voting :"))
if(a>=18):
    print("you are above age")
elif(a<0):
    print("you age is invalid")
elif(a==0):
    print("you age is zero")   
else:
    print("you are below age")
