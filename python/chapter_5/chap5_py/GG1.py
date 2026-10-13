def verify_user():
    while True:
        age = input("What is your age?(type 'exit' to quit): ")
        if age.lower() == "exit":
            print("Good bye!")
            break
        try:
            age = int(age)
            if age >= 18:
                return True
            elif age < 18:
                 return False
        except ValueError:
            print("Error! You didn't type a number. Please use digits like '8'.")

is_adult = verify_user()   

if is_adult == True:
   print("Accessing Confirming...")
elif is_adult == False:
   print("Access Denied.")