class Parent:
    def fn1(self):
        print("This is parent class")


class Child(Parent):
    def fn2(self):
        print("This is child class")


ob = Child()
ob.fn1()
ob.fn2()