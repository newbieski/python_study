# parent class
class Animal :
    def __init__(self, type) :
        self.animal_type = type
    def eat(self) :
        print(f'{self.animal_type} eats')

class Dog(Animal) :
    def speaking(self) :
        print("bow")

class Cat(Animal) :
    def speaking(self) :
        print('meow')

t1 = Dog("dog")
print(t1.animal_type)
t1.eat()
t1.speaking()

t2 = Cat("cat")
print(t2.animal_type)
t2.eat()
t2.speaking()