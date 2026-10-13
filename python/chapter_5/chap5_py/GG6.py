security_database = {
    "Ashutosh": "Admin Clearance",
    "Rishabh": "Guest Clearance",
    "Bobby":  "Simple Access"
}

Username = input("Enter your username to access the system: ")


if Username in security_database:
    clearance_level = security_database[Username]
    print(f"Hello! {Username}. Your status is: {clearance_level}")
    with open("mainframe_data.txt", "a") as file:
        file.write(f"{Username} successfully accessed the mainframe.\n")
else:
    with open("mainframe_data.txt", "a") as file:
        file.write("WARNING: Unknown user attempted access.")


with open("mainframe_data.txt", "r") as file:
    remembered_data = file.read()
    print(remembered_data)
