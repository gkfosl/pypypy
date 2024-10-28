text = input ("Введите текст")

reserved_words = input("Введите список зарезервированных слов через пробел: ").split()

for word in reserved_words:
    text = text.replace(word, word.upper())

print(f"Измененный текст: {text}")
