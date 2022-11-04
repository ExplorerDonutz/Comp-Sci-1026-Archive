# Michael Quick
# 26 October 2022
# Reads university information from csv file and display the extracted information

import csv

RANK_FILE = 'TopUni.csv'
CAPITAL_FILE = 'capitals.csv'


def getUniversitiesAndCountries(reader):
    # Start at -1 to skip the heading
    uniCount = -1
    countries = ""

    for row in reader:
        uniCount += 1
        if row[2] not in countries:
            countries += row[2] + ", "

    return f"Total number of universities => {uniCount}\nAvailable countries => {countries}\n"


def getContinents(reader):
    continents = ""
    for row in reader:
        if row[len(row) - 1] not in continents:
            continents += row[len(row) - 1] + ", "

    return f"Available continents => {continents}\n"


def internationalRank(reader, selectedCountry):
    universities = []

    for row in reader:
        if row[2].upper() == selectedCountry.upper():
            universities.append(row)

    # File is already sorted by rank so we can just assume the first element has the best rank
    return f"At international rank => {universities[0][0]} the university name is => {universities[0][1]}\n"


def nationalRank(reader, selectedCountry):
    unis = []
    for row in reader:
        if row[2].upper() == selectedCountry.upper():
            unis.append(row)

    # Sort by national rank
    swapped = False
    # Check all elements in array
    for i in range(len(unis) - 1):
        for j in range(0, len(unis) - i - 1):
            # Swap if the element is greater than the next element
            if unis[j][3] > unis[j + 1][3]:
                swapped = True
                unis[j], unis[j + 1] = unis[j + 1], unis[j]
        if not swapped:
            # No swaps, exit the for loop
            return

    return f"At national rank => {unis[0][3]} the university name is => {unis[0][1]}\n"


def averageScore(reader, selectedCountry):
    unis = []
    for row in reader:
        if row[2].upper() == selectedCountry.upper():
            unis.append(row)

    avg = 0

    for uni in unis:
        avg += float(uni[len(uni) - 1])

    avg /= len(unis)
    return f"The average score => {avg}\n"


def printToOutput(outputInfo):
    with open("output.txt", "w") as file:
        file.write(outputInfo)


# Open TopUni file and sort information
def getInformation(selectedCountry, rankingFileName, capitalsFileName):
    info = ""

    # Open
    rankFile = open(rankingFileName)
    rankReader = csv.reader(rankFile)
    rankFile.seek(1)
    info += getUniversitiesAndCountries(rankReader)

    capitalFile = open(capitalsFileName)
    capitalReader = csv.reader(capitalFile)
    info += getContinents(capitalReader)

    rankFile.seek(1)
    info += internationalRank(rankReader, selectedCountry)
    rankFile.seek(1)
    info += nationalRank(rankReader, selectedCountry)
    rankFile.seek(1)
    info += averageScore(rankReader, selectedCountry)

    printToOutput(info)

    rankFile.close()
    capitalFile.close()
