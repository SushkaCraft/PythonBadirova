import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

functions = {
    "x**2 + y**2": (-3, 3),
    "x**2 - y**2": (-3, 3),
    "x**3 + y**3": (-3, 3),
    "x**3 - y**3": (-3, 3),
    "x**2 - y**2 + x": (-3, 3),
    "x**2 - y**2 + y": (-3, 3),
    "x**2 + y**2 + x": (-3, 3),
    "x**2 + y**2 + y": (-3, 3),
    "np.sin(x*y)": (-3, 3),
    "np.cos(x*y)": (-3, 3),
    "np.tan(x*y)": (-3, 3),
    "x*y": (-3, 3),
    "x - np.sin(x*y)": (-3, 3),
    "x + np.cos(x*y)": (-3, 3),
    "np.sqrt(x**2 + y**2)": (-3, 3)
}

for i, (expr, (start, end)) in enumerate(functions.items(), 1):
    x = np.linspace(start, end, 100)
    y = np.linspace(start, end, 100)
    X, Y = np.meshgrid(x, y)
    Z = eval(expr)
    
    plt.figure()
    plt.contourf(X, Y, Z, levels=20, cmap='viridis')
    plt.colorbar()
    plt.title(f"{i}. Контур: {expr}")
    plt.savefig(f"contour_{i}.png")
    plt.close()
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    plt.title(f"{i}. 3D: {expr}")
    plt.savefig(f"3d_{i}.png")
    plt.close()

plt.show()