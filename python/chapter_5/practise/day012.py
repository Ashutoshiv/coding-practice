# python weight converter

weight =  float(input("Enter your weight: "))
unit = input("Kilograms or pound? (K or L): ")

if unit.lower() == "k":
    weight *= 2.205
    unit = "Lbs"
    print(f"Your weight is: {round(weight, 2)} {unit}")       
elif unit.lower() == "l": 
    weight /= 2.205
    unit = "Kgs"
    print(f"Your weight is: {round(weight, 2)} {unit}")       
else :
    print(f"{unit} was not valid")


# print(f"Your weight is: {round(weight, 2)} {unit}")       