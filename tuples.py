# 1. Tuple items are ordered (starts from 0)
# 2. To create list we should use ()
# 3. Tuple can contain duplicate items
# 4. Tuple in Python are Immutable (Can't Modify or Delete items)
# 5. Tuple in python could contain different datatypes 



t = (1, 2, 3)
my_tt = tuple([2, 4, 6])

# print(t)
# print(my_tt)
my_t = (14, 10, 'Mohamed', True, 10, 'ol', 'ol')
print(my_t)
print(len(my_t))

print(my_t[0])
print(my_t[1:4])
print(my_t.count('ol'))
fruits = ('apple', 'banana', 'cherry', 'banana', 'cherry')
print(fruits.index("cherry")) # returns the position at the first occurrence 


l = [1]
print(type(l))
# t1 = tuple('iti')
# t1 = ('iti', )
t1 = 'iti',
print(type(t1))

# Concatenation
my_new_t = my_t + fruits
print(my_new_t)
print(my_t + fruits)

# if 'o' in 'Hello':
#     print('o char is in the string')
# else:
#     print('o is not in the string')

# txt = 'Hello in our community'
# if 'i' in txt:
#     print('i char is in the string')
# else:
#     print('o is not in the string')

# if 'ol' in my_t:
#     print('ol Member is attend')

x = (5,66,77)
print(min(x))
print(max(x))

t = () # falsy value
if t:
    print("Non empty tuple")
else:
    print("Empty tuple ")
