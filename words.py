import random
import os


def save_words(word_list):
    with open('words.txt', 'w', encoding='utf-8') as f:
        for word in word_list:
            f.write(f'{word["en"]}|{word["ru"]}|{word["desc"]}\n')


def load_words():
    default_words = [
        {"en": "sun", "ru": "солнце", "desc": "Светило неба"},
        {"en": "cat", "ru": "кошка", "desc": "Мяукающий питомец"},
        {"en": "dog", "ru": "собака", "desc": "Лучший друг человека"},
        {"en": "hello", "ru": "привет", "desc": "Приветствие при встрече"},
        {"en": "car", "ru": "машина", "desc": "кусок метала на колесах"},
        {"en": "doctor", "ru": "доктор", "desc": "добрый ....  Айболит"},
        {"en": "man", "ru": "мужчина", "desc": "взрослый мальчик"},
        {"en": "girl", "ru": "девочка", "desc": "будущая мать"},
        {"en": "boy", "ru": "мальчик", "desc": "будущий отец"},
        {"en": "father", "ru": "отец", "desc": "глава семьи"},
    ]
    if not os.path.exists('words.txt'):
        save_words(default_words)
        return default_words
    else:
        user_words = []
        with open('words.txt', 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    en, ru, desc = line.split('|')
                    user_words.append({'en': en, 'ru': ru, 'desc': desc})
        return user_words


def start_game(words):
    if len(words) < 5:
        print('В вашем списке недостаточно слов, добавьте больше слов')
        return

    selected = random.sample(words, 5)
    print('\n--- Этап 1 : переведи слово ---')
    correct_translate = 0
    wrong_translate = 0
    for select in selected:
        user_unswer = input(f'Как переводится {select["ru"]}:').strip().lower()
        correct_unswer = select['en'].lower()
        if user_unswer == correct_unswer:
            correct_translate += 1
            print('Верно')
        else:
            wrong_translate += 1
            print(f'неверно. верно: {select["en"]}')
    print(f'Правильно: {correct_translate}.Неправильно: {wrong_translate}')

    print('\n --- Этап 2 : угадай слово по описанию ---')
    random.shuffle(selected)
    correct_desc = 0
    wrong_desc = 0
    for select in selected:
        user_test = input(
            f'Вспомни какое слово можно описать так: {select["desc"]}:'
            ).strip().lower()
        answer_test = select['en'].lower()
        if user_test == answer_test:
            correct_desc += 1
            print('Правильно')
        else:
            wrong_desc += 1
            print(f'неправильно. ты должен был ответить: {select["en"]}')   
    print(f'Правильно: {correct_desc}. Неправильно: {wrong_desc}')

    total_correct = correct_desc + correct_translate
    total_wrong = wrong_desc + wrong_translate
    print(f'Всего верных ответов: {total_correct}.'
          f'Всего неверных ответов: {total_wrong}.')


def add_words(words):
    print('\n ---Добавление нового слова---')
    en = input('Английское слово: ').strip().lower()
    ru = input('Русский перевод: ').strip().lower()
    desc = input('Описание: ').strip()
    words.append({'en': en, 'ru': ru, 'desc': desc})
    save_words(words)
    print(f'Слово {en} добавлено и сохранено программой')


def main():
    words = load_words()
    while True:
        print(" --- Учебный помощник слов ---")
        print("1. Начать тренировку")
        print("2. Добавить новое слово")
        print("0. Выход")
        choice = input('Ваш выбор:').strip()
        if choice == '1':
            start_game(words)
        elif choice == '2':
            add_words(words)
        elif choice == '0':
            print('Пока')
            break
        else:
            print('Неверный ввод')


if __name__ == "__main__":
    main()