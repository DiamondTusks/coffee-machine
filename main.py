MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

WATER = resources["water"]
MILK = resources["milk"]
COFFEE = resources["coffee"]
MONEY = 0
selection = ""


# TODO 1 user prompt
def prompt():
    return input("What would you like? (espresso, latter, cappuuccino): ").lower()


def report():
    print(f"Water: {WATER}ml")
    print(f"Milk: {MILK}ml")
    print(f"Coffee: {COFFEE}g")
    print(f"Money: ${MONEY}")


machine_on = True
    while machine_on:
        selection = prompt()
    # TODO 2 Turn off the Coffee Machine by entering “off” to the prompt.
        if selection == "off":
            machine_on = False
    # TODO 3 Print report.
        elif selection == "report":
            report()

    # TODO 4 Check resources sufficient?
        elif selection == "espresso":
            if MENU["espresso"]["ingredients"]["water"] > resources["water"]:
                print("Sorry there is not enough water")
                machine_on = False
            elif MENU["espresso"]["ingredients"]["coffee"] > resources["coffee"]:
                print("Sorry there is not enough coffee")
                machine_on = False

        elif selection == "latte":
            if MENU["latte"]["ingredients"]["water"] > resources["water"]:
                print("Sorry there is not enough water")
                machine_on = False
            if MENU["latte"]["ingredients"]["coffee"] > resources["coffee"]:
                print("Sorry there is not enough coffee")
                machine_on = False
            if MENU["latte"]["ingredients"]["milk"] > resources["milk"]:
                print("Sorry there is not enough milk")
                machine_on = False

        elif selection == "cappuccino":
            if MENU["cappuccino"]["ingredients"]["water"] > resources["water"]:
                print("Sorry there is not enough water")
                machine_on = False
            elif MENU["cappuccino"]["ingredients"]["coffee"] > resources["coffee"]:
                print("Sorry there is not enough coffee")
                machine_on = False
            elif MENU["cappuccino"]["ingredients"]["milk"] > resources["milk"]:
                print("Sorry there is not enough milk")
                machine_on = False

    # TODO Process coins.
        print("Please inset coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))

        total_inserted = (quarters* 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
        # print(total_inserted)

    # TODO Check transaction successful.
        cost = MENU[selection]["cost"]
        if total_inserted < cost:
            print("Sorry that's not enough money. Money refunded.")
        else:
            MONEY = MONEY + cost
            if total_inserted > cost:
                change = total_inserted - cost
                print(f"Here is ${change:.2f} change.")

    # # TODO Make coffee.
    #     if selection == "espresso":
    #         resources["water"] = WATER - MENU[selection]["water"]
    #         resources["coffee"] = COFFEE - MENU[selection]["coffee"]
    #     else:
    #         resources["coffee"] = COFFEE - MENU[selection]["coffee"]
    #         resources["milk"] = COFFEE - MENU[selection]["milk"]
    #         resources["water"] = WATER - MENU[selection]["water"] 
    #
    #     prompt()
