# -*- coding: utf-8 -*-

# Guido van Rossum <guido@python.org>

def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print(
        'Утка взяла зонтик. Она вышла из дома. '
        'Пошел дождь. '
        'Подождать такси до бара или пойти пешком?️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step3_taxi()
    return step3_no_taxi()


def step2_no_umbrella():
    print(
        'Утка решила, что зонтик ей не нужен. '
        'Она выходит на улицу. '
        'Наступает сумасшедший ливень, весь наряд промок. '
        'Пришлось вернуться домой. '
        'Она решила пойти в бар завтра. '
        'Наступает следующий день.'
    )
    return step1()


def step3_taxi():
    print(
        'Утка вызвала такси. Ну не мокнуть же под дождем? '
        'Откликнулся водитель с рейтингом 4.4. '
        'Маловато. Вызвать другого таксиста?'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step4_change()
    return step4_no_change()


def step3_no_taxi():
    print(
        'Утка решила, что пойдет пешком. '
        'Но погода была ужасной. зонтик выбило и унесло. '
        'Весь наряд промок. '
        'Пришлось вернуться домой. '
        'Она решила пойти в бар завтра. '
        'Наступает следующий день. '
    )
    return step1()


def step4_change():
    print(
        'Утка перезаказала такси. '
        'Приехал водитель с рейтингом 4.9. '
        'Отправиться в путь до бара? '
        'Или попытать удачу в поиске водителя 5.0?'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step5_final()
    return step5_no_final()


def step4_no_change():
    print(
        'Утка ждала водителя с рейтингом 4.4. '
        'Что-то пошло не так. '
        'Водитель долго не ехал. '
        'Телефон разрядился. '
        'Утка решила, что пойдет пешком. '
        'Но погода была ужасной. зонтик выбило и унесло. '
        'Весь наряд промок. '
        'Пришлось вернуться домой. '
        'Она решила пойти в бар завтра. '
        'Наступает следующий день.'
    )
    return step1()


def step5_final():
    print(
        'Утка добралась до бара! '
        'Вы восхитительны!'
    )


def step5_no_final():
    print(
        'Утка решила, что нужно дождаться водителя 5.0. '
        'Заказала еще раз. '
        'Но никто не ехал, повышенный спрос. '
        'Телефон разрядился. '
        'Утка решила, что пойдет пешком. '
        'Но погода была ужасной. зонтик выбило и унесло. '
        'Весь наряд промок. '
        'Пришлось вернуться домой. '
        'Она решила пойти в бар завтра. '
        'Наступает следующий день.'
    )
    return step1()


if __name__ == '__main__':
    step1()
