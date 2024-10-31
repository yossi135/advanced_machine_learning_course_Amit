from abc import ABC , abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
         pass
     
    def describe(self):
        print("This is an animal.")
         
class Cow(Animal) :
    
    def make_sound(self):
        return 'hooo'
    
class Dog(Animal):
    
    def make_sound(self):
        return "Woof!"  

class Cat(Animal):
    def make_sound(self):
        return "Meow!"  
    
dog=Dog()
cat=Cat()
cow=Cow()

dog.describe()
print(dog.make_sound())
cow.describe()
print(cow.make_sound())
cat.describe()
print(cat.make_sound())