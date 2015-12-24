class Person:
    "A person"
    def __init__(self,name):
        self.name=name
        print("A person biult.")

    def saymyname(self):
        print(self.name)
    def saymyclass(self):
        print(self.name+" from class Person.")

class Child(Person):
    "A child"
    def __init__(self,name):
        Person.__init__(self,name)
        print("A child biult.")
    def saymyclass(self):
        print(self.name+" from class Child.")


class Man(Person):
    "A man"
    def __init__(self,name):
        Person.__init__(self,name)
        print("A man biult.")
    def saymyclass(self):
        print(self.name+" from class Man.")

person1=Person("Person1")
child1=Child("Child1")
man1=Man("Man1")

items=[child1,man1,person1]
for item in items:
    print("")
    item.saymyname()
    item.saymyclass()
