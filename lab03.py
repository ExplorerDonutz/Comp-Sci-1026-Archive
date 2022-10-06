n = int(input("How many numbers do you want to use today? "))
if n > 0:
    firstValue = int(input("Enter the first number: "))
    largest = firstValue
    smallest = firstValue
    total = firstValue

    counter = 0
    while counter < (n-1):
        current = int(input("Enter the next number: "))
        total = total+current
        counter = counter+1
        if current < smallest:
            smallest = current
        elif current > largest:
            largest = current
    print("The average of the values is: ", total/n)
    print("The smallest of the values is {}".format(smallest))
    print("The largest of the values is {}".format(largest))
    print("The range of the values is {}".format(largest-smallest))
else:
    print("You did not want to use any numbers today.")

accountTotal = 50
# Should be >=, not =<
while accountTotal >= 20:
    print(accountTotal)
    # Needs to take 1 away each loop
    accountTotal -= 1

print("Your account has reached $20")
