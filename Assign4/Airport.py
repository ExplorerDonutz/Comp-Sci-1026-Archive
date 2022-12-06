class Airport:
    def __init__(self, code, city, country):
        self.code = code
        self.city = city
        self.country = country

    def __repr__(self):
        # Return all the information about this airport
        return f"{self.code} ({self.city}, {self.country})"

    def getCode(self):
        return self.code

    def getCity(self):
        return self.city

    def getCountry(self):
        return self.country

    def setCity(self, city):
        self.city = city

    def setCountry(self, country):
        self.country = country
