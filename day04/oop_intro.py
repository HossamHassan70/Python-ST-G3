# Class => is a blueprint for creating objects (instances)
    # - properties (characteristics) (color, price, brand ...)
    # - methods (Behavior) (move, sound ...)
# object => is an instance from class
# constructor method

class Car:
    no_of_obj = 0 # class attribute
    # spacial method that is called when an object create
    def __init__(self, b, c, price, speed): # constructor
        self.brand = b # instance attribute
        self.color = c
        self.price = price
        self.speed = speed
        Car.no_of_obj += 1
        
    def get_all_info(self): # instance method
        print(f'Brand is: {self.brand} \nspeed is: {self.speed} \ncolor: {self.color} \nprice: {self.price}')
    def change_brand_and_color(self, new_brand, new_color):
        self.brand = new_brand
        self.color = new_color
    
    @classmethod
    def get_no_of_obj(cls):
        return f'The total number of car objects created: {cls.no_of_obj}'
    
    @classmethod
    def change_no_of_obj(cls, val):
        cls.no_of_obj = val
        return f'The total number of car objects created: {val}'

car1 = Car('BMW', 'black', 5000000, 300)
car2 = Car('Fiat', 'red', 100000, 80)
car3 = Car('Volvo', 'blue', 300000, 180)

# print(car1.brand)
# print(car1.speed)
# car1.get_all_info()
# car2.get_all_info()
# my_text = 'Hello'
# print(type(my_text))

# print(car1.brand)
# car1.change_brand_and_color('Ferrari', 'Yellow')
# print(car1.brand)

# car1.get_all_info()
# print(Car.no_of_obj)
# print(car1.no_of_obj)

# print(Car.get_no_of_obj())

# class Date:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day

#     @classmethod
#     def from_string(cls, date_string):
#         year, month, day = map(int, date_string.split('-'))
#         # date_string.split('-') => ['2023', '07', '16']
#         # [int('2023'), int('07'), int'(16')]
#         # year, month, day = [2023, 07, 16]
#         return cls(year, month, day)
    
#     def instance_me(self):
#         pass
# # Here, from_string is a factory method that creates an instance of the Date class from a string:


# date = Date.from_string('2023-07-16')
# print(date.year, date.month, date.day) 

# print(Car.change_no_of_obj(5))
# print(Car.get_no_of_obj())

car1.brand = 'New_Value'
print(car1.brand)