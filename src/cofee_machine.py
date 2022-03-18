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

amount = []
sum=0
condition = "yes"
def check_resource(coffee):
    if resources['water'] < MENU[coffee]['ingredients']['water']:
        print("Not enough resource of water")
        return 0
    elif resources['coffee'] < MENU[coffee]['ingredients']['coffee']:
        print("Not enough resource of coffee")
        return 0
    elif coffee != "espresso":
        if resources['milk'] < MENU[coffee]['ingredients']['milk']:
            print("Not enough resource of milk")
            return 0
    else:
        return 1
def report():
    print(resources)
    sum = 0
    for i in amount:
        sum += i
    print(f"Money: {sum}")
def get_amount():
    print("Enter the amount:")
    quarters = int(input('Enter Quaters :')) * 0.25
    dimes = int(input('Enter dimes :')) * 0.10
    nickles = int(input('Enter nickles :')) * 0.05
    pennies = int(input('Enter pennies :')) * 0.01
    tot = quarters + dimes + nickles + pennies
    tot = round(tot, 2)
    return tot
def transaction(c_type,tot):
    resources['water'] = resources['water'] - MENU[c_type]['ingredients']['water']
    resources['coffee'] = resources['coffee'] - MENU[c_type]['ingredients']['coffee']
    if c_type != "espresso":
        resources['milk'] = resources['milk'] - MENU[c_type]['ingredients']['milk']
    if tot == MENU[c_type]['cost']:
        amount.append(tot)
    elif tot > MENU[c_type]['cost']:
        amount.append(MENU[c_type]['cost'])
        print(f"the extra amount is {round(tot - MENU[c_type]['cost'], 2)} is refunded")
    print(f"Here is your {c_type}!! Enjoy")

while condition == "yes":
    c_type = input('What would you like? (espresso/latte/cappuccino):')
    if c_type == "off":
        break
    elif c_type == "report":
        report()
    elif c_type == "espresso" or c_type == "latte" or c_type == "cappuccino" :
        val = check_resource(c_type)
        if val == 0:
            break;
        else:
            tot = get_amount()
            if tot < MENU[c_type]['cost']:
                print("Sorry that's not enough money. Money refunded")
                break
            else:
                transaction(c_type,tot)
                condition = input("Do you have next round? yes or no")
