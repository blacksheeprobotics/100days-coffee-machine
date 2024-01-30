from menu import MENU
from menu import resources

# Global variables
money = 0.0


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
def process_coins(drink):
    global money
    money_paid = 0.0
    change = 0.0
    print("Please insert coins.")
    num_of_quarters = int(input("How many quarters?: "))
    num_of_dimes = int(input("How many dimes?: "))
    num_of_nickels = int(input("How many nickels?: "))
    num_of_pennies = int(input("How many pennies?: "))
    money_paid += (0.25 * num_of_quarters) + (0.10 * num_of_dimes) + (0.05 * num_of_nickels) + (
            0.01 * num_of_pennies)
    return money_paid


# TODO: 4. Check if transaction is successful
def check_transaction(drink, money_check):
    global money
    if money_check >= MENU[drink]["cost"]:
        money += MENU[drink]["cost"]
        change = money_check - MENU[drink]["cost"]
        print(f"Here is ${change:.2f} in change.")
        return True
    else:
        return False


# TODO: 5. Make coffee
def make_drink(drink):
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    if drink == "latte" or drink == "cappuccino":
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]

serve_coffee = True
while serve_coffee == True:
    get_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if get_choice == "report":
        print_report()
    elif get_choice == "off":
        serve_coffee = False
    elif (get_choice == "espresso") or (get_choice == "latte") or (get_choice == "cappuccino"):
        if check_resources(get_choice):
            money_paid = process_coins(get_choice)
            if check_transaction(get_choice, money_paid):
                make_drink(get_choice)
                print(f"Here is your {get_choice}. Enjoy!.")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Unable to serve.")
    else:
        print("I don't understand. Please try again.")
