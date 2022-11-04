# Michael Quick
# 26 October 2022
# Reads university information from csv file and display the extracted information

import csv

RANK_FILE = 'TopUni.csv'
CAPITAL_FILE = 'capitals.csv'


def getUniversitiesAndCountries(reader):
    uniCount = 0
    countries = ""

    for row in reader:
        uniCount += 1
        if row[2] not in countries:
            countries += row[2] + ", "

    return f"Total number of universities => {uniCount}\nAvailable countries => {countries}\nAvailable continents => {continents}"


def getContinents(reader):
    continents = ""
    for row in reader:
        if row[len(row) - 1] not in continents:
            continents += row[len(row) - 1] + ", "


def printToOutput(outputInfo):
    with open("output.txt", "w") as file:
        file.write(outputInfo)


# Open TopUni file and sort information
def getInformation(selectedCountry, rankingFileName, capitalsFileName):
    info = ""

    # Open
    with open(rankingFileName) as file:
        reader = csv.reader(file)
        info += getUniversitiesAndCountries(reader)

    # Skip first row
    next(reader)

    with open(capitalsFileName) as file:
        reader = csv.reader(file)
