#### VIRTUAL COFFE MACHINE

import time

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 85,
    },

    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 125,
    },

    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 150,
    },

    "americano": {
        "ingredients": {
            "water": 300,
            "coffee": 20,
        },
        "cost": 110,
    },

    "mocha": {
        "ingredients": {
            "water": 200,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 170,
    },

    "blackcoffee": {
        "ingredients": {
            "water": 150,
            "coffee": 20,
        },
        "cost": 90,
    },

    "hotchocolate": {
        "ingredients": {
            "milk": 250,
            "water": 50,
        },
        "cost": 140,
    },

    "coldcoffee": {
        "ingredients": {
            "milk": 200,
            "coffee": 20,
            "water": 50,
        },
        "cost": 160,
    },

    "greentea": {
        "ingredients": {
            "water": 200,
        },
        "cost": 60,
    },

    "masalatea": {
        "ingredients": {
            "water": 100,
            "milk": 100,
        },
        "cost": 70,
    }
}

resources = {
    "water": 2000,
    "milk": 1000,
    "coffee": 500,
    "money": 0,
}


# COFFEE ART
def coffee_art():
    print(r"""
         ( (
          ) )
       ........
       |      |]
       \      /
        `----'
    """)


# CHECK RESOURCES
def is_resource_sufficient(order_ingredients):

    for item in order_ingredients:

        if order_ingredients[item] > resources[item]:
            print(f"\n❌ Sorry there is not enough {item}")
            return False

    return True


# PROCESS COINS
def process_coins():

    print("\n💰 Please insert coins")

    five = int(input("How many 5Rs coins   : "))
    ten = int(input("How many 10Rs coins  : "))
    twenty = int(input("How many 20Rs coins  : "))

    total = (five * 5) + (ten * 10) + (twenty * 20)

    return total


# PAYMENT CHECK
def is_transaction_successful(money_received, drink_cost):

    if money_received >= drink_cost:

        change = money_received - drink_cost

        print("\n✅ Payment Successful")
        print(f"💵 Change Returned : Rs{change}")

        resources["money"] += drink_cost

        return True

    else:
        print("\n❌ Sorry that's not enough money.")
        print("💸 Money refunded.")

        return False


# MAKE COFFEE
def make_coffee(drink_name, order_ingredients):

    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print(f"\n☕ Preparing your {drink_name.title()}...")
    time.sleep(1)

    print("▒▒▒▒▒▒▒▒▒▒ 20%")
    time.sleep(1)

    print("████▒▒▒▒▒▒ 40%")
    time.sleep(1)

    print("██████▒▒▒▒ 60%")
    time.sleep(1)

    print("████████▒▒ 80%")
    time.sleep(1)

    print("██████████ 100%")
    time.sleep(1)

    print(f"\n✅ Here is your {drink_name.title()}. Enjoy!")
    coffee_art()


# REPORT
def machine_report():

    print("\n========= MACHINE REPORT =========")

    print(f"💧 Water   : {resources['water']}ml")
    print(f"🥛 Milk    : {resources['milk']}ml")
    print(f"☕ Coffee  : {resources['coffee']}g")
    print(f"💰 Money   : Rs{resources['money']}")

    print("==================================")


# MENU DISPLAY
def display_menu():

    print("\n" + "=" * 45)
    print("         ☕ PYTHON COFFEE MACHINE ☕")
    print("=" * 45)

    print("""
1️⃣  Espresso         - Rs85
2️⃣  Latte            - Rs125
3️⃣  Cappuccino       - Rs150
4️⃣  Americano        - Rs110
5️⃣  Mocha            - Rs170
6️⃣  BlackCoffee      - Rs90
7️⃣  HotChocolate     - Rs140
8️⃣  ColdCoffee       - Rs160
9️⃣  GreenTea         - Rs60
🔟  MasalaTea         - Rs70

---------------------------------------------
Type 'report' -> Show resources
Type 'off'    -> Turn off machine
=============================================
""")


# MAIN PROGRAM
machine_on = True

print("\n🎉 Welcome to the Virtual Coffee Machine 🎉")

customer_name = input("👤 Enter your name: ")

print(f"\nHello {customer_name.title()} ☕")


while machine_on:

    display_menu()

    choice = input("👉 What would you like to have? ").lower()

    if choice == "off":

        print("\n🔴 Coffee Machine Turning Off...")
        print("🙏 Thank you for visiting!")

        machine_on = False

    elif choice == "report":

        machine_report()

    elif choice in MENU:

        drink = MENU[choice]

        if is_resource_sufficient(drink["ingredients"]):

            payment = process_coins()

            if is_transaction_successful(payment, drink["cost"]):

                print("\n========= BILL =========")

                print(f"👤 Customer : {customer_name.title()}")
                print(f"☕ Drink    : {choice.title()}")
                print(f"💰 Cost     : Rs{drink['cost']}")
                print(f"💵 Paid     : Rs{payment}")
                print(f"🪙 Change   : Rs{payment - drink['cost']}")

                print("========================")

                make_coffee(choice, drink["ingredients"])

                rating = input(
                    "\n⭐ Please rate our coffee (1-5): "
                )

                print(f"\n🙏 Thanks for giving {rating} stars!")

    else:

        print("\n❌ Invalid choice. Please try again.")