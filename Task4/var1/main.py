import math

x, y = int(input("x: ")), int(input("y: "))

c = math.sqrt(math.log10(1/math.cos(x)) + y**2)

k = (math.cos(x)**2 + abs(math.sin(c**2)))**1/3

a = 3**(-c)*((math.sin(math.pi*k)/(math.pi*k)))

t = c - a * math.exp(-2) + math.atan(k)

print(c)
print(k)
print(a)
print(t)