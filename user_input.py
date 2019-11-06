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

    # Change the value of the temperature, only replaces the value does not add to it.
    # If possible, look in to API that would give daily weather to populate for user.
    # Thereby bypassing the need for user to enter data.
    def change_temperature(self, amount):
        self.temperature_value = amount

    # Current iteration of weather response. You will put in the current temperature and then it will pick a response.
    # Ultimate goal is having this be individualized bases on when the user picks sweater, jacket, or t-shirt.
    # Then the user will enter their name and a pin(symbols to prevent use of actual user pins)
    # This will pull the user data and adjust with user inputs. (Most likely a picture symbol for each type)
    # Possibly it will check the range of the values stored in each type per individual and check the range of those
    # values to pick the correct response.
    def sweater_whether(self):
        if self.temperature_value <= 34:
            print(self.person_name + ", you'll need a heavy jacket. It is " + str(self.temperature_value) +
                  " Fahrenheit\n")
        elif self.temperature_value in range(35, 49):
            print(self.person_name + ", I would recommend a jacket. It is " + str(self.temperature_value) +
                  " Fahrenheit\n")
        elif self.temperature_value in range(50, 65):
            print(self.person_name + ", I would use a sweater. It is " + str(self.temperature_value) +
                  " Fahrenheit\n")
        elif self.temperature_value in range(65, 70):
            print(self.person_name + ", A very light sweater is recommended. It is " + str(self.temperature_value) +
                  " Fahrenheit\n")
        else:
            print(self.person_name + ",  No, stop asking. It is " + str(self.temperature_value) +
                  " Fahrenheit\n")
    # I decided to keep this strictly Python for the next few terms. I want this project to showcase my abilities
    # with this language and then another project for an alternate language. Once I'm more comfortable, I would like
    # to research other languages to optimize my projects.