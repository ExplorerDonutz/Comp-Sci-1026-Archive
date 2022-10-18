# Michael Quick
# 17 October 2022
# Gets user input to create pizza order

from Assign2.pizzaReceipt import generateReceipt

TOPPINGS = ("ONION", "TOMATO", "GREEN PEPPER", "MUSHROOM", "OLIVE", "SPINACH", "BROCCOLI", "PINEAPPLE", "HOT PEPPER", "PEPPERONI", "HAM", "BACON", "GROUND BEEF", "CHICKEN", "SAUSAGE")

ordering = True

begin = input("Do you want to order a pizza? ").lower()

if begin == "q" or begin == "no":
    ordering = False

pizzas = []

# Ordering loop
while ordering:
    choosingSize = True
    size = ""

    # Loop through pizza size prompt until the user gives a valid size
    while choosingSize:
        size = input("Choose a size: S, M, L, or XL: ").upper()

        if size == "S":
            choosingSize = False
        elif size == "M":
            choosingSize = False
        elif size == "L":
            choosingSize = False
        elif size == "XL":
            choosingSize = False

    choosingToppings = True
    # Prompt user for pizza toppings until they have all the toppings they desire
    toppings = []
    while choosingToppings:
        topping = input("Type in one of our toppings to add it to your pizza. To see the list of toppings, enter \n\"LIST\". When you are done adding toppings, enter \"X\"\n").upper()
        if topping == "X":
            choosingToppings = False
        elif topping == "LIST":
            print(TOPPINGS)
        else:
            # Check to see if topping is in list of toppings
            if topping in TOPPINGS:
                # Add topping to topping list
                print(f"Added {topping} to your pizza")
                toppings.append(topping)
            else:
                # Topping wasn't found, so it is invalid
                print("Invalid topping")

    # Create pizza
    pizza = (size, toppings)

    # Add current pizza to list of pizzas being ordered
    pizzas.append(pizza)

    # See if user would like to make another pizza or if they have completed their order
    finished = input("Do you want to continue ordering? ").upper()
    if finished == "Q" or finished == "NO":
        ordering = False
generateReceipt(pizzas)
