class CoffeeMachine:
    def __init__(self):
        self.amount = []
        self.MENU = {
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
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def check_resource(self,coffee):
        if self.resources['water'] < self.MENU[coffee]['ingredients']['water']:
            print("Not enough resource of water")
            return 0
        elif self.resources['coffee'] < self.MENU[coffee]['ingredients']['coffee']:
            print("Not enough resource of coffee")
            return 0
        elif coffee != "espresso":
            if self.resources['milk'] < self.MENU[coffee]['ingredients']['milk']:
                print("Not enough resource of milk")
                return 0
        else:
            return 1
    def report(self):
        print(self.resources)
        sum = 0
        for i in self.amount:
            sum += i
        print(f"Money: {sum}")
    def get_amount(self):
        print("Enter the amount:")
        quarters = int(input('Enter Quaters :')) * 0.25
        dimes = int(input('Enter dimes :')) * 0.10
        nickles = int(input('Enter nickles :')) * 0.05
        pennies = int(input('Enter pennies :')) * 0.01
        tot = quarters + dimes + nickles + pennies
        tot = round(tot, 2)
        return tot
    def transaction(self,c_type,tot):
        self.resources['water'] = self.resources['water'] - self.MENU[c_type]['ingredients']['water']
        self.resources['coffee'] = self.resources['coffee'] - self.MENU[c_type]['ingredients']['coffee']
        if c_type != "espresso":
            self.resources['milk'] = self.resources['milk'] - self.MENU[c_type]['ingredients']['milk']
        if tot == self.MENU[c_type]['cost']:
            self.amount.append(tot)
        elif tot > self.MENU[c_type]['cost']:
            self.amount.append(self.MENU[c_type]['cost'])
            print(f"the extra amount is {round(tot - self.MENU[c_type]['cost'], 2)} is refunded")
        print(f"Here is your {c_type}!! Enjoy")

if __name__ == '__main__':
    coffee = CoffeeMachine()
    c_type = "report"
    while c_type == "report" or c_type == "espresso" or c_type == "latte" or c_type == "cappuccino" :
        c_type = input('What would you like? (espresso/latte/cappuccino):')
        if c_type == "off":
            break
        elif c_type == "report":
            coffee.report()
            continue
        elif c_type == "espresso" or c_type == "latte" or c_type == "cappuccino" :
            val = coffee.check_resource(c_type)
            if val == 0:
                break;
            else:
                tot = coffee.get_amount()
                if tot < coffee.MENU[c_type]['cost']:
                    print("Sorry that's not enough money. Money refunded")
                    break
                else:
                    coffee.transaction(c_type,tot)
                    continue
