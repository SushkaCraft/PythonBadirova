import math

x, y, z = int(input("x: ")), int(input("y: ")), int(input("z: "))

f = -math.e**(x * math.sqrt(abs(y))) + z

v = abs(math.sin(math.cos(f))**2 + x)**(1/3)

w = f + v + math.log10(x * y * z)

U = x + y + math.exp(-w * v * f)

print(f)
print(v)
print(w)
print(U)
