class Employee():
    language="Python"# class attribute
    salary="12 Lakh"
    

    def getinfo(self):
        print(f"The Language is.{self.language}. The salary is.{self.salary}")

    @staticmethod
    def gooday():
        print("Good Morning")
s1=Employee()
s1.language="Java"# instance attribute
s1.getinfo()
s1.gooday()
#print(s1.language,s1.salary)