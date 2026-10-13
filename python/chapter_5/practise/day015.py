temp = int(input("Enter the temperature: "))
is_sunny = input("Enter True or False; ")

if is_sunny.lower() == "true" :
    is_sunny = True
elif is_sunny.lower() == "false":
    is_sunny = False
else:
    print("Please choose eather True or False ")



if temp >= 28 and is_sunny:
    print("It is Hot outside")
    print("It is Sunny ")
elif temp <= 0 and is_sunny:
    print("It is COLD outside ")
    print("It is SUNNY")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside")
    print("It is SUNNY")
if temp >= 28 and not is_sunny:
    print("It is Hot outside")
    print("It is Cloudy")
elif temp <= 0 and not is_sunny:
    print("It is COLD outside ")
    print("It is  Cloudy")
elif 28 > temp > 0 and not is_sunny:
    print("It is WARM outside")
    print("It is  Cloudy")
else:
    print("Your input is invalid ")
