class Employee():
    language="Python"# class attribute
    salary="12 Lakh"
    
    def __init__(self,name,salary,language):# dunder method automatically called
        self.name=name
        self.salary=salary
        self.language=language
        print("I am creating a object")
        

    
s1=Employee("aman","120000","javascript")
print(s1.name,s1.language)