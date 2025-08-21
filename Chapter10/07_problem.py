class Programer():
    company="Microsoft"
    def __init__(self,name,salary,pincode,Group):
        self.name=name
        self.salary=salary
        self.pincode=pincode
        self.Group=Group

p1=Programer("Aman","12lakh","458880","Group B")
print(p1.name,p1.salary,p1.pincode,p1.Group)

p1=Programer("Hariom","20lakh","468880","Group A")
print(p1.name,p1.salary,p1.pincode,p1.Group)

p1=Programer("Ajay","12lakh","458880","Group A")
print(p1.name,p1.salary,p1.pincode,p1.Group)

p1=Programer("Akshat","12lakh","458880","Group C")
print(p1.name,p1.salary,p1.pincode,p1.Group)
        
