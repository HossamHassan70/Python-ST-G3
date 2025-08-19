name = 'Ahmed' # global scope 


# def outerFn():
    # name is local scope for outerFu
    # name = "Ali" # the name variable make append by the new value 
    
#     def innerFn():
#         print(name)
#     innerFn()

# outerFn()
#######################################3
# def outer_fun():
#     # print(name) # UnboundLocalError: cannot access local variable 'name' where it is not associated with a value
#     name = 'Omnia'
#     def innerFn():
#         print(name)
#         # my_name = 'Basmala'
#     innerFn()
#     # print(my_name) # NameError: name 'my_name' is not defined

# outer_fun()
# print(name)
###########################################3
# def outer_fun():
#     # print(name) # UnboundLocalError: cannot access local variable 'name' where it is not associated with a value
#     global name
#     name = 'Omnia'
#     def innerFn():
#         print(name)
#         # my_name = 'Basmala'
#     innerFn()
#     # print(my_name) # NameError: name 'my_name' is not defined

# outer_fun()
# print(name)
# ####################################33

# def outer_fun():
#     # print(name) # UnboundLocalError: cannot access local variable 'name' where it is not associated with a value
#     global new_name
#     new_name = 'Mahmoud'
#     name = 'Omnia'
#     local_name = 'Omar'
#     def innerFn():
#         print(name)
#         # my_name = 'Basmala'
#     innerFn()
#     # print(my_name) # NameError: name 'my_name' is not defined

# outer_fun()
# print(name)
# # print(local_name) # NameError: name 'local_name' is not defined
# print(new_name)

###########################################3

# def outer():
#     # a is local for outer()
#     a = 5
#     b = 4
#     def inner():
#         nonlocal a # a is nonlocal for inner(), so it will be global for outer()
#         a = 10
#         print(b) # 4
#         def in_inner():
#             nonlocal b
#             b = 7
#         in_inner()
#     print(b) # 4
#     inner()
#     print(b) # 7
#     print(a)
    
# outer()
# print(a) # NameError: name 'a' is not defined
#################################################33
# a = 7 # Global scope
# def outer():
#     # a = 5 # Local Scope 
    
#     print(a) # 5 7

#     def inner():
#         global a
#         a = 10
#         print(a) # 10
#     inner()
#     print(a) # 5

# outer()
# print(a) # 7