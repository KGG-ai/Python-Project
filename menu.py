menu = {"pizza" : 3.00,
        "nachos": 4.50,
        "fries" : 9.00,
        "tasty": 5.90,
        "kurkure" : 6.90}

cart = []
total = 0

print("---------MENU---------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("-----------------------")


while True:
    food = input("Select an item (q to quit) : ")
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("--------- YOUR ORDER ---------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")





