marks=int(input("enter a marks in result"))

if(marks<=100 and marks>=90):
  print("Grade Exellent")
elif(marks<90 and marks>=80):
  print("Grade A")
elif(marks<80 and marks>=70):
  print("Grade B")
elif(marks<70 and marks>=600):
  print("Grade C")
elif(marks<60 and marks>=50):
  print("Grade D")
elif(marks<50 and marks>=40):
  print("Grade E")
else:
  print("fail")