name = 'Hossam'
work = "Information Technology Institute"

print(len(name), len(work)) # 6 32 
# name[start:end(not included):step]
# slicing
print(name[1:3]) # os
print(work[0:7]) # Informa
print(work[0:7:2]) # Ifra
print(work[4:]) # rmation Technology Institute
print(work[:10]) # Informatio
print(work[-1]) # e
print(work[15:-1]) # hnology Institut

print(name.count('s')) # 2
print('this is a normal string'.capitalize()) # This is a normal string
print(work.find('o'))
txt = "For only {price:.2f} dollars!, For {days}!"
print(txt.format(price = 50, days = 2))
print(f"This is {name} work in {work}")
print(name.upper())
print(name.isupper())
print(name.lower())
print(name.islower())

new_name = '              hossam        '
print(new_name)
print(new_name.strip())
print(new_name.lstrip())
print(new_name.rstrip())
print((name + ' ') * 3)
print(work.replace('o', '*')) # Inf*rmati*n Techn*l*gy Institute
x = "10"
# check the value inside the string is digit
print(x.isdigit()) # True
