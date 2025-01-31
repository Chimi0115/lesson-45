class Student:
    grade=9
    name="Dhendup"

    def show(self):
        print("Hi i am a Student")

    def intro(self):
        print("Hi I am a student")

    def intro(self):
        print("I am a {} and i study in grade {}".format(self.name,self.grade))

stud1=Student()
stud1.show()
stud1.intro()