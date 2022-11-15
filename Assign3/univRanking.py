# Michael Quick
# 05 November 2022
# Reads university information from csv file and display the extracted information

import csv
import time


def getUniversitiesAndCountries(reader):
    uniCount = 0
    countries = ""

    for row in reader:
        uniCount += 1
        # Add the country to the string only if it has not been added yet
        if row[2] not in countries:
            countries += row[2] + ", "

    return f"Total number of universities => {uniCount}\nAvailable countries => {countries}\n"


def getContinents(reader):
    continents = ""
    for row in reader:
        # Add the continent to the string only if it has not been added yet
        if row[len(row) - 1] not in continents:
            continents += row[len(row) - 1] + ", "

    return f"Available continents => {continents}\n"


def internationalRank(reader, selectedCountry):
    universities = []

    for row in reader:
        # If university is located in the selected country, add it to the list
        if row[2].upper() == selectedCountry.upper():
            universities.append(row)

    # File is already sorted by rank, so we can just assume the first university has the best rank
    return f"At international rank => {universities[0][0]} the university name is => {universities[0][1].upper()}\n"


def nationalRank(reader, selectedCountry):
    unis = []
    for row in reader:
        if row[2].upper() == selectedCountry.upper():
            unis.append(row)

    # Find best rank
    best = unis[0]

    # Check all ranks in list
    for i in range(1, len(unis)):
        # If current rank is better (less than) than the best, replace best with this rank
        if unis[i][3] < best[3]:
            best = unis[i]

    return f"At national rank => {best[3]} the university name is => {best[1].upper()}\n"


def averageScore(reader, selectedCountry):
    unis = []
    for row in reader:
        # If university is located in the selected country, add it to the list
        if row[2].upper() == selectedCountry.upper():
            unis.append(row)

    avg = 0

    for uni in unis:
        # Add score of each university to average
        avg += float(uni[len(uni) - 1])

    avg /= len(unis)

    # Return rounded to 2 digits
    return round(avg, 2)


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

    # Check all scores in array
    for i in range(1, len(scores)):
        # If current score is greater than the best, replace best with this score
        if scores[i] > best:
            best = scores[i]

    # Add info for the average as well as continent relative score
    return f"The average score => {avg}%\nThe relative score to the top university in {continent.upper()} is => ({avg} / {best:0.2f}) x 100% = {(avg / best) * 100:0.2f}%\n"


def capitalCity(capitalReader, selectedCountry):
    capital = ""

    # Search each row for the selected country's capital
    for row in capitalReader:
        if row[0].upper() == selectedCountry.upper():
            capital = row[1]
            # The capital is found so the loop can stop
            break
    # Return the capital for use in capitalUniversities
    return capital


def capitalUniversities(rankReader, capital):
    unis = []
    info = f"The capital is => {capital.upper()}\n"
    for row in rankReader:
        # If the university contains the capital, add it to the list
        if capital in row[1]:
            unis.append(row[1])

    info += "The universities that contain the capital name =>\n"

    # Use i for numbering and add all capital universities to the info string
    for i in range(len(unis)):
        info += f"#{i + 1} {unis[i].upper()}\n"

    return info


def printToOutput(outputInfo):
    with open("output.txt", "w") as file:
        # Write all the information to the output file
        file.write(outputInfo)


def getInformation(selectedCountry, rankingFileName, capitalsFileName):
    # Create blank string that will hold all the information to be written
    info = ""

    rankFile = open(rankingFileName)
    rankReader = csv.reader(rankFile)
    # Skip heading
    next(rankReader)
    info += getUniversitiesAndCountries(rankReader)

    capitalFile = open(capitalsFileName)
    capitalReader = csv.reader(capitalFile)
    info += getContinents(capitalReader)

    # Return to top (below heading)
    rankFile.seek(1)
    info += internationalRank(rankReader, selectedCountry)
    rankFile.seek(1)
    info += nationalRank(rankReader, selectedCountry)

    rankFile.seek(1)
    capitalFile.seek(1)
    info += continentRelativeScore(rankReader, capitalReader, capitalFile, rankFile,
                                   averageScore(rankReader, selectedCountry), selectedCountry)

    capitalFile.seek(1)
    rankFile.seek(1)
    info += capitalUniversities(rankReader, capitalCity(capitalReader, selectedCountry))

    printToOutput(info)

    # Close the files
    rankFile.close()
    capitalFile.close()
