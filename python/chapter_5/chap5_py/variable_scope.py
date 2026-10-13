# variable scope = where a variable is visible and accessible 
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# local

# def func1():
#     x = 1
#     print(x)

# def func2():
#     x = 3
#     print(x)

# func1()
# func2()

# Enclosed

# def func1():
#     x = 1


# def func2():

#     print(x)

# func1()
# func2()

# Global

# def func1():

#     print(x)

# def func2():

#     print(x)
# x = 3

# func1()
# func2()

# Built-in

# from math import e

# def func1():
#     print(e)

# e = 4

# func1()
