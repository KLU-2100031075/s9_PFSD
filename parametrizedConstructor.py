class Student:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def display(self):
        print(self.id,self.name)

std1=Student(10,"abc")
std2=Student(20,"def")
std1.display()
std2.display()