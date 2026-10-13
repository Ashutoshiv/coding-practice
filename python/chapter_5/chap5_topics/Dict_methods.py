marks = {
    "Sunny": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Sunny"
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Sunny": 99 , "Renuka": 100})

print(marks.get("Sunny")) # prints none
print(marks)
print(marks["Sunny"]) # returns an error


