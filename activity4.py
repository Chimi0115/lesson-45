class Parrot:
    species="Bird"

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sing(self,song):
        return"{} sings song {}".format(self.name,song)
    
    def dance(self):
        return"{} is now dancing".format(self.name)
    
p1=Parrot("Blu",2)
print("{} is a {}".format(p1.name,p1.species))
print(p1.sing("Happy"))
print(p1.dance())

p2=Parrot("Rio",2)
print("{} is a {}".format(p2.name,p2.species))
print(p2.sing("Happy"))
print(p2.dance())
