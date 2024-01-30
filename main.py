from menu import MENU
from menu import resources

# Global variables
money = 2.50


# TODO: 1. Print report of all coffee machine resources
def print_report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${money}")


# TODO: 2. Check resources sufficient to make drink order
def check_resources(drink):
    drink_can_be_processed = True
    if resources["water"] < MENU[drink]["ingredients"]["water"]:
        print("Sorry there is not enough water")
        drink_can_be_processed = False
    if resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee")
        drink_can_be_processed = False
    if drink == "latte" or drink == "cappuccino":
        if resources["milk"] < MENU[drink]["ingredients"]["milk"]:
            print("Sorry there is not enough milk")
            drink_can_be_processed = False
    return drink_can_be_processed

# TODO: 3. Process coins to pay for drink

# TODO: 4. Check if transaction is successful

# TODO: 5. Make coffee
serve_coffee = True
while serve_coffee == True:
    get_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if get_choice == "report":
        print_report()
    elif get_choice == "off":
        serve_coffee = False
    elif (get_choice == "espresso") or (get_choice == "latte") or (get_choice == "cappuccino"):
        print(MENU["espresso"]["ingredients"]["water"])
        resource_sufficient = check_resources(get_choice)
        if resource_sufficient:
            print("Coffee served")
        else:
            print("Unable to serve.")
    else:
        print("I don't understand. Please try again.")
