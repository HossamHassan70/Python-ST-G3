# 1. List items are ordered (starts from 0)
# 2. To create list we should use []
# 3. List can contain duplicate items
# 4. List in Python are Mutable (Modify or Delete items)
# 5. List in python could contain different datatypes 


my_list = [14, 10, 'Mohamed', True, 10, 'ol', 'ol']
print(my_list)
print(my_list[0])
my_list[1] = 15
print(my_list[1])
my_list.append(44)
print(my_list)
my_list.append([4,5,True,'Omnia'])
print(my_list)
print(my_list[len(my_list)-1][3])
print(my_list[-1][3])

cleared_list = [1, 2, 4, 'Ahmed', False]
print(cleared_list)
cleared_list.clear()
print(cleared_list)

print(my_list.count('ol'))
sec_list = [5, 6, 7, 8, 9]

my_list.extend(sec_list)
print(my_list)
fruits = ['apple', 'banana', 'cherry', 'banana']

fruits.insert(1, "orange")
print(fruits)
print(fruits.index("cherry")) # returns the position at the first occurrence 
poped_element = fruits.pop(1)
print(fruits)
fruits.remove("banana") # removes the first occurrence
print(fruits)
fruits.reverse()
print(fruits)


cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# Concatenation
print(my_list + fruits)

# in operator
l4 = ['Python', 'Minya', 'c#']
print('Mohamed' in l4)
nums = [1, 2, 3, 4]
for i in nums:
    print(i * 2)
    
x = [5,66,77]
print(min(x))
print(max(x))

