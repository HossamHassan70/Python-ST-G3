import re
import json
our_file = 'users.txt'



def validate_email(email):
    pattern = r'^[A-Za-z0-9\._]+@[A-Za-z\.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def register_user(fname, lname, em, pas, con_pas):
    if not all([fname, lname, em, pas, con_pas]):
        print('All Fields are required! ')
        return False
    if fname and not fname.strip():
        print('First Name cannot be empty! ')
        return False
    if lname and not lname.strip():
        print('Last Name cannot be empty! ')
        return False
    if em and not validate_email(em):
        print('Invalid Email Format!')
        return False
    if pas and len(pas) < 8:
        print('Password Must be at least 8 characters')
        return False
    if pas != con_pas:
        print('Password Not match')
        return False
    
    user_data = {
        'first_name': fname.strip(),
        'last_name': lname.strip(),
        'email': em.lower().strip(),
        'password': pas
    }
    try:
        with open(our_file, 'a') as file:
            file.write(json.dumps(user_data) + "\n")
        return True
    except:
        print('Error with saving user data!') 
        return False
    
while True:
    print('Welcome In Our Website')
    print('1. Register')
    print('2. Login')
    print('3. Exit')
    choice = input("\nSelect your option (1-3): ")
    if choice == '1':
        print('\n===User Registration===')
        first_name = input('Enter Your First Name: ')
        last_name = input('Enter Your Last Name: ')
        email = input('Enter Your Email: ')
        password = input('Enter Your Password: ')
        confirm_password = input('Confirm Your Password: ')
        
        success = register_user(first_name, last_name, email, password, confirm_password)
        if success:
            print('Registration Successfully! 👌')
        else:
            print('Registration Failed! Something happened Wrong!')
    elif choice == '2':
        pass
    elif choice == '3':
        print('\nGoodbye!')
        break
    else:
        print('Invalid Input you should type from these values (1,2,3)')
        