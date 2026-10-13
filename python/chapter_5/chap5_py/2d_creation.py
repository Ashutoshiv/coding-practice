# fruits =     ["apple" , "orange", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potatos"]
# drinks =     ["dudh", "water", "cold drink"]

groceries = [["apple" , "orange", "banana", "coconut"], 
             ["celery", "carrots", "potatos"] , 
             ["dudh", "water", "cold drink"]]

groceries = (("apple" , "orange", "banana", "coconut"), 
             ("celery", "carrots", "potatos") , 
             ("dudh", "water", "cold drink"))

groceries = {{"apple" , "orange", "banana", "coconut"}, 
             {"celery", "carrots", "potatos"} , 
             {"dudh", "water", "cold drink"}}

# print(groceries[1][0])

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()