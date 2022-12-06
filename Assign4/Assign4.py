# Michael Quick
# 06 December 2022
# Loads data from airport and flight files and returns information from them

from Flight import *
from Airport import *


def loadData(aFile, fFile):
    try:
        airportFile = open(aFile)
        flightFile = open(fFile)
    except IOError:
        # Something has gone wrong while loading the files
        return False

    # Get data from airport file
    for line in airportFile:
        strings = line.split(",")

        # Strip any whitespace
        for i in range(len(strings)):
            strings[i] = strings[i].strip()

        # Create a new airport and add it to the list
        allAirports.append(Airport(strings[0], strings[2], strings[1]))

    # Get data from flight file
    flights = []
    origin = Airport("", "", "")
    destination = Airport("", "", "")
    for line in flightFile:
        strings = line.split(",")

        # Strip any whitespace
        for i in range(len(strings)):
            strings[i] = strings[i].strip()
        for a in allAirports:
            if a.getCode() == strings[1]:
                origin = a
            elif a.getCode() == strings[2]:
                destination = a
        flights.append(Flight(strings[0], origin, destination))

    for i in range(0, len(flights)):
        if flights[i].getOrigin().getCode() in allFlights:
            # Flight code is already in dictionary, so add a new value to it
            allFlights[flights[i].getOrigin().getCode()].append(flights[i])
        else:
            # Flight code was not in dictionary, add it and its first value
            allFlights[flights[i].getOrigin().getCode()] = [flights[i]]

    # Close the files
    airportFile.close()
    flightFile.close()
    return True


def getAirportByCode(code):
    for a in allAirports:
        if a.getCode() == code:
            return a
    return -1


def findAllCityFlights(city):
    flights = []
    for code in allFlights:
        for flight in allFlights[code]:
            # Check if either the origin OR destination cities are the inputted city
            if flight.getOrigin().getCity() == city or flight.getDestination().getCity() == city:
                flights.append(flight)
    if not flights:
        return -1
    return flights


def findAllCountryFlights(country):
    flights = []
    for code in allFlights:

        # Check if either the origin, or destination, or both countries are the inputted country
        for flight in allFlights[code]:
            if flight.getOrigin().getCountry == country and flight.getDestination().getCountry() == country:
                flights.append(flight)
            elif flight.getDestination().getCountry() == country:
                flights.append(flight)
            elif flight.getOrigin().getCountry() == country:
                flights.append(flight)

    if not flights:
        return -1
    return flights


def findFlightBetween(origAirport, destAirport):
    singleHop = set()

    # Check all flights going from origAirport
    for flight in allFlights[origAirport.getCode()]:
        # If the destination is destAirport then it is a direct flight
        if flight.getDestination().getCode() == destAirport.getCode():
            return f"Direct Flight: {origAirport.getCode()} to {destAirport.getCode()}"
        # Check all flights going from the destination of flight
        for hop in allFlights[flight.getDestination().getCode()]:
            # If the destination of the flight is destAirport then it is a single hop flight
            if hop.getDestination().getCode() == destAirport.getCode():
                singleHop.add(flight.getDestination().getCode())
    if len(singleHop) == 0:
        return -1
    else:
        return singleHop


def findReturnFlight(firstFlight):
    for flight in allFlights[firstFlight.getDestination().getCode()]:
        # Check if the flight reversed exists (origin is now destination and vice versa)
        if flight.getDestination() == firstFlight.getOrigin():
            return flight
    return -1


# Create the empty list and dictionary for airports and flights
allAirports = []
allFlights = {}
