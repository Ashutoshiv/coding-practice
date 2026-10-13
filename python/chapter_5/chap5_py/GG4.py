# security_database = {
#     "Ashutosh": "Admin Clearance",
#     "Rishabh": "Guest Clearance",
#     "Bobby":  "Simple Access"
# }

# user_input = input("Enter your username to access the system: ")

# # The AI dynamically checks the entire database in one line:
# if user_input in security_database:
#     # We pull their specific clearance level dynamically
#     clearance_level = security_database[user_input] 
    
#     # We use an 'f-string' (formatted string) to inject variables directly into the text
#     print(f"Hello! {user_input}. Your status is: {clearance_level}")
    
# else:
#     print("ALERT: Unrecognized user detected!")


# Writing to a file ("w" means write)
with open("jarvis_memory.txt", "w") as file:
    file.write("Sir loves black coffee.\n")

# Reading from a file ("r" means read)
with open("jarvis_memory.txt", "r") as file:
    remembered_data = file.read()
    print(remembered_data)