class student:
    def __init__(self,name,age):#constructor
        self.name=name
        self.age=age
        
    def hello(self):
        print(f"Hello {self.name},I am a student of age {self.age}.")
 

s1=student(name="Alice",age=20)
s1.hello()