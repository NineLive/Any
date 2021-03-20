"""
Новый вызов для смелых, ловких и умелых! Правила те же: сигнатуру не менять, импортировать только
из стандартной бибилиотеки, решения слать мне в личку,
предварительно внимательно проверив и убедившись что все по ТЗ. Не жалейте тестов!
Реализовать функцию to_russian_string(value: int) -> str:, которая примнимает на вход целое число
от 0 до 999 (включая) и возвращает его письменное преставление на русском языке строчными буквами,
например 0='ноль', 111='сто одиннадцать'. Только 1 пробел между словами!
При неверных значениях бросать любое адекватное исключение. Кто не силен в русском, советую проверять
по гуглу как пишутся те или иные числительные, чтобы потом не удивляться.#task
"""


def to_russian_string(value: int) -> str:
    """
    :param value: Takes an integer from 0 to 999
    :return: Returns the word string obtained from the value in Russian lowercase letters
    """
    if not (isinstance(value, int) and (0 <= value <= 999)):
        raise ValueError('Value must be int in range from 0 to 999')
    value = str(value)
    if len(value) == 3:
        result = get_len3(value)
    elif len(value) == 2:
        result = get_len2(value)
    else:
        result = get_len1(value)
    return result


def get_len3(value):
    if int(value) % 10 == 0:  # 110,220,330...
        if int(value) % 100 == 0:  # 100,200,300...
            result = f'{hundreds[value[0]]}'
        else:
            result = f'{hundreds[value[0]]} {tens[value[1]]}'

    elif 10 < int(value[1:]) < 20:  # 111,212,311..
        result = f'{hundreds[value[0]]} {units2[value[2]]}'
    elif value[1] == '0':  # 105, 209, 304...
        result = f'{hundreds[value[0]]} {units[value[2]]}'
    else:  # 145,227,546.. any
        result = f'{hundreds[value[0]]} {tens[value[1]]} {units[value[2]]}'
    return result


def get_len2(value):
    if value[1] == '0':  # 20, 30, 40...
        result = f'{tens[value[0]]}'
    elif int(value) < 20:  # 11, 12, 13...
        result = f'{units2[value[1]]}'
    else:  # 27, 34, 45... any
        result = f'{tens[value[0]]} {units[value[1]]}'
    return result


def get_len1(value):
    return f'{units[value[0]]}'


units = {
    '0': 'ноль',
    '1': 'один',
    '2': 'два',
    '3': 'три',
    '4': 'четыре',
    '5': 'пять',
    '6': 'шесть',
    '7': 'семь',
    '8': 'восемь',
    '9': 'девять'}

units2 = {
    '1': 'одиннадцать',
    '2': 'двенадцать',
    '3': 'тринадцать',
    '4': 'четырнадцать',
    '5': 'пятнадцать',
    '6': 'шестнадцать',
    '7': 'семнадцать',
    '8': 'восемнадцать',
    '9': 'девятнадцать'}

tens = {
    '1': 'десять',
    '2': 'двадцать',
    '3': 'тридцать',
    '4': 'сорок',
    '5': 'пятьдесят',
    '6': 'шестьдесят',
    '7': 'семьдесят',
    '8': 'восемьдесят',
    '9': 'девяносто'}

hundreds = {
    '1': 'сто',
    '2': 'двести',
    '3': 'триста',
    '4': 'четыреста',
    '5': 'пятьсот',
    '6': 'шестьсот',
    '7': 'семьсот',
    '8': 'восемьсот',
    '9': 'девятьсот'}

if __name__ == "__main__":
    assert to_russian_string(0) == 'ноль'
    assert to_russian_string(1) == 'один'
    assert to_russian_string(10) == 'десять'
    assert to_russian_string(11) == 'одиннадцать'
    assert to_russian_string(21) == 'двадцать один'
    assert to_russian_string(100) == 'сто'
    assert to_russian_string(101) == 'сто один'
    assert to_russian_string(110) == 'сто десять'
    assert to_russian_string(111) == 'сто одиннадцать'
    assert to_russian_string(199) == 'сто девяносто девять'
