# Import coffee menu and resources
from menufile import MENU
from menufile import resources


# Checks if user has enough money for coffee item
def transaction_check(a):
    if coffee_input == a:
        global money
        global change
        if MENU[a]["cost"] <= money:
            change = money - MENU[a]["cost"]
            money = 0
            change = round(change, 2)
            money += change
            return True
        else:
            money = 0
            change = 0
            return False


# Coffee resources used, coffee given, change given
def make_coffee(a):
    resources['water'] -= MENU[a]["ingredients"]['water']
    resources['coffee'] -= MENU[a]["ingredients"]['coffee']
    if coffee_input != 'espresso':
        resources['milk'] -= MENU[a]["ingredients"]['milk']
    if change > 0:
        print(f"Here is ${change} in change.")
        print(f"Here is your {a} ☕ Enjoy!")
    elif change == 0:
        print(f"Here is your {a} ☕ Enjoy!")


# Checks if machine has enough ingredients for selected coffee
def ingredient_check(a):
    if resources['water'] >= MENU[a]["ingredients"]['water']:
        if resources['coffee'] >= MENU[a]["ingredients"]['coffee']:
            if a == 'espresso':
                return True
            elif resources['milk'] >= MENU[a]["ingredients"]['milk']:
                return True
            else:
                print("Sorry there is not enough ")
                return False
        else:
            print("Sorry there is not enough coffee")
            return False
    else:
        print("Sorry there is not enough water")
        return False


# Asks for money input in coins
def insert_coins():
    global quarters
    global dimes
    global nickels
    global pennies
    global money
    while True:
        try:
            quarters = int(input("How many quarters?: "))
            quarters *= .25
            dimes = int(input("How many dimes?: "))
            dimes *= .1
            nickels = int(input("How many nickels?: "))
            nickels *= .05
            pennies = int(input("How many pennies?: "))
            pennies *= .01
            money = quarters + dimes + nickels + pennies
            money = round(money, 2)
            break
        except ValueError:
            print("Invalid input. Please type a number for each coin.")
            continue


# Variable scopes defined
quarters = 0
dimes = 0
nickels = 0
pennies = 0
money = 0
change = 0

# Coffee machine while loop to ask for command
while True:
    try:
        coffee_input = input("What would you like? (espresso/latte/cappuccino)\n").lower()
    except ValueError:
        print("Invalid input. Please give your choice of coffee.")
        continue
    if coffee_input == 'off':
        break
    elif coffee_input == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Milk: {resources['milk']}g")
        print(f"Money: ${money}")
        continue
    elif coffee_input == 'espresso':
        if ingredient_check('espresso'):
            insert_coins()
            if transaction_check('espresso'):
                make_coffee('espresso')
                continue
            else:
                print("Sorry that's not enough money. Money refunded.")
                continue
        else:
            continue
    elif coffee_input == 'latte':
        if ingredient_check('latte'):
            insert_coins()
            if transaction_check('latte'):
                make_coffee('latte')
                continue
            else:
                print("Sorry that's not enough money. Money refunded.")
                continue
        else:
            continue
    elif coffee_input == 'cappuccino':
        if ingredient_check('cappuccino'):
            insert_coins()
            if transaction_check('cappuccino'):
                make_coffee('cappuccino')
                continue
            else:
                print("Sorry that's not enough money. Money refunded.")
                continue
        else:
            continue
    else:
        print("Invalid input. Please give your choice of coffee.")
        continue
