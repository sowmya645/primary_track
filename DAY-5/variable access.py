class parent:
    def __init__(self):
        self.public_var="Public"
        self._protected_var="Protected"
        self.__private_var="private"
    def access_from_same_class(self):
        print("Inside parent class")
        print("public:",self.public_var)
        print("Protected:",self._protected_var)
        print("Private",self.__private_var)
class Child(parent):
    def access_from_same_class(self):
        print("Inside child class(subclass):")
        print("Public",self.public_var)
        print("Protected",self._protected_var)
        print("Private",self.__private_var)
p=parent()
p.access_from_same_class()
c=Child()
c.access_from_same_class()