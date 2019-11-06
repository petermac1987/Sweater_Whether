# Author: Chris Peterman
# Date: 11/01/2019
# Version: 1.01
# Description: This program will

import json

class Sweater():
    """This program will take an input of temperature and return a True or
    False value based on who the user is, the temperature that they usually
     wear a sweater"""

    # Initializes objects of users entered.
    def __init__(self, username, age, temperature):
        """Take in the name of the user and the temperature"""
        self.person_name = username
        self.person_age = age
        self.temperature_value = temperature
        self.data = {}
        self.data['people'] = []

    def change_temperature(self, amount):
        self.temperature_value = amount

    def sweater_whether(self):
        if self.temperature_value <= 35:
            print(self.person_name + ", you'll need a heavy jacket. It is " + str(self.temperature_value) +
                  " Fahrenheit\n")
        elif self.temperature_value > 35 and self.temperature_value < 50:
            print(self.person_name + ", I would recommend a jacket. It is " + str(self.temperature_value) +
                  " Fahrenheit\n")
        elif self.temperature_value >= 50 and self.temperature_value < 65:
            print(self.person_name + ", I would use a sweater. It is " + str(self.temperature_value) +
                  " Fahrenheit\n")
        elif self.temperature_value >= 65 and self.temperature_value < 70:
            print(self.person_name + ", A very light sweater is recommended. It is " + str(self.temperature_value) +
                  " Fahrenheit\n")
        else:
            print(self.person_name + ",  No, stop asking. It is " + str(self.temperature_value) +
                  " Fahrenheit\n")
    # Write to txt file using JSON.
    # At this point, the biggest issue is not being able to write multiple user data to the file.
    # Every time I call this function it will overwrite the previous persons data.
    def data_write(self):
        self.data['people'].append({
            'name': self.person_name,
            'age': str(self.person_age),
        })

        with open('data.txt', 'w') as outfile:
            json.dump(self.data, outfile)

    # Open user data from data.txt
    def data_open(self):
        with open('data.txt') as json_file:
            data = json.load(json_file)
            for p in data['people']:
                print('Name: ' + p['name'])
                print('Age: ' + p['age'])
                print(' ')