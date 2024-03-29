f = open("rawdata.txt", "r")
incomeDict = {}
countryDict = {}
countryList = []
incomeList = []
initialList = []

for line in f:
    line = line.upper().strip("\n").split(":")
    initialList.append(line[1][0])
    countryList.append(line[1])
    incomeList.append(line[2])

for i in range(0, len(countryList)):
    incomeDict[countryList[i]] = incomeList[i]
    if initialList[i] in countryDict:
        countryDict[initialList[i]].add(countryList[i])
    else:
        countryDict[initialList[i]] = {countryList[i]}

done = False
while not done:
    text = input("Enter an initial or a country name: ")
    text = text.upper()
    if text == "QUIT":
        done = True
    elif text in countryDict:
        print(countryDict[text])
    elif text in incomeDict:
        print(incomeDict[text])
    else:
        print("Does not exist.")

# 3) Identify errors and fix the code.

sentence = "I had such a horrible day It was awful so bad sigh It could not have been worse but actually though it " \
           "was such a terrible horrible awful bad day"

makeItHappy = {"horrible": "amazing", "bad": "good", "awful": "awesome", "worse": "better", "terrible": "great"}

spsentence = sentence.split()
# Change word to i for reading purpose
# Shouldn't have -1
for i in range(0, len(spsentence)):
    if spsentence[i] in makeItHappy:
        # makeItHappy needs the string value from spsentence, not a int value
        spsentence[i] = makeItHappy[spsentence[i]]

newString = ""

for word in spsentence:
    newString = newString + word + " "

print(newString)
