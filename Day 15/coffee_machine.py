from menu import MENU, resources


def show_item_report(item):
    
    """ Show the user the ingredients
    and cost of a given item. """
    
    
    water = item["ingredients"]["water"]
    coffee = item["ingredients"]["coffee"]
    cost = item["cost"]
    try: 
        milk = item["ingredients"]["milk"]
        print(f"Water: {water}ml\n"
              f"Milk: {milk}ml\n"
              f"Coffee: {coffee}g\n"
              f"Money: ${cost}")
    except KeyError:
        print(f"Water: {water}ml\n"
              f"Coffee: {coffee}g\n"
              f"Money: ${cost}")

def show_machine_report(d_resources):
    
    """ Show the user the resources the machine has. """
    
    d_water = d_resources["water"]
    d_coffee = d_resources["coffee"]
    d_milk = d_resources["milk"]
    print(f"Water: {d_water}ml\n"
          f"Milk: {d_coffee}ml\n"
          f"Coffee: {d_milk}ml")
    try:
        d_profit = d_resources["profit"]
        print(f"Profit: ${d_profit}")
    except KeyError:
        pass
    
def check_item(item, d_resources):
    
    """ Check if a given item is available to make
    in the machine. """
    
    item_water = item["ingredients"]["water"]
    item_coffee = item["ingredients"]["coffee"]
    
    d_water = d_resources["water"]
    d_coffee = d_resources["coffee"]
    
    
    if d_water < item_water:
        print("Sorry there is not enough water.")
        return False
    if d_coffee < item_coffee:
        print("Sorry there is not enough coffee.")
        return False
    
    try: 
        item_milk = item["ingredients"]["milk"]
        d_milk = d_resources["milk"] 
           
        if d_milk < item_milk:
            print("Sorry there is not enough milk.")
            return False
        
    except KeyError:
        pass
        
    return True

def deduct_ingredients(item, d_resources):
    
    """ Deduct the required ingredients of a given item
    from the machine's resources. """
    
    item_water = item["ingredients"]["water"]
    item_coffee = item["ingredients"]["coffee"]
  
    
    d_resources["water"] -= item_water
    d_resources["coffee"] -= item_coffee
    
    
    try: 
        item_milk = item["ingredients"]["milk"]
        d_resources["milk"] -= item_milk
        
    except KeyError:
        pass
        

def check_money(item, payment_amount, d_resources):
    
    """ Check if the payment amount is enough for buying an item,
    gives refund if the amount is greater than the cost
    of that item and add profit to the machine. """
    
    cost = item["cost"]
    if payment_amount < cost:
        print("Sorry that's not enough money. Money refunded.”.")
        return False
    else:
        if payment_amount > cost:
            change = payment_amount - cost
            print(f"Here's your change: ${round(change, 2)}")
        d_resources["profit"] += cost
        return True

def coffee_machine(actual_menu, actual_resources):
    
    """ Run a coffee machine simulation. """
    
    making_coffee = True

    while making_coffee:
        
        resources = actual_resources

        report = input("Show machine report? Type (y/n): ").lower()
        if report == "y":
            show_machine_report(resources)
            
        choice = input("What would you like? (espresso/latte/cappuccino): \n").lower()
        
        
            
        item = actual_menu[choice]
        if check_item(item, resources):
            print("Now insert the payment...")
            # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
            quarters = int(input("Type the amount of quarters: ")) * 0.25
            dimes = int(input("Type the amount of dimes: ")) * 0.1
            nickles = int(input("Type the amount of nickles: ")) * 0.05
            pennies = int(input("Type the amount of pennies: ")) * 0.01
            coins = quarters + dimes + nickles + pennies
            if check_money(item, coins, resources):
                deduct_ingredients(item, resources)
                print(f"Here is your {choice}. Enjoy!")
            
        turn_off = input("Type 'off' if you want to turn off the machine, type 'on' to continue ordering: ").lower()
        if turn_off == "off":
            print("Machine is off")
            making_coffee = False
                
                
coffee_machine(MENU, resources)