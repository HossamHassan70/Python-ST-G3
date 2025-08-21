import psycopg2
import re
from getpass import getpass

conn = psycopg2.connect(
    dbname='py_track',
    user= 'postgres',
    password= 'super',
    host= 'localhost',
    port= 5432
)
cur = conn.cursor()


def validate_email(email):
    pattern = r'^[A-Za-z0-9\._]+@[A-Za-z\.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def register_user(name, em, pas, con_pas):
    try:
        if not all([name.strip(), em.strip(), pas, con_pas]):
            print('All Fields are required! ')
            return False
        if not validate_email(em):
            print('Invalid Email Format!')
            return False
        if pas and len(pas) < 8:
            print('Password Must be at least 8 characters')
            return False
        if pas != con_pas:
            print('Password Not match')
            return False
        # check if the email is already exist
        check_query = 'select email from user_data where email = %s'
        cur.execute(check_query, (em,))
        if cur.fetchone():
            print('Email is Already Registered! you can login')
            return False
        insert_query = 'insert into user_data (name, email, password) values(%s, %s, %s)'
        cur.execute(insert_query, (name, em, pas))
        conn.commit()
        print('Registration Successfully! 👌')
        return True
    except psycopg2.Error as err:
        print(f'Database error: {err}')
        conn.rollback()
        return False

def login_user(em, pwd):
    if not em.strip() or not pwd.strip():
        print('Email and password are required!')
        return False
    select_query = 'select email, password from user_data where email = %s and password = %s'
    cur.execute(select_query, (em, pwd))
    row = cur.fetchone()
    if row is not None:
        print('Login Successfully ⭐\n')
        # print(row)
        return True
    else:
        print('Invalid email or password!')
        return False

try:
    print('=' * 30)
    print('Welcome to Our website')
    print('=' * 30)
    
    while True:
        print('\nChoose the operation you want to do: ')
        print('1. Register')
        print('2. Login')
        print('3. Exit')
        choice = input("\nSelect your option (1-3): ")
        if choice == '1':
            print('\n===User Registration===')
            name = input('Enter Your First Name: ')
            email = input('Enter Your Email: ')
            password = getpass('Enter Your Password: ')
            confirm_password = getpass('Confirm Your Password: ')
            
            register_user(name, email, password, confirm_password)
        elif choice == '2':
            print('\n===User Login===')
            email = input('Enter Your Email: ')
            password = getpass('Enter Your Password: ')
            
            login_user(email, password)
            
        elif choice == '3':
            print('\nGoodbye!')
            break
        else:
            print('Invalid Input you should type from these values (1,2,3)')
        
except:
    pass