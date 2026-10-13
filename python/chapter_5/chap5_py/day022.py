# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age can't be negative ")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old")


# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter a food you like (q to quit): ")
# print("bye")

# while loop = excute some code WHILE some condition remains true


num = int(input("Enter a # between 1 - 19: "))

while 1 > num > 19:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 19: "))

print(f"Your number is: {num}")