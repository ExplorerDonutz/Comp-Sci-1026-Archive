def factorial(n):
    result = n
    for i in range(n - 1, 0, -1):
        result = result * i
    return result


def helloWorld():
    print("Hello World")


def helloWorldNTimes(n):
    for i in range(n):
        helloWorld()


def countVowels(word):
    # Should be 0 not 1
    numVowels = 0
    # Should be word not string
    for letter in word:
        # Should set letter to lower
        if letter.lower() in "aeiou":
            numVowels += 1
            # Should return numVowels, not letter
    return numVowels


def main():
    print("5! = {}".format(factorial(5)))
    helloWorldNTimes(2)
    helloWorldNTimes(1)
    helloWorldNTimes(3)
    helloWorldNTimes(2)
    print(countVowels("AEIOu"))


main()
