from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_simulator():

    making_coffee = True

    menu = Menu()
    coffeeMaker = CoffeeMaker()
    moneyMachine = MoneyMachine()

    while making_coffee:
        
        choice = input("What would you like? (espresso/latte/cappuccino): \n").lower()
        
        if choice == "off":
            print("Machine is off ❌")
            making_coffee = False
        elif choice == "report":
            coffeeMaker.report()
            moneyMachine.report()
        else:
            ordered_drink = menu.find_drink(choice)
            price = ordered_drink.cost
            if coffeeMaker.is_resource_sufficient(ordered_drink):
                if moneyMachine.make_payment(price):
                    coffeeMaker.make_coffee(ordered_drink)
                
            
coffee_simulator()            