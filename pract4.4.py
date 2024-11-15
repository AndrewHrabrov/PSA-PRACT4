def char_freq(file):
    frequencies = {}
    russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    with open(file, encoding='utf-8') as file:
        text = file.read().lower()

        for char in text:
            if char not in russian_alphabet:
                text = text.replace(char, "")

        for letter in text:
            if letter in russian_alphabet:
                if letter in frequencies:
                    frequencies[letter] += 1
                else:
                    frequencies[letter] = 1

    all_letters = len(text)

    for letter in frequencies:
        frequencies[letter] = round((frequencies[letter] / all_letters), 7)

    # frequencies = dict(sorted(frequencies.items())) # сортировка по алфавиту
    # сортировка частот по убыванию
    frequencies = dict(sorted(frequencies.items(), key=lambda item: item[1], reverse=True))
    return frequencies

frequencies = char_freq("Pract4.files/zadanie3.3.txt")
for i in frequencies.items():
    print(i)