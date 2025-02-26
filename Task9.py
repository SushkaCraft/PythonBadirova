# Task A -
student_num = tuple(range(1, 26))
last_names = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y')

index = int(input("Введите номер студента (от 1 до 25): "))

if 0 <= index < len(student_num):
    print(f"Номер студента: {student_num[index]}, Фамилия: {last_names[index]}")
else:
    print("Неверный номер студента. Пожалуйста, введите число от 1 до 25.")
    
# Task B -
index = 5
print(f"Студент под номерм 5: {last_names[index - 1]}")

# Task C -

print(f"Студент под номерм 5: {last_names[index]}")

# Task D -
combo_tuple = student_num + last_names
print(combo_tuple)

# Task E
slice_tuple = combo_tuple[20:30]

print(slice_tuple)
