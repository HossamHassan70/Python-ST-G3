class Person:
    def __init__(self, name, age, salary):
        self.__name = name 
        # public attribute/ member (self.name)
        # protected attribute/ member (self._name)
        # private attribute/ member (self.__name)
        self.age = age
        self._salary = salary
    def get_name(self): # Getter Method 
        return self.__name
        
user1 = Person('Ahmed', 25, 1000)
print(user1.age)
print(user1._salary)
# print(user1.__name) # AttributeError: 'Person' object has no attribute '__name'
print(user1.get_name())

class Protected:
    def __init__(self):
        self._age = 30  # Protected attribute
        self.__name = 'Ahmed'

class Subclass(Protected):
    def display_age(self):
        print(self._age)  # Accessible in subclass
        
    # def display_name(self):
    #     print(self.__name) # Cannot accessible in subclass

obj = Subclass()
# obj.display_name() # AttributeError: 'Subclass' object has no attribute '_Subclass__name'