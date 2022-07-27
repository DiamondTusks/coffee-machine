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
    "coffee": 10,
}

WATER = resources["water"]
MILK = resources["milk"]
COFFEE = resources["coffee"]
MONEY = 0
machine_on = True
selection = ""
# TODO 1 user prompt
def prompt():
    return input("What would you like? (espresso, latter, cappuuccino): ").lower()

while machine_on:
    selection = prompt()
# TODO 2 Turn off the Coffee Machine by entering “off” to the prompt.
    if selection == "off":
        machine_on = False
# TODO 3 Print report.
    elif selection == "report":
        print(f"Water: {WATER}ml")
        print(f"Milk: {MILK}ml")
        print(f"Coffee: {COFFEE}g")
        print(f"Money: ${MONEY}")
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
        elif MENU["latte"]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry there is not enough coffee")
            machine_on = False
        elif MENU["latte"]["ingredients"]["milk"] > resources["milk"]:
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
    quarters = input("How many quarters?: ")
    dimes = input("How many dimes?: ")
    nickels = input("How many nickels?: ")
    pennies = input("How many pennies?: ")


