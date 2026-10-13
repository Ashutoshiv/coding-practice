# Concession stand program

menu = {"pizza": 5.00,
        "nachos": 6.30,
        "popcorn": 1.30,
        "fries": 3.20,
        "chips": 1.30,
        "pretzel": 3.50,
        "soda": 2.34,
        "lemonade": 4.34}
cart = []
total = 0

print("-------- MENU ---------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("---------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("-------- YOUR ORDER ---------")

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")