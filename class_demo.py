class Person(object):
    def __init__(self):
        self.name = "Tom"
    def getName(self):
        return self.name

class Student(Person):
    def __init__(self):
        Person.__init__(self)
        self.age = 12
    def getAge(self):
        return self.age

if __name__ == "__main__":
    stu = Student()
    print(stu.getName())