# return = statement used to end a function and send a result back to the caller

# z = add(1, 2)

# def add(x, y):
#     z = x + y
#     return z

# def subtract(x, y):
#     z = x - y
#     return z

# def multiply(x, y):
#     z = x - y
#     return z

# def devide(x, y):
#     z = x - y
#     return z

# print(add(1, 2))
# print(subtract(1, 2))
# print(multiply(1, 2))
# print(devide(1, 2))


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("sunny", "kumar")

print(full_name)