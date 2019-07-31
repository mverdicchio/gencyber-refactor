import math


def main():
    name = input("what is your name?")
    print("hello", name, "Please enter the integer radius for 5 circles, one by one.")

    for i in range(5):
        radius = int(input())
        area = calc_area(radius)
        print("area is", area)

    print("thanks. we're done.")


def calc_area(radius):
    return math.pi * radius ** 2


main()
