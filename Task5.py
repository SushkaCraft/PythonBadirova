def count_words_start_a():
    text = input("Введите строку: ")
    words = text.split()
    count = sum(1 for word in words if word.lower().startswith('а'))
    print(f"Количество слов, начинающихся с 'а': {count}")

def replace_colons():
    text = input("Введите строку: ")
    replaced_text = text.replace(":", "%")
    count = text.count(":")
    print("Измененная строка:", replaced_text)
    print(f"Количество замен: {count}")

def remove_dots():
    text = input("Введите строку: ")
    new_text = text.replace(".", "")
    count = text.count(".")
    print("Измененная строка:", new_text)
    print(f"Количество удаленных точек: {count}")

def replace_a_with_o():
    text = input("Введите строку: ")
    new_text = text.replace("а", "о")
    count = text.count("а")
    print("Измененная строка:", new_text)
    print(f"Количество замен: {count}")

def to_lowercase():
    text = input("Введите строку: ")
    new_text = text.lower()
    print("Измененная строка:", new_text)

def remove_a_count():
    text = input("Введите строку: ")
    count = text.count("а")
    new_text = text.replace("а", "")
    print("Измененная строка:", new_text)
    print(f"Количество удаленных символов: {count}")

def replace_p_with_star():
    text = input("Введите строку: ")
    new_text = ''.join('*' if char == 'п' else char for char in text)
    count = text.count('п')
    print("Измененная строка:", new_text)
    print(f"Количество замен: {count}")

def count_words():
    text = input("Введите строку, оканчивающуюся точкой: ")
    words = text.split()
    print(f"Количество слов в строке: {len(words)}")

def count_word_occurrences():
    text = input("Введите строку: ")
    word = input("Введите слово для поиска: ")
    count = text.count(word)
    print(f"Слово '{word}' встречается {count} раз(а) в тексте.")

def capitalize_words():
    text = input("Введите строку (предложение на английском языке): ")
    words = text.split()
    new_text = ' '.join(word.capitalize() for word in words)
    print("Измененная строка:", new_text)

def longest_n_sequence():
    text = input("Введите строку: ")
    max_sequence = ''
    current_sequence = ''
    for char in text:
        if char == 'н':
            current_sequence += char
            if len(current_sequence) > len(max_sequence):
                max_sequence = current_sequence
        else:
            current_sequence = ''
    print("Самая длинная последовательность букв 'н':", max_sequence)

def words_end_with_ya():
    text = input("Введите строку: ")
    words = [word for word in text.split() if word.endswith('я')]
    print("Слова, оканчивающиеся на 'я':", ', '.join(words))

def chars_inside_brackets():
    text = input("Введите строку с одной открывающей и одной закрывающей скобкой: ")
    start = text.find('(')
    end = text.find(')')
    if start != -1 and end != -1 and start < end:
        print("Символы внутри скобок:", text[start + 1:end])
    else:
        print("Скобки не найдены или расположены неправильно.")

def words_start_a_end_o():
    text = input("Введите строку: ")
    words = [word for word in text.split() if word.lower().startswith('а') and word.lower().endswith('о')]
    print("Слова, начинающиеся с 'а' и оканчивающиеся на 'о':", ', '.join(words))

def count_v_letters():
    text = input("Введите строку: ")
    count = text.lower().count('т')
    print(f"Количество букв 'т' в строке: {count}")
