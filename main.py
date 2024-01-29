from menu import MENU
from menu import resources

# Global variables
Water = 100.0
Milk = 50.0
Coffee = 76.0
Money = 2.50

# TODO: 1. Print report of all coffee machine resources
def print_report():
    print(f"Water: {Water}ml")
    print(f"Milk: {Milk}ml")
    print(f"Coffee: {Coffee}g")
    print(f"Money: ${Money}")

# TODO: 2. Check resources sufficient to make drink order
def check_resources(drink):
    if drink == "espresso":
        return True
    if drink == "latte":
        return True
    else:
        return True

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
    elif get_choice == "espresso" or "latte" or "cappuccino":
        resource_sufficient = check_resources(get_choice)
        if resource_sufficient == True:
            print("Coffee served")
        else:
            print("Unable to serve.")
    else:
        print("I don't understand. Please try again.")

