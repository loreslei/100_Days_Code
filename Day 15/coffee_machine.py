from menu import MENU, resources



def show_item_report(ingredients, price):
    
    """ Show the user the ingredients
    and cost of a given item. """
      
    water = ingredients["water"]
    coffee = ingredients["coffee"]
    cost = price
    
    print(f"Water 💧: {water}ml\n"
          f"Coffee ☕: {coffee}g")
    try: 
        milk = ingredients["milk"]
        print(f"Milk 🥛: {milk}ml")
    except KeyError:
       pass
    print(f"Money 💵: ${cost}")

def show_machine_report(d_resources):
    
    """ Show the user the resources the machine has. """
    
    d_water = d_resources["water"]
    d_coffee = d_resources["coffee"]
    d_milk = d_resources["milk"]
    print(f"Water 💧: {d_water}ml\n"
          f"Milk 🥛: {d_coffee}ml\n"
          f"Coffee ☕: {d_milk}g")
    try:
        d_profit = d_resources["profit"]
        print(f"Profit 💵: ${d_profit}")
    except KeyError:
        pass
    
def check_item(ingredients, d_resources):
    
    """ Check if a given item is available to make
    in the machine. """
    
    for ingredient in ingredients:
        if ingredients[ingredient] >= d_resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
        
    return True

def check_money(price, payment_amount, d_resources):
    
    """ Check if the payment amount is enough for buying an item,
    gives refund if the amount is greater than the cost
    of that item and add profit to the machine. """
    
    cost = price
    if payment_amount < cost:
        print("Sorry that's not enough money. Money refunded.”.")
        return False
    else:
        if payment_amount > cost:
            change = payment_amount - cost
            print(f"Here's your change: ${round(change, 2)}")
        d_resources["profit"] += cost
        return True
    
def deduct_ingredients(ingredients, d_resources):
    
    """ Deduct the required ingredients of a given item
    from the machine's resources. """
    
    for ingredient in ingredients:
        d_resources[ingredient] -= ingredients[ingredient]
        
    
    
def insert_coins():
    """ Return the amount of coins inserted into the machine."""
    print("Now insert the payment...")
    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    quarters = int(input("Type the amount of quarters: ")) * 0.25
    dimes = int(input("Type the amount of dimes: ")) * 0.1
    nickles = int(input("Type the amount of nickles: ")) * 0.05
    pennies = int(input("Type the amount of pennies: ")) * 0.01
    coins = quarters + dimes + nickles + pennies
    return coins

def coffee_machine(actual_menu, actual_resources):
    
    """ Run a coffee machine simulation. """
    
    
    making_coffee = True

    while making_coffee:
        
        
        resources = actual_resources
            
        choice = input("What would you like? (espresso/latte/cappuccino): \n").lower()
        if choice == "off":
            print("Machine is off ❌")
            making_coffee = False
        elif choice == "report":
            show_machine_report(resources)
        else: 
            order_ingredients = actual_menu[choice]["ingredients"]
            cost = actual_menu[choice]["cost"]
            rep = input("Do you want to see the ingredients and cost? (y/n): ").lower()
            if rep == "y":
                show_item_report(order_ingredients, cost)
            else:
                if check_item(order_ingredients, resources):
                    inserted_coins = insert_coins()
                    if check_money(cost, inserted_coins, resources):
                        deduct_ingredients(order_ingredients, resources)
                        print(f"Here is your {choice} ☕. Enjoy!")
                
        
                
                
coffee_machine(MENU, resources)