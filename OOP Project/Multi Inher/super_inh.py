class Parent1:
    def show(self):
        print("This is Parent1")

class Parent2:
    def show(self):
        print("This is Parent2")

class Child(Parent1, Parent2):
    def show(self):
        super().show()  
        print("This is the Child class")

obj = Child()
obj.show()
