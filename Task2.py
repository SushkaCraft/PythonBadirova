import math

def calculate_z(x, y):
    return (9 * math.pi * y + 10 * math.cos(x) * math.exp(x)) / (math.sqrt(y) - math.sin(y))
  
print(f"Вариант 1: Z = {calculate_z(-0.93, 8.3)}")
print(f"Вариант 2: Z = {calculate_z(-5.5, 1.2)}")
print(f"Вариант 3: Z = {calculate_z(11.8, 0.35)}")
print(f"Вариант 4: Z = {calculate_z(-5.95, -0.57)}")
print(f"Вариант 5: Z = {calculate_z(-7.85, 0.13)}")
print(f"Вариант 6: Z = {calculate_z(1.13, 5.75)}")
print(f"Вариант 7: Z = {calculate_z(-7.65, 3.51)}")
print(f"Вариант 8: Z = {calculate_z(-2.25, 1.7)}")
print(f"Вариант 9: Z = {calculate_z(-3.13, 8.1)}")
print(f"Вариант 10: Z = {calculate_z(-5.9, 8.06)}")
print(f"Вариант 11: Z = {calculate_z(-6.65, 5.8)}")
print(f"Вариант 12: Z = {calculate_z(-0.53, 4.3)}")
print(f"Вариант 13: Z = {calculate_z(-0.77, 0.89)}")
print(f"Вариант 14: Z = {calculate_z(-1.5, -0.176)}")
print(f"Вариант 15: Z = {calculate_z(1.34, 1.34)}")
