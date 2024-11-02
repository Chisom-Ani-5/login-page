import sys
from flask import Flask, render_template

app = Flask(__name__)

Info = {}

def SignUp() :
    global Info
    Username = input('Enter username: ')
    Email_address = input('Enter email address: ')
    Password = input('Enter your password: ')


    Info[Username] = {
    'Username' : Username, 
    'Email address' : Email_address, 
    'Password' : Password
    }

def ConfirmInfo() :
    global Info
    print('User Information: ')
    for username, data in Info.items():
        print(f'Username: {data['Username']}')
        print(f'Email address: {data['Email address']}')
        print(f'Password: {data['Password']}')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__' :

    while True :
        print('1. Sign up')
        print('2. Confirm Info')
        print('3. Exit')

        Choice = int(input('What would you like to do? : '))

        if Choice == 1 :
            SignUp()

        elif Choice == 2 :
            ConfirmInfo()

        elif Choice == 3 :
            sys.exit(0)

        else :
            print('Invalid choice. Please chose again')

