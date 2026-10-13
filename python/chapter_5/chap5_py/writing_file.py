# Python writing files (.txt, .json, .csv)
# import json

# employee = {
#     "name": "Spongebob",
#     "age": 30,
#     "job": "cook"
# }

# file_path = "C:/Users/ashut/Desktop/output.json"

# try:
        
#     with open(file=file_path, mode="w")as file:
#         json.dump(employee, file, indent=4)

#         print(f" jason file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists!")


# import csv

# employees = [["Name", "Age", "Job"],
#              ["Spongebob", 30, "Cook"],
#              ["Patrick", 34, "Unemployed"],
#              ["Sandy", 25, "Scientist"]]

# file_path = "C:/Users/ashut/Desktop/output.csv"

# try:
#     with open(file_path, "w", newline="") as file:
#         writer = csv.writer(file)
#         for row in employees:
#             writer.writerow(row)
#         print(f"csv file '{file_path}' was created")
# except  FileExistsError:
#     print("That file already exists!")



