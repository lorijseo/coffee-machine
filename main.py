MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

# TODO: 1. prompt user "what would you like?" (espresso/latte.cappuccino)
# TODO: 2. turn off coffee machine when "off"
# TODO: 3. shows report when "report"
# TODO: 4. check if sufficient resources (milk, coffee, water)
# TODO: 5. prompt user to accept coins
# TODO: 6. show if sufficient funds (q,d,n,p)
# TODO: 7. make coffee, reduce resources and funds


# def user_order(user_input):
#     if user_input == "espresso":
#         return MENU["espresso"]
#     elif user_input == "latte":
#         return MENU["latte"]
#     elif user_input == "cappuccino":
#         return MENU["cappuccino"]
#     else:
#         return "off"


def check_resources():
    """returns if there are enough resources"""
    if drink_ingredients["water"] > resources["water"]:
        print("Sorry, not enough water.")
        return "no resources"
    elif drink_ingredients["milk"] > resources["milk"]:
        print("Sorry, not enough milk.")
        return "no resources"
    elif drink_ingredients["coffee"] > resources["coffee"]:
        print("Sorry, not enough coffee.")
        return "no resources"
    else:
        pass


def calculate_money(q, d, n, p):
    """calculates total amount of coins inputted"""
    total = q * 0.25
    total += d * 0.10
    total += n * 0.05
    total += p * 0.01
    return round(total, 2)


coffee_machine_on = True
money = 0


while coffee_machine_on:
    order = input("What would you like? 'espresso' , 'latte' , 'cappuccino' ").lower()
    if order == "off":
        coffee_machine_on = False
    elif order == "report":
        for items in resources:
            print(f"{items} : {resources[items]}")
        print(f"money : {money}")
    else:
        chosen_drink = MENU[order]
        drink_ingredients = chosen_drink["ingredients"]
        if check_resources() == "no resources":
            coffee_machine_on = False
            break
        else:
            print("Please insert coins.")

        quarter = int(input("How many quarters?: "))
        dime = int(input("How many dimes?: "))
        nickel = int(input("How many nickels?: "))
        penny = int(input("How many pennies?: "))

        total_input = calculate_money(quarter, dime, nickel, penny)

        if total_input <= chosen_drink["cost"]:
            print(f"Sorry {total_input} is not enough.")
            coffee_machine_on = False
        else:
            return_change = round(total_input - chosen_drink["cost"], 2)
            money += chosen_drink["cost"]
            for items in drink_ingredients:
                resources[items] -= drink_ingredients[items]
            print(f"Here is ${return_change} in change.\nHere is your {order}. Enjoy!")



















