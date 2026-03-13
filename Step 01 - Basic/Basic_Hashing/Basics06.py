class Student:
    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return hash(self.name)

s1 = Student("Soutik")
print(hash(s1))