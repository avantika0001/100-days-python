#Local development environment setup & Coffee Machine

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

totalMoney=0
coffeeMachine_On=True


def dispenseDrink(drink):
    for item in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][item]>resources[item]:
            print(f"​Sorry there is not enough {item}.")
        else:
            resources[item]-=MENU[drink]["ingredients"][item]
               
        
def calculateMoney(drink):
    print("Please insert coins!")
    n1=int(input("How many quarters?"))
    n2=int(input("How many dimes?"))
    n3=int(input("How many nickels?"))
    n4=int(input("How many pennies?"))
    Usermoney=(n1*0.25)+(n2*0.10)+(n3*0.05)+(n4*0.01)
    if Usermoney<MENU[drink]["cost"]:
        print("Sorry that's not enough money! Money refunded.")
    else:
        print(f"Here is ${Usermoney-MENU[drink]['cost']} in change.")
        print(f"Here is your {drink} ☕, enjoy!")
        global totalMoney
        totalMoney+= MENU[drink]["cost"]
        print(totalMoney)   


def printReport():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {totalMoney}")


def serveDrink(drink):
    dispenseDrink(drink)
    calculateMoney(drink)
    

while coffeeMachine_On:
    choice=input("What would you like?(espresso/latte/cappuccino/report/off)")
    if choice=="espresso":
        serveDrink("espresso")
    elif choice=="latte":
        serveDrink("latte")
    elif choice=="cappuccino":
        serveDrink("cappuccino")
    elif choice=="report":
        printReport()
    elif choice=="off":
        print("Thanks for visiting!")
        coffeeMachine_On=False
    else:
        print("Please type a valid option!")                    

