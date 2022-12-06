import Airport


class Flight:
    def __init__(self, flightNo, origin, destination):
        # Check if both origin and destination are airport objects
        if isinstance(origin, Airport.Airport) and isinstance(destination, Airport.Airport):
            self.flightNo = flightNo
            self.origin = origin
            self.destination = destination
        else:
            raise TypeError("The origin and destination must be Airport objects")

    def __repr__(self):
        if self.isDomesticFlight():
            return f"Flight: {self.flightNo} from {self.origin.getCity()} to {self.destination.getCity()} ""{domestic}"
        return f"Flight: {self.flightNo} from {self.origin.getCity()} to {self.destination.getCity()} ""{international}"

    def __eq__(self, other):
        # Check if other is also a flight object
        if isinstance(other, Flight):
            # If the origin airports and destination airports are equal, then they are the same flights
            if self.origin == other.origin and self.destination == other.destination:
                return True
        return False

    def getFlightNumber(self):
        return self.flightNo

    def getOrigin(self):
        return self.origin

    def getDestination(self):
        return self.destination

    def isDomesticFlight(self):
        if self.origin.getCountry() == self.destination.getCountry():
            return True
        return False

    def setOrigin(self, origin):
        self.origin = origin

    def setDestination(self, destination):
        self.destination = destination
