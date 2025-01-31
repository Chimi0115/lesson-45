class Parrot:
    species="Bird"

    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=Parrot("Blu",2)
print("{} is a {}".format(p1.name,p1.species))
print("{} is {} years old".format(p1.name,p1.age))

p2=Parrot("Rio",4)
print("{} is a {}".format(p2.name,p2.species))
print("{} is {} years old".format(p2.name,p2.age))
