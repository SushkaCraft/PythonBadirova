import math

# Задача 1: Сумма и количество элементов массива X(100)
def task1(X):
    return sum(X), len(X)

# Задача 2: Среднее арифметическое массива A(80)
def task2(A):
    return sum(A) / len(A)

# Задача 3: Копирование массива X(70) в Y
def task3(X):
    Y = X.copy()
    return Y, len(Y)

# Задача 4: Максимальный элемент массива B(50) и его индекс
def task4(B):
    max_val = max(B)
    return max_val, B.index(max_val) + 1

# Задача 5: Минимальный элемент массива C(40)
def task5(C):
    min_val = min(C)
    return min_val, C.index(min_val) + 1

# Задача 6: Поменять местами max и min в массиве D(80) (ИСПРАВЛЕННАЯ)
def task6(D):
    if len(D) == 0:
        return D
        
    max_val, min_val = max(D), min(D)
    max_idx, min_idx = D.index(max_val), D.index(min_val)
    D[max_idx], D[min_idx] = D[min_idx], D[max_idx]  # Исправлено здесь
    return D

# Задача 7: Среднее геометрическое массива Y(20)
def task7(Y):
    product = 1
    for num in Y:
        product *= num
    return math.pow(product, 1/len(Y))

# Задача 8: Упорядочить массив R из Z(30)
def task8(Z):
    positive = [num for num in Z if num > 0]
    negative = [num for num in Z if num < 0]
    return positive + negative

# Задача 9: Сумма элементов, кратных 3, в массиве N(50)
def task9(N):
    return sum(num for num in N if num % 3 == 0)

# Задача 10: Сумма и количество элементов X(n)
def task10(X):
    return sum(X), len(X)

# Задача 11: Среднее геометрическое массива A(n)
def task11(A):
    product = 1
    for num in A:
        product *= num
    return product ** (1 / len(A))

# Задача 12: Положительные элементы массива X(n) в Y
def task12(X):
    return [num for num in X if num > 0]

# Задача 13: Разделение элементов X(n) на Y (положительные) и Z (отрицательные)
def task13(X):
    Y = [num for num in X if num > 0]
    Z = [num for num in X if num < 0]
    return Y, Z

# Задача 14: Максимальный элемент массива B(k)
def task14(B):
    max_val = max(B)
    return max_val, B.index(max_val) + 1

# Задача 15: Минимальный элемент массива C(k)
def task15(C):
    min_val = min(C)
    return min_val, C.index(min_val) + 1

if __name__ == "__main__":
    print("\n=== Тестирование задач ===")
    
    X1 = list(range(1, 101))
    print("\nЗадача 1:", task1(X1))
    
    A2 = list(range(80))
    print("Задача 2:", task2(A2))
    
    X3 = list(range(70))
    print("Задача 3:", task3(X3)[1])
    
    B4 = [i % 47 for i in range(50)]
    print("Задача 4:", task4(B4))
    
    C5 = [i % 39 for i in range(40)]
    print("Задача 5:", task5(C5))
    
    D6 = [i for i in range(80)]
    D6[10], D6[20] = 100, -5
    task6(D6)
    print("Задача 6:", D6[10], D6[20])
    
    Y7 = [i+1 for i in range(20)]
    print("Задача 7:", f"{task7(Y7):.2f}")
    
    Z8 = [i - 15 for i in range(30)]
    print("Задача 8 (первые 5 элементов):", task8(Z8)[:5])
    
    N9 = list(range(50))
    print("Задача 9:", task9(N9))
    
    X10 = [1, 2, 3]
    print("Задача 10:", task10(X10))
    
    A11 = [2, 4, 8]
    print("Задача 11:", f"{task11(A11):.2f}")
    
    X12 = [-1, 2, -3, 4]
    print("Задача 12:", task12(X12))
    
    X13 = [-5, 3, -2, 7]
    print("Задача 13:", task13(X13))
    
    B14 = [10, 20, 30, 40]
    print("Задача 14:", task14(B14))
    
    C15 = [30, 20, 10, 40]
    print("Задача 15:", task15(C15))
