import random
import os
from datetime import datetime


def save_words(word_list):
    with open('words.txt', 'w', encoding='utf-8') as f:
        for word in word_list:
            f.write(
                f'{word["en"]}|{word["ru"]}|{word["desc"]}|{word["category"]}'
                '\n'
            )


def load_words():
    default_words = [
        {"en": "sun", "ru": "солнце", "desc": "Светило неба",
         "category": "basic"},
        {"en": "cat", "ru": "кошка", "desc": "Мяукающий питомец",
         "category": "basic"},
        {"en": "dog", "ru": "собака", "desc": "Лучший друг человека",
         "category": "basic"},
        {"en": "hello", "ru": "привет", "desc": "Приветствие при встрече",
         "category": "basic"},
        {"en": "car", "ru": "машина", "desc": "кусок метала на колесах",
         "category": "basic"},
        {"en": "doctor", "ru": "доктор", "desc": "добрый ....  Айболит",
         "category": "basic"},
        {"en": "man", "ru": "мужчина", "desc": "взрослый мальчик",
         "category": "basic"},
        {"en": "girl", "ru": "девочка", "desc": "будущая мать",
         "category": "basic"},
        {"en": "boy", "ru": "мальчик", "desc": "будущий отец",
         "category": "basic"},
        {"en": "father", "ru": "отец", "desc": "глава семьи",
         "category": "basic"},
    ]

    if not os.path.exists('words.txt'):
        save_words(default_words)
        return default_words
    else:
        user_words = []
        with open('words.txt', 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split('|')
                if len(parts) == 3:
                    en, ru, desc = parts
                    category = 'basic'
                else:
                    en, ru, desc, category = parts
                user_words.append(
                    {'en': en, 'ru': ru, 'desc': desc, 'category': category}
                )
        return user_words


def start_game(words, category=None):
    if category:
        filtered = [w for w in words if w['category'] == category]
        print(f'Тренировка по категории: {category}')
    else:
        filtered = words
        print('Тренировка по всем категориям')
    if len(filtered) < 5:
        print('В вашем списке недостаточно слов, добавьте больше слов')
        return

    selected = random.sample(filtered, 5)
    print('\n--- Этап 1 ---')
    correct_translate = 0
    wrong_translate = 0
    for select in selected:
        user_unswer = input(f'Переведи: {select["ru"]}:').strip().lower()
        correct_unswer = select['en'].lower()
        if user_unswer == correct_unswer:
            correct_translate += 1
            print('Верно')
        else:
            wrong_translate += 1
            print(f'Правильный вариант: {select["en"]}')
    print(f'Правильно: {correct_translate}. Неправильно: {wrong_translate}')

    print('\n --- Этап 2 ---')
    random.shuffle(selected)
    correct_desc = 0
    wrong_desc = 0
    for select in selected:
        user_test = input(
            f'Переведи по описанию: {select["desc"]}:'
            ).strip().lower()
        answer_test = select['en'].lower()
        if user_test == answer_test:
            correct_desc += 1
            print('Правильно')
        else:
            wrong_desc += 1
            print(f'Правильный вариант: {select["en"]}')
    print(f'Правильно: {correct_desc}. Неправильно: {wrong_desc}')

    total_correct = correct_desc + correct_translate
    total_wrong = wrong_desc + wrong_translate
    print(f'Всего верных ответов: {total_correct}.'
          f'Всего неверных ответов: {total_wrong}.')
    test_day = datetime.now()
    formated_test_time = test_day.strftime('%Y/%m/%d %H:%M')
    result = (
        f'Вего верно: {total_correct}\n'
        f'Всего не верно: {total_wrong}\n'
        f'<-={formated_test_time}=->'
        '\n'
        '===============================\n'
    )
    history = open('history.txt', 'a', encoding='utf-8')
    history.write(result + '\n')
    history.close()


def add_words(words):
    print('\n ---Добавление нового слова---')
    en = input('Английское слово: ').strip().lower()
    ru = input('Русский перевод: ').strip().lower()
    desc = input('Описание: ').strip()
    category = input('Введи категорию: ').strip()
    words.append({'en': en, 'ru': ru, 'desc': desc, 'category': category})
    save_words(words)
    print(f'Слово {en} добавлено и сохранено программой')


def choose_category(words):
    categories = sorted(set(w['category'] for w in words))
    print('--- Выбор категории ---')
    print('0. Все категории')
    for i, cat in enumerate(categories, start=1):
        print(f'{i}.  {cat}')
    choice = input('Ваш выбор: ').strip()
    if choice == '0':
        return None
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(categories):
            return categories[idx]
        else:
            print('Неверный номер. Выбраны все категории.')
            return None
    except ValueError:
        print('Неверный ввод')
        return None


def main():
    words = load_words()
    current_category = None
    while True:
        print(" --- RU*ENG ---")
        print("1. Начать тренировку")
        print("2. Добавить новое слово")
        print("3. Выбрать категорию")
        print("0. Выход")
        if current_category:
            print(f'Текущая категория: {current_category}')
        else:
            print('Текущая категоия: все')
        choice = input('Ваш выбор:').strip()
        if choice == '1':
            start_game(words, current_category)
        elif choice == '2':
            add_words(words)
        elif choice == '3':
            new_cat = choose_category(words)
            if new_cat is not None:
                current_category = new_cat
                print(f'Категория изменена на: {current_category}')
            else:
                current_category = None
                print('Выбраны все категории')
        elif choice == '0':
            print('Адьёс')
            break
        else:
            print('Неверный ввод')


if __name__ == "__main__":
    main()
