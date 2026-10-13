import time

def count(start, end):
# def count(end, start=0): then we are to use just a ending value

    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

count(0, 10)