class food:
    def menu(self):
        print("some food")
class indian(food):
    def menu(self):
        print("Dosa,idli,vada")
class italian(food):
    def menu(self):
        print("pizza,pasta,lasagna")
for food in (indian(),italian()):
    food.menu()
