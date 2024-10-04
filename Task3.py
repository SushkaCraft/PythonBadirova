# Variant 3
x = int(input("x: "))

def calc_x(x):

    if -4 < x and x <= 5:
        return pow(pow(x, 2) + 6 * x, 1/3)
        
    elif x > 5:
        return pow(x, 5) + 3.5

print(calc_x(x))
