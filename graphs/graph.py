import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

functions = {
    "x**2": (-2, 2),
    "x**3": (-2, 2),
    "x**4": (-2, 2),
    "np.cos(2 * np.pi * x)": (-10, 10),
    "1 / x * np.cos(2 * np.pi * x)": (1, 10),
    "np.exp(-x) * np.cos(2 * np.pi * x)": (-10, 10),
    "4 * np.sin(np.pi + x / 8) - 1": (-10, 10),
    "2 * np.cos(x - 2) + np.sin(2 * x - 4)": (-20 * np.pi, 10 * np.pi),
    "np.log(x + 1)": (0, np.e - 1),
    "np.log2(np.abs(x))": (-4, 4),
    "2**x": (-2, 2),
    "np.e**x": (-2, 2),
    "2**(-x)": (-2, 2),
    "np.sqrt(x)": (1, 125),
    "np.cbrt(x)": (1, 32),
}

for i, (expr, (start, end)) in enumerate(functions.items(), 1):
    plt.figure()
    if i == 6:
        x = np.arange(2, 5, 0.2)
        y = eval(expr)
        plt.plot(x, y, color='magenta', linestyle='--', marker='o')
    else:
        if expr == "np.log2(np.abs(x))":
            x = np.arange(start, end, 0.01)
            x = x[x != 0]
        else:
            x = np.linspace(start, end, 400)
        y = eval(expr)
        plt.plot(x, y)
    plt.title(f"{i}. {expr}")
    plt.grid()

# 8 
plt.figure()
x = np.linspace(-1, 1, 400)
for n in range(1, 7):
    plt.plot(x, x**n, label=f'x^{n}')
plt.title("1. Степенные многочлены")
plt.legend()
plt.grid()

plt.figure()
t = np.linspace(-1, 1, 400)
for _W_ in range(2, 9):
    plt.plot(t, np.sin(_W_ * np.pi * t), label=f'ω={_W_}π')
plt.title("2. Синусоиды с разными частотами")
plt.legend()
plt.grid()

plt.figure()
t = np.linspace(-1, 1, 400)
for _F_0 in np.arange(0, 5*np.pi/6 + 0.1, np.pi/6):
    plt.plot(t, np.sin(2*np.pi*t + _F_0), label=f'φ0={_F_0/np.pi:.2f}π')
plt.title("3. Синусоиды с разными фазами")
plt.legend()
plt.grid()

plt.figure()
x = np.linspace(1, 10, 400)
plt.plot(x, np.log2(x), label='log2(x)')
plt.plot(x, np.log(x), label='ln(x)')
plt.plot(x, np.log10(x), label='log10(x)')
plt.title("4. Логарифмические функции")
plt.legend()
plt.grid()

plt.figure()
x = np.linspace(-10, 10, 400)
plt.plot(x, (np.exp(x) - np.exp(-x))/2, label='sh(x)')
plt.plot(x, (np.exp(x) + np.exp(-x))/2, label='ch(x)')
plt.plot(x, (np.exp(x) - np.exp(-x))/(np.exp(x) + np.exp(-x)), label='th(x)')
plt.title("5. Гиперболические функции")
plt.legend()
plt.grid()

# 9
def plot_subplots(rows, cols, layout_name):
    fig = plt.figure(figsize=(cols*6, rows*4))
    axes = fig.subplots(rows, cols)
    
    x = np.linspace(-1, 1, 400)
    for i, ax in enumerate(axes.flat if rows*cols > 1 else [axes]):
        if i == 0:
            for n in range(1,7):
                ax.plot(x, x**n)
                ax.set_title(f"Степенные x^{n}")
                ax.grid()
        elif i == 1:
            for _W_ in range(2,9):
                ax.plot(x, np.sin(_W_*np.pi*x))
                ax.set_title(f"Синусы ω={_W_}π")
                ax.grid()
        elif i == 2:
            for _F_ in np.arange(0, 5*np.pi/6+0.1, np.pi/6):
                ax.plot(x, np.sin(2*np.pi*x + _F_))
                ax.set_title(f"Фаза {_F_/np.pi:.2f}π")
                ax.grid()
        elif i == 3:
            ax.plot(x, np.log2(x+1), x, np.log(x+1), x, np.log10(x+1))
            ax.set_title("Логарифмы")
            ax.grid()
        elif i == 4:
            ax.plot(x, (np.exp(x)-np.exp(-x))/2, 
                    (np.exp(x)+np.exp(-x))/2, 
                    (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x)))
            ax.set_title("Гиперболические")
            ax.grid()
        if i >= 4: break
    plt.tight_layout()
    plt.savefig(f'{layout_name}.png')

configs = [(5,1), (3,2), (2,3), (1,5)]
for idx, (r,c) in enumerate(configs, 1):
    plot_subplots(r, c, f'layout_{idx}')
    plt.close()

# 10
labels = ['Только 5', '5 и 4', 'С 3', 'Пересдачи', 'Отчислены']
sizes = [15, 35, 40, 8, 2]

plt.figure()
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Успеваемость группы')
plt.savefig('pie_chart.png')
plt.show()
