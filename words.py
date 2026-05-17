import random
words = [
    {"en": "sun", "ru": "солнце", "desc": "Светило неба"},
    {"en": "cat", "ru": "кошка", "desc": "Мяукающий питомец"},
    {"en": "dog", "ru": "собака", "desc": "Лучший друг человека"},
    {"en": "hello", "ru": "привет", "desc": "Приветствие при встрече"},
    {"en": "good night", "ru": "доброй ночи", "desc": "Пожелание перед сном"},
    {"en": "doctor", "ru": "доктор", "desc": "добрый ....  Айболит"},
    {"en": "man", "ru": "мужчина", "desc": "взрослый мальчик"},
    {"en": "girl", "ru": "девочка", "desc": "будущая мать"},
    {"en": "boy", "ru": "мальчик", "desc": "будущий отец"},
    {"en": "father", "ru": "отец", "desc": "глава семьи"},
]

selected = random.sample(words, 5)

print('\n--- Этап 1 : переведи слово ---')
correct_translate = 0
wrong_translate = 0
for select in selected:
    user_unswer = input(f'Как переводится {select["ru"]}:').strip().lower()
    correct_unswer = select['en'].lower()
    if user_unswer == correct_unswer:
        correct_translate += 1
        print(f'Верно')
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
        print(f'Правильно')
    else:
        wrong_desc += 1
        print(f'неправильно. ты должен был ответить: {select["en"]}')      
print(f'Правильно: {correct_desc}. Неправильно: {wrong_desc}')

total_correct = correct_desc + correct_translate
total_wrong = wrong_desc + wrong_translate
print(f'Всего верных ответов: {total_correct}.'
      f'Всего неверных ответов: {total_wrong}.')
