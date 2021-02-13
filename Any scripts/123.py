
"""
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self,x):
        if x == 'name':
            print(self.name)
        elif x == 'age':
            print(self.age)
        else:
            print("Error")
a = Student('Вася', 17)
a.show('age')

"""

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name)
        print(self.age)
        
a = Student('Вася', 17)
print(dir(a))
