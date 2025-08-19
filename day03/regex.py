import re
# []	A set of characters	"[a-m]"	
# \	Signals a special sequence (can also be used to escape special characters)	"\d"	
# .	Any character (except newline character)	"he..o"	
# ^	Starts with	                                        "^hello"	
# $	Ends with	                                        "planet$"	
# *	Zero or more occurrences	                        "he.*o"	
# +	One or more occurrences	                            "he.+o"	
# ?	Zero or one occurrences	                            "he.?o"	
# {}	Exactly the specified number of occurrences	    "he.{2}o"	
# |	Either or	                                        "falls|stays"	
# () Capture and group
##############################################333
# name = input('Enter your Name: ')
email = input('Enter your Email: ')
pattern = r"^[A-Za-z0-9\.\+_-]+@[A-Za-z]+\.[a-zA-Z]*$"
# print(re.match(pattern, email))
# if not re.match(pattern, email):
#     print('Please Enter a valid email')
if re.match(pattern, email) is None:
    print('Please Enter a valid email')
    