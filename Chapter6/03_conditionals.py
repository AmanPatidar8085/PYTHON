marks1=int(input("enter marks in subject1:"))
marks2=int(input("enter marks in subject2:"))
marks3=int(input("enter marks in subject3:"))
total_per=((100)*(marks1+marks2+marks3)/300)
if(total_per>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("Passed!")
else:
    print("Fail!")