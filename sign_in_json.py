import json
# ask if they want to signin or create acount
# take an input for username
# see if username is in database
# if it is ask for password, in while loop 3 tries
# if username isnt then make username and password and store it to data base

def create_new_user(username, password):
    """creates new entry into database"""
    try:
        with open('users.json', 'r') as f:
            database = json.load(f)
    except FileNotFoundError:
        with open('users.json', 'w') as f:
            print('new user database was created')
        database = {username:password}
    else:
        database[username] = password
    with open('users.json', 'w') as f:
        json.dump(database, f)

def sign_in():
    """prompts user for username then password then trys to sign in"""
    username = input('Enter username: ')
    count = 0
    try:
        with open('users.json') as f:
            database = json.load(f)
    except FileNotFoundError:
        print('no user database please create a user first')
        quit() 
    
    while True:
        if username in database:
            password = input('Enter password: ')
            while count < 2:
                if database[username] == password:
                    print('You have succesfully signed in') 
                    break
                else:
                    count += 1
                    password = input('Enter password: ')
            if count > 3:
                print('login failed')
            break
        else:
            print('cannot find username')
            username = input('Enter username: ')


# intro and intial choice between signing in and creating an account
print("\nIf you want to sign-in to an existing account enter 's'\nIf you want to create account enter 'c'\n")
user_choice = input('Type here: ')
while True:
    if user_choice == 'c' or user_choice == 's': 
        break
    user_choice = input('Type here: ')


if user_choice == 'c':
    username = input('Enter username: ')
    password = input('Enter password: ')
    create_new_user(username, password)
    print('Your account has been created, thank you!')
else:
    sign_in()
