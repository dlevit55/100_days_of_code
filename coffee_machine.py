
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

machine_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Coffee Machine resources
water_sum = machine_resources["water"]
milk_sum = machine_resources["milk"]
coffee_sum = machine_resources["coffee"]
money_sum = 0
change = 0

def calc_money(): # Function to calculate the sum of all coins the users enters the coffee machine
    print("please insert coins.")
    quarter_amount = int(input("How many quarters?: ")) * 0.25 # The Value of a quarter
    dime_amount = int(input("How many dimes?: ")) * 0.10 # The value of a dime
    nickel_amount = int(input("How many nickels?: ")) * 0.05 # The value of a nickel
    penny_amount = int(input("How many pennies?: ")) * 0.01 # The value of a penny
    total_amount = quarter_amount + dime_amount + nickel_amount + penny_amount
    return total_amount

drink_coffe = True
while drink_coffe:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    if user_choice == "off":
        exit()
    elif user_choice == "report":
        print(f"Water: {water_sum}ml\nMilk: {milk_sum}ml\ncoffee: {coffee_sum}g\nmoney: ${money_sum}")
    elif user_choice == "espresso":
        if water_sum >= MENU["espresso"]["ingredients"]["water"] and coffee_sum >= MENU["espresso"]["ingredients"]["coffee"]:
            water_sum -= MENU["espresso"]["ingredients"]["water"]
            coffee_sum -= MENU["espresso"]["ingredients"]["coffee"]
            amount_entered = calc_money()
            if amount_entered > MENU["espresso"]["cost"]:
                money_sum += MENU["espresso"]["cost"]
                change = amount_entered - MENU["espresso"]["cost"]
                print("Here is your ☕ espresso Enjoy!")
                print(f"your change :${change:.2f}")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else :
            print("not enough resources")

    elif user_choice == "latte":
        if water_sum >= MENU["latte"]["ingredients"]["water"] and milk_sum >= MENU["latte"]["ingredients"]["milk"] and coffee_sum >= MENU["latte"]["ingredients"]["coffee"]:
            water_sum -= MENU["latte"]["ingredients"]["water"]
            milk_sum -= MENU["latte"]["ingredients"]["milk"]
            coffee_sum -= MENU["latte"]["ingredients"]["coffee"]
            amount_entered = calc_money()
            if amount_entered > MENU["latte"]["cost"]:
                money_sum += MENU["latte"]["cost"]
                change = amount_entered - MENU["latte"]["cost"]
                print("Here is your ☕ latte Enjoy!")
                print(f"your change :${change:.2f}")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("not enough resources")

    elif user_choice == "cappuccino":
        if water_sum >= MENU["cappuccino"]["ingredients"]["water"] and milk_sum >= MENU["cappuccino"]["ingredients"]["milk"] and coffee_sum >= MENU["cappuccino"]["ingredients"]["coffee"]:
            water_sum -= MENU["cappuccino"]["ingredients"]["water"]
            milk_sum -= MENU["cappuccino"]["ingredients"]["milk"]
            coffee_sum -= MENU["cappuccino"]["ingredients"]["coffee"]
            amount_entered = calc_money()
            if amount_entered > MENU["cappuccino"]["cost"]:
                money_sum += MENU["cappuccino"]["cost"]
                change = amount_entered - MENU["cappuccino"]["cost"]
                print("Here is your ☕ cappuccino Enjoy!")
                print(f"your change :${change:.2f}")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("not enough resources")

