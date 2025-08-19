# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered
# changeable and do not allow duplicates.
# The values in dictionary items can be of any data type


d = {}
print(type(d))
my_set = {'basmala', 'ahmed'}
age = 20
emp = {
    'name': 'Ahmed',
    'age': age,
    'salary': 5000.54,
    'name': 'Omnia',
    'phones': ['011111111', '0122222222']
}

print(emp['name'])
print(emp['age'])
print(f'The name is {emp["name"]} and age is: {emp["age"]}, and Salary is: {emp["salary"]}')
print(emp)

print(len(emp))

# get keys of dic
print(emp.keys())

# get values of dic
print(emp.values())

print(emp.items())

emp['name'] = 'Mohamed'
print(emp)
print(emp['phones'][0])

##################### 
# update()
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
updated_car = {
    "color": "White",
    "brand": "BMW"
}
print(car)

# The update() method inserts the specified items to the dictionary.
car.update(updated_car)
print(car)

# check key exists in dictionary
if 'name' in emp:
    print('name is exist')
else:
    print('Not exist')

# check values
if "Omnia" in emp.values():
    print("hi")
else:
    print("bye")
    
# loop over the dictionary keys
for item in emp:
    print(f"{item} = {emp[item]}")


for key,value in emp.items(): # list of tuples
    print(f"{key} = {value}")
    
# remove all items in dictionary
# emp.clear()
# print(emp)
###################

# to delete certain dict
# del(car)
# print(car)
