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

# TODO: 1. prompt user "what would you like?" (espresso/latte.cappuccino)
# TODO: 2. turn off coffee machine when "off"
# TODO: 3. shows report when "report"
# TODO: 4. check if sufficient resources (milk, coffee, water)
# TODO: 5. prompt user to accept coins
# TODO: 6. show if sufficient funds (q,d,n,p)
# TODO: 7. make coffee, reduce resources and funds
coffee_machine_on = True
money = 0


def user_order(user_input):
    if user_input == "espresso":
        return MENU["espresso"]
    elif user_input == "latte":
        return MENU["latte"]
    elif user_input == "cappuccino":
        return MENU["cappuccino"]
    else:
        return "off"


def check_resources():
    if drink_ingredients["water"] < resources["water"]:
        return "not enough resources"
    elif drink_ingredients["milk"] < resources["milk"]:
        return "not enough resources"
    elif drink_ingredients["coffee"] < resources["coffee"]:
        return "not enough resources"
    else:
        return "enough resources"


while coffee_machine_on:
    order = input("What would you like? 'espresso' , 'latte' , 'cappuccino' ").lower()
    if order == "off":
        coffee_machine_on = False
    elif order == "report":
        for items in resources:
            print(f"{items} : {resources[items]}")
        print(f"money : {money}")
    else:
        user_order(order)
    # chosen_drink = user_order(order)
    # drink_ingredients = chosen_drink["ingredients"]









