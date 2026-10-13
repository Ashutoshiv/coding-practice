temp = float(input("Enter the temperature: "))
is_raining = input("Is it raining: {Y/N}")

if temp > 35 or temp < 0 or is_raining.lower() == "y":
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is stil scheduled")    