class animal:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def run(self):
        print("Anumal can run")
        print(f"Name of animal : {self.name} and brees : {self.breed}")
    def __dance(self):
        print("Dance can dancing")
    # for accessing private attribute
    def getDance(self):
        self.__dance()
class Dog(animal): # single inheritance
    def __init__(self, name, breed, age):
        super().__init__(name, breed)
        self.age = age
    def display(self):
        print("cat voice is like vowo")
        print("life of dogs are " , self.age)


class Human(Dog):
    def decisionMaker(self):
        print("Human can making decision")

# obj1 = Dog("tommy", "Libra",2)
# obj1.display()
# obj1.run()
# obj1.getDance()
obj2 = Human("tommy ", "Liber" , 3)
obj2.decisionMaker()
