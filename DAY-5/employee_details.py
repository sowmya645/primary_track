class employee:
    def __init__(self,name,email,employee_id,phone_number,department):
        self.name=name
        self.email=email
        self.employee_id=employee_id
        self.phone_number=phone_number
        self.department=department
    def display(self):
        print(f"Name of the employee: {self.name}")
        print(f"Email of the employee: {self.email}")
        print(f"Employee ID of the employee: {self.employee_id}")
        print(f"Phone Number of the employee: {self.phone_number}")
        print(f"Department of the employee: {self.department}")
    def pd(self,*args):#
        for i in args:
            print(i)

    def dept(self):
        print("general department")
    
class hr(employee):
    def dept(self):
        print("hr")
class dev(employee):
    def dept(self):
        print("dev")
    def df(Self):
        print("devv")
class proj(dev):
    def dept(self):
        print("project")
    def df(self):
        return super().df()
class dev_hr(dev,hr):
    def wor(self):
        print("dev_hr")
name=input("enter the employee name:")
email=input("enter the employee email: ")
employee_id=input("enter the employee id: ")
phone_number=input("enter the employee phone number: ")
department=input("enter the employee department name: ")
e1=employee(name,email,employee_id,phone_number,department)
e1.display()
e1.pd(name)
e1.pd(name,email)

for d in (hr(name,email,employee_id,phone_number,department),dev(name,email,employee_id,phone_number,department)):
    d.dept()
d1=proj(name,email,employee_id,phone_number,department)#multiple
d1.df()
d1.dept()
c1=dev_hr(name,email,employee_id,phone_number,department)#hier
c1.dept()

