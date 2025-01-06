# Задача "Однокоренные":
def single_root_words(root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
        # Сравним совпадения слов
        if root_word.lower() in other_words[i].lower() or other_words[i].lower() in root_word.lower():
            same_words.append((other_words[i])) # Добавим в список однокоренные слова
    return same_words   # Выведем список


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
