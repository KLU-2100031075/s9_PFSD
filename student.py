class Student:
    def __init__(self,id,name,cgpa):
        self.id=id
        self.name=name
        self.cgpa=cgpa
s=Student(10,"ABC",9.5)
print(getattr(s,"name"))
print(getattr(s,'id'))
setattr(s,"cgpa",9)
print(getattr(s,"cgpa"))
delattr(s,"cgpa")
print(hasattr(s,"id"))
print(hasattr(s,"cgpa"))