# Michael Quick
# 17 October 2022
# Takes pizza order and creates the receipt

def generateReceipt(pizzaOrder):
    # Blank order
    if len(pizzaOrder) == 0:
        print("You did not order anything")
    else:
        total = 0.00
        items = []
        costs = []

        print("Your order:")

        # Run for loop for each pizza in the order
        for i in range(0, len(pizzaOrder)):
            pizza = pizzaOrder[i]

            # Add cost to cost list based on size
            if pizza[0] == "S":
                costs.append(7.99)
                # Add pizza cost to total
                total += 7.99
            elif pizza[0] == "M":
                costs.append(9.99)
                total += 9.99
            elif pizza[0] == "L":
                costs.append(11.99)
                total += 11.99
            else:
                costs.append(13.99)
                total += 13.99

            # Add pizza to item list
            items.append(f"Pizza {i + 1}: {pizza[0]}")

            # Loop through all the toppings on the current pizza
            toppings = pizza[1]
            for j in range(0, len(toppings)):
                items.append(f"- {toppings[j]}")
                costs.append("")

            # If there are more than 3 toppings, add extra topping charge
            if len(pizza[1]) > 3:
                # Determine how many extra toppings there are
                extraCount = len(pizza[1]) - 3

                # Add charges based on size
                for k in range(0, extraCount):
                    # Add topping charge to item list
                    items.append(f"Extra Topping ({pizza[0]})")

                    if pizza[0] == "S":
                        costs.append(f"{0.50:0.2f}")
                        # Add topping charge to total
                        total += 0.50
                    elif pizza[0] == "M":
                        costs.append(f"{0.75:0.2f}")
                        total += 0.75
                    elif pizza[0] == "L":
                        costs.append(f"{1.00:0.2f}")
                        total += 1.00
                    else:
                        costs.append(f"{1.25:0.2f}")
                        total += 1.25

        # Add tax to item list and cost list
        items.append("Tax:")
        costs.append(f"{total * 0.13:0.2f}")

        # Add tax to total
        total += total * 0.13

        items.append("Total:")
        costs.append(f"{total:0.2f}")

        # Print all items and their costs
        for i in range(0, len(items)):
            print(f"{items[i]:<18}{costs[i]:>13}")
