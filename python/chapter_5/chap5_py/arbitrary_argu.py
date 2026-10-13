# *args    = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#            *  unpacking operator
#            1. positional 2. default 3. keyword 4. ARBITRARY

# 1. *args

# def add(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total

# print(add(1, 2, 3))

# def display_name (*args):
#     for arg in args:
#         print(arg, end=" ")

# display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III" )

# 2. **kwargs

# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#     # for key in kwargs.keys():
#     #     print(key)
#     # for value in kwargs.values():
#     #     print(value)

# print_address(street="road no. 0", 
#               city= "Patna", 
#               state="Bihar", 
#               zip="800024")

def shipping_lebel(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    print(f"{kwargs.get('city')}, {kwargs.get('state')}, {kwargs.get('zip')}")


shipping_lebel("Dr.", "Spongebob", "Harold", "Squarepants", "III",
               street="road no. 0", 
               city= "Patna", 
               state="Bihar", 
               zip="800024")