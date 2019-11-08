class Sweater():
    """This program will take an input of temperature and return a True or
    False value based on who the user is, the temperature that they usually
     wear a sweater"""

    # Initializes objects of users entered.
    def __init__(self, username,  temperature):
        """Take in the name of the user and the temperature"""
        self.person_name = username
        self.temperature_value = temperature

    def change_temperature(self, amount):
        """Changes temperature to value entered"""
        self.temperature_value = amount

    def sweater_whether(self):
        """Compares temperature value to set values and returns a response."""
        if self.temperature_value <= 34:
            return(self.person_name + ", you'll need a heavy jacket. It is " + str(self.temperature_value) +
                  " Fahrenheit")
        elif self.temperature_value in range(35, 49):
            return(self.person_name + ", I would recommend a jacket. It is " + str(self.temperature_value) +
                  " Fahrenheit")
        elif self.temperature_value in range(50, 65):
            return(self.person_name + ", I would use a sweater. It is " + str(self.temperature_value) +
                  " Fahrenheit")
        elif self.temperature_value in range(65, 70):
            return(self.person_name + ", A very light sweater is recommended. It is " + str(self.temperature_value) +
                  " Fahrenheit")
        else:
            return(self.person_name + ",  It is way too warm, no sweater unless you hail from the desert. It is " +
                  str(self.temperature_value) + " Fahrenheit")
