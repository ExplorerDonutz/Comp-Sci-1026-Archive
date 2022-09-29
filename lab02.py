# 1) Write code
age = int(input("Enter your age: "))
if age >= 9:
    height = float(input("Enter your height in cm: "))
    if height > 130:
        print("You may go on this ride!")
    else:
        print("YOu are too short for this ride.")
else:
    print("You are too young for this ride.")

# 2) Fix bugs in code

IDEAL_CREDIT_SCORE = 720

userScore = int(input("Please enter your credit score: "))
housePrice = int(input("Please enter the price of the house: "))

# => should be >=
if userScore >= IDEAL_CREDIT_SCORE:
    downPayment = 0.1 * housePrice
# else if should be elif & "600" should be 600
elif userScore < IDEAL_CREDIT_SCORE and userScore > 600:
    downPayment = 0.2 * housePrice
else:
    # Anything inside else statement must be indented
    downPayment = 0.3 * housePrice
print("Your down payment is: ${}".format(downPayment))
