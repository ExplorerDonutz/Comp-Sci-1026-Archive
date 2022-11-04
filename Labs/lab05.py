def numbers():
    nums = []
    while len(nums) < 10:
        nums.append(input("Please enter a number "))
    return nums


def firstLast(strings):
    total = 0
    for word in strings:
        if word[0] == word[len(word) - 1] and len(word) > 1:
            total += 1
    return total


def zFirst(words):
    zresult = []
    result = []
    for word in words:
        if word.lower()[0] == 'z':
            # Begins wh a z
            zresult.append(word)
        else:
            # Doesn't begin with z
            result.append(word)
    zresult.sort()
    result.sort()
    return zresult + result


words = ["hello", "good", "nice", "as", "at", "baseball", "absorb", "sword", "a", "tall", "so", "bored", "silver", "hi",
         "pool", "we", "am", "seven", "do", "you", "want" "ants", "because", "that's", "how", "you", "get", "zebra",
         "zealot", "zoo", "xylophone", "asparagus"]

print(numbers())

print(firstLast(["bob", "home", "pizza", "wow", "i", "party", "101", "22"]))

# Print result of using zFirst
print(zFirst(words))

values = [1, 2, 3, 4, 5]
# Need to use [:] to copy
newValues = values[:]

# Should not be len + 1, out of range
for i in range(len(values)):
    # Should add to newValues, not values

    newValues[i] += 1
    # Should use values not newValues
    print("Old Value at index {} is: {} ".format(i, values[i]))
    print("New Value at index {} is: {} \n".format(i, newValues[i]))
