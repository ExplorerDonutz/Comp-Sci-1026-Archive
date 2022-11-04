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

    # Find best rank
    best = unis[0]

    # Check all elements in array
    for i in range(1, len(unis)):
        # If current element is less than the best, replace best with this element
        if unis[i][3] < best[3]:
            best = unis[i]

    return f"At national rank => {best[3]} the university name is => {best[1]}\n"


def averageScore(reader, selectedCountry):
    unis = []
    for row in reader:
        if row[2].upper() == selectedCountry.upper():
            unis.append(row)

    avg = 0

    for uni in unis:
        avg += float(uni[len(uni) - 1])

    avg /= len(unis)
    return avg


def continentRelativeScore(rankReader, capitalReader, capitalFile, rankFile, avg, selectedCountry):
    countries = []
    continent = ""
    scores = []

    # Find which continent the country is in
    for row in capitalReader:
        if row[0].upper() == selectedCountry.upper():
            continent = row[len(row) - 1]

    capitalFile.seek(1)

    # Find all countries in continent
    for row in capitalReader:
        if row[len(row) - 1] == continent:
            countries.append(row[0])

    rankFile.seek(1)

    # Get all scores from all the countries in the continent
    for row in rankReader:
        for country in countries:
            if row[2] == country:
                scores.append(float(row[len(row) - 1]))

    # Sort by national rank
    best = scores[0]

    # Check all elements in array
    for i in range(1, len(scores)):
        # If current element is greater than the best, replace best with this element
        if scores[i] > best:
            best = scores[i]

    # Add info for the average as well as continent relative score
    return f"The average score => {avg}\n The relative score to the top university in {continent} is => ({avg} / {best}) x 100% = {(avg / best) * 100}%"


def printToOutput(outputInfo):
    with open("output.txt", "w") as file:
        file.write(outputInfo)


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
    capitalFile.seek(1)
    info += continentRelativeScore(rankReader, capitalReader, capitalFile, rankFile, averageScore(rankReader, selectedCountry), selectedCountry)

    printToOutput(info)

    rankFile.close()
    capitalFile.close()
