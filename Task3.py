# Zadanie 1

# a, b, c = int(input()), int(input()), int(input())
# in_interval = [x for x in [a, b, c] if 1 <= x <= 3]
# print(f"Задание 1: Числа из интервала [1,3]: {in_interval}")

a = int(input())
b = int(input())
c = int(input())
in_interval = []

for x in [a, b, c]:
    if 1 <= x <= 3:
        in_interval.append(x)

print(f"Числа из интервала [1,3]: {in_interval}")

# Zadanie 2

year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    days = 366
else:
    days = 365
print(f"В году {year} {days} дней.")

# Zadanie 3

purchase_amount = int(input())
discount = 0
if purchase_amount > 1000:
    discount = 0.05
elif purchase_amount > 500:
    discount = 0.03
final_price = purchase_amount * (1 - discount)
print(f"Сумма покупки с учетом скидки: {final_price:.2f} руб.")

# Zadanie 4

unit = int(input())
mass = int(input())
if unit == 1:
    kg = mass
elif unit == 2:
    kg = mass / 1_000_000
elif unit == 3:
    kg = mass / 1000
elif unit == 4:
    kg = mass * 1000
elif unit == 5:
    kg = mass * 100
else:
    kg = None
print(f"Масса в килограммах: {kg}")

# Zadanie 5

numbers = [1.0, 2.0, 3.0, 0.5]
min_number = min(numbers)
cos_min = math.cos(min_number)
print(f"Косинус минимального числа {min_number}: {cos_min:.2f}")

# Zadanie 6

numbers = [0.5, 1.0, 1.5]
max_number = max(numbers)
sin_max = math.sin(max_number)
print(f"Синус максимального числа {max_number}: {sin_max:.2f}")

# Zadanie 7

sides1 = [3, 4, 5]
sides2 = [6, 8, 10]

def triangle_area(sides):
    s = sum(sides) / 2
    area = (s * (s - sides[0]) * (s - sides[1]) * (s - sides[2])) ** 0.5
    return area

area1 = triangle_area(sides1)
area2 = triangle_area(sides2)

if area1 == area2:
    print("Foul!!!")
else:
    print("Треугольники не равновеликиe.")

# Zadanie 8

base = int(input())
height = int(input())
area = (base * height) / 2
if area % 2 == 0:
    area /= 2
    print(f"Площадь равнобедренного треугольника, деленная на 2: {area:.2f}")
else:
    print("Не делиться на 2!")

# Zadanie 9

month_number = int(input())
months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]
if 1 <= month_number <= 12:
    month_name = months[month_number - 1]
    print(f"Месяц номер {month_number}: {month_name}")
else:
    print("Неверный номер месяца.")

# Zadanie 10

import math

conversion_choice = int(input("1 - v gradusi\n2 - v radian\n"))
angle_value = int(input())

if conversion_choice == 1:
    degrees = math.degrees(angle_value)
    print(f"{angle_value} радиан = {degrees:.2f} градусов")
elif conversion_choice == 2:
    radians = math.radians(angle_value)
    print(f"{angle_value} градусов = {radians:.2f} радиан")
else:
    print("Неверный выбор перевода.")

# Zadanie 11

numbers = [-1, 0, 2]
positive_count = len([x for x in numbers if x > 0])
print(f"Количество положительных чисел: {positive_count}")

# Zadanie 12

x, y = int(input()), int(input())
if (x > 0 and y > 0) or (x < 0 and y < 0):
    geometric_mean = (x * y) ** 0.5
    print(f"Среднее геометрическое: {geometric_mean:.2f}")
else:
    arithmetic_mean = (x + y) / 2
    print(f"Среднее арифметическое: {arithmetic_mean:.2f}")

# Zadanie 13
# x, y, z = int(input()), int(input()), int(input())

x = int(input())
y = int(input())
z = int(input())
if (x**2 + y**2 == z**2) or (x**2 + z**2 == y**2) or (y**2 + z**2 == x**2):
    area = (x * y) / 2
    print(f"Задание 13: Площадь прямоугольного треугольника: {area:.2f}")
else:
    print("Задание 13: Прямоугольный треугольник не существует.")

# Dop zadaniya 

# Variant 1
x = int(input("x: "))

def calc_x(x):

    if  -2 < x and x < 5:
        return 5 * x**2 + 6
    elif x >= 5:
        return x**3 + 7
    elif x <= -2:
        return -1
    
# Variant 2
x = int(input("x: "))

def calc_x(x):

    if x >= 0:
        return math.sqrt(x**3 + 5)
    elif -3 < x and x < 0:
        return 3 * x**4 + 9

# Variant 3
x = int(input("x: "))

def calc_x(x):

    if -4 < x and x <= 5:
        return pow(pow(x, 2) + 6 * x, 1/3)
        
    elif x > 5:
        return pow(x, 5) + 3.5

print(calc_x(x))

# Variant 4
x = int(input("x: "))

def calc_x(x):

    if x < 122:
        return x * math.cos(x)
    elif -3 < x and x < 0:
        return 5 * x**2 + 1.7
    
# Variant 5
x = int(input("x: "))

def calc_x(x):

    if 0 < x and x < 2:
        return x**3 * math.cos(x)
    elif x >= 2:
        return 3 * x**4 + 7
    elif x <= 0:
        return math.sqrt(5 * x**2 + 16)

# Variant 6
x = int(input("x: "))

def calc_x(x):

    if x < 1.5:
        return x * math.tan(x) - math.sin(x)
    elif 1.5 <= x and x < 2.5:
        return x**3 + math.sin(x) + 7
    elif x >= 2.5:
        return 3 * x**3 + 5

# Variant 7
x = int(input("x: "))

def calc_x(x):

    if 0 < x and x < 2:
        return math.sqrt(3 * x**2 + 4)
    elif x >= 1:
        return 5 - pow(math.sin(x), 2)

# Variant 8
x = int(input("x: "))

def calc_x(x):

    if -5 < x and x < 0:
        return math.sqrt(x**2 + math.fabs(x))
    elif 0 <= x and x <= 2:
        return 5 * x**2

# Variant 9
x = int(input("x: "))

def calc_x(x):

    if 0 <= x and x < 1:
        return x * pow(math.cos(x), 2) + math.sin(x)
    elif 1 <= x and x <= 2:
        return math.sqrt(x**2 + 6 * math.sin(x))
    elif x > 2:
        return 1.7 * x**3 + 7

# Variant 10
x = int(input("x: "))

def calc_x(x):

    if x < 0:
        return math.sin(x) + amth.sqrt(x**2 + 1.2)
    elif 2 < x and x <= 6:
        return pow(math.tan(x), 2) + math.cos(x) + 35
