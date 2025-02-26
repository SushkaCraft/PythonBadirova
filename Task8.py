# Task 1
School = {
    '1а': 25,
    '1б': 30,
    '2в': 20,
    '3г': 28,
    '4д': 22
}

print("Количество учащихся в классах:", School)

klass = input("Введите класс (например, 1а): ")

if klass in School:
    print(f"В классе {klass} учится {School[klass]} человек.")
else:
    print("Такого класса не существует.")

# Task 2
def reverse_dict(dict_items):
    return {value: key for key, value in dict_items}

original_dict = {
    1: "яблоко",
    2: "банан",
    3: "апельсин"
}

reversed_dict = reverse_dict(original_dict.items())

print("Исходный словарь:", original_dict)
print("Обратный словарь:", reversed_dict)

# Task 3
School = {'1а': 16, '1б': 20, '2в': 18, '3г': 22, '4д': 19}
School['1а'] = 18
School['2в'] = 20
School['4д'] = 21
print(School)

# Task 4
vocab = {'cat': 'кошка', 'dog': 'собака', 'mouse': 'мышь', 'house': 'дом', 'eats': 'ест', 'in': 'в', 'too': 'тоже'}
text = "Mouse in house. Cat in house.\nCat eats mouse in dog house.\nDog eats mouse too."

translated_lines = []
for line in text.split('\n'):
    sentences = line.split('. ')
    translated_sentences = []
    for sentence in sentences:
        words = sentence.split()
        translated_words = [vocab.get(word.lower(), word) for word in words]
        translated_sentences.append(' '.join(translated_words))
    translated_lines.append('. '.join(translated_sentences))

print('\n'.join(translated_lines))
