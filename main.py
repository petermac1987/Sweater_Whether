# Author: Chris Peterman
# Date: 11/01/2019
# Version: 1.01
# Description: This program will

class Sweater():
    """This program will take an input of temperature and return a True or
    False value based on who the user is, the temperature that they usually
     wear a sweater"""

    def __init__(self, username, temperature):
        """Take in the name of the user and the temperature"""
        self.person_name = username
        self.temperature_value = temperature

    def change_temperature(self, amount):
        self.temperature_value = amount

    def sweater_whether(self):
        if self.person_name.lower() == "ricky":
            print("Ricky's a loser.")
            return
        elif self.temperature_value <= 35:
            print(self.person_name + ", you'll need a heavy jacket. It is " + str(self.temperature_value) +
                  " Fahrenheit\n")
        elif self.temperature_value > 35 and self.temperature_value < 50:
            print(self.person_name + ", I would recommend a jacket. It is " + str(self.temperature_value) +
                  " Fahrenheit\n")
        elif self.temperature_value >= 50 and self.temperature_value < 65:
            print(self.person_name + ", I would use a sweater. It is " + str(self.temperature_value) + " Fahrenheit\n")
        elif self.temperature_value >= 65 and self.temperature_value < 70:
            print(self.person_name + ", A very light sweater is recommended. It is " + str(self.temperature_value) +
                  " Fahrenheit\n")
        else:
            print(self.person_name + ",  No, stop asking. It is " + str(self.temperature_value) + " Fahrenheit\n")