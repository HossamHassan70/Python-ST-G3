# to define function 
def fun_name():
    pass

def summ(num1, num2=0):
    result = int(num1) + int(num2)
    return result

x,y = 7, 9
print(summ(5,'6'))
print(summ(5,7))
print(summ(x,y))
# print(summ(input('Enter first number: '), input('Enter second Number: ')))
# print(summ())
print(summ(1))


#######################
# def displayArgs(*args):
#     # print(type(args))
#     # print(len(args))
#     for item in args:
#         print(f"the argument is {item} and type is {type(item)}")
#     return 
#     print('hello') # not executed because it comes after return

# displayArgs('Hello', 'Hossam', 2025, True)

def fun(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Argument *argv :", arg)

fun('Hello', 'Welcome', 'to', 'iti_S.T')



######################3
# **kwargs
# def fun(**kwargs):
#     print(type(kwargs))
#     for k, val in kwargs.items():
#         print(f"{k}:{val}")

# fun(a=1, b=2, c=3)

def fun(*args, **kwargs):
    print(type(args))
    print("Positional arguments:", args)
    print(type(kwargs))
    print("Keyword arguments:", kwargs)

fun(1, 2, 3, a=4, b=5)