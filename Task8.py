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
text = "Mouse in house. Cat in house. \nCat eats mouse in dog house. \nDog eats mouse too. "

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

# Task 5
School = {'1а': 20, '1б': 25, '2в': 18, '3г': 22, '4д': 19}
School['5е'] = 23
School['6ж'] = 24
print(School)

# Task 6
School = {'1а': 20, '1б': 25, '2в': 18, '3г': 22, '4д': 19}
del School['2в']
print(School)

# Task 7
text = "Пример текста на русском языке. Этот текст содержит повторяющиеся слова: текст, пример, слова, слова, пример."
word_count = {}
words = text.lower().split()
for word in words:
    cleaned_word = ''.join(filter(str.isalpha, word))
    if cleaned_word:
        word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1

sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
print(sorted_words[:10])

# Task 8
School = {'1а': 20, '1б': 25, '2в': 18, '3г': 22, '4д': 19}
total = sum(School.values())
print(total)

# Task 9
n = int(input())
countries = {}
for _ in range(n):
    country, *langs = input().split()
    for lang in langs:
        countries.setdefault(lang, []).append(country)

query_langs = input().split()
for lang in query_langs:
    print(f"{lang}: {', '.join(countries.get(lang, ['Нет данных']))}")

# Task 10
en_ru = {
    'cat': ['кошка'],
    'dog': ['собака'],
    'home': ['домашняя папка', 'дом'],
    'mouse': ['мышь', 'манипулятор мышь'],
    'to do': ['делать', 'изготавливать'],
    'to make': ['изготавливать']
}

ru_en = {}
for en_word, ru_translations in en_ru.items():
    for ru_word in ru_translations:
        ru_en.setdefault(ru_word, []).append(en_word)

for ru_word in sorted(ru_en.keys()):
    translations = ', '.join(sorted(ru_en[ru_word]))
    print(f"{ru_word} - {translations}")

# Task 11
s = 'how many times'
count = {}
for char in s:
    if char != ' ':
        count[char] = count.get(char, 0) + 1

result = {}
for char, freq in count.items():
    result.setdefault(freq, []).append(char)

for key in result:
    result[key].sort()

print(result)

# Task 12
toys = {
    'конструктор': '6+',
    'мяч': '3+',
    'пазл': '4+',
    'кукла': '5+',
    'машинка': '3+'
}

sorted_toys = dict(sorted(toys.items()))
print(sorted_toys)

# Task 13
en_ru = {
    'cat': ['кошка'],
    'dog': ['собака'],
    'home': ['дом', 'домашняя папка'],
    'mouse': ['мышь', 'манипулятор мышь']
}

ru_en = {}
for en_word, ru_words in en_ru.items():
    for ru_word in ru_words:
        ru_en.setdefault(ru_word, []).append(en_word)

for ru_word in ru_en:
    ru_en[ru_word] = sorted(ru_en[ru_word])

print(ru_en)
