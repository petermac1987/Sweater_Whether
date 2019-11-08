# Author: Chris Peterman
# Date: 11/01/2019
# Version: 2.0
# Description: This program will

from user_input import Sweater

# Welcome message
print("Hello, welcome to Sweater Whether.")
print("This app will take the temperature today and suggest on \'Whether\' you should wear a sweater.")

# User inputs
print("What is your name? ")
username = input("> ")
print("What is the temperature?")
temperature = int(input("> "))

# Auto output of initial values
response = Sweater(username, temperature)
print(response.sweater_whether())

# Change the temperature value in the program.
while True:
    print("\nWould you like to change the temperature? y/n")
    decision = input("> ")
    if decision.lower() == 'n':
        print("Good bye!")
        break
    elif decision.lower() == 'y':
        print("What is the new temperature?")
        temperature = int(input("> "))
        print(response.sweater_whether())
    else:
        print("Invalid input")