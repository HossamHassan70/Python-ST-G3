# 1. Sets are used to store multiple items in a single variable.
# 2. A set is a collection which is unordered => No indexes
# 3. Sets are unchangeable (Immutable)
# 4. Sets are didn't not allow duplicate values.
# True and 1 is considered the same value:
# False and 0 is considered the same value:

my_set = {"apple", "banana", "cherry", "apple", 1, True, False, 0, 10, 5.4}
set1 = set(("apple", "banana", "cherry"))

print(my_set)
print(len(my_set))

print(type(my_set))
print(set1)