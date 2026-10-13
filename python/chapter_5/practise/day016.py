# num = int(input("Enter any number: "))


a = 6
b = 7
# age = int(input("Enter your age: "))
# temp = float(input("Enter the temperature: "))
user_role = "Admin"
# print("Posittive" if num > 0 else "Negative")
# result = "EVEN " if num % 2 == 0 else "ODD"
max_num = a if a > b else b
min_num = a if a < b else b
# status = "Adult" if age >= 18 else "Minor"
# weather = "Hot" if temp > 28  else "Lower temperature"
access_level = "Full access" if user_role == "Admin" else "Limited access"
# print(min_num)
# print(max_num)
# print(status)
print(access_level)