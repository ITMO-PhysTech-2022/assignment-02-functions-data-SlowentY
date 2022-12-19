from typing import Any, Callable
import random
import string


# BASE

def useless_function():
    """
    Эта функция должна ничего не делать и ничего не возвращать
    Зачем она здесь?... Никто не знает :(
    """

    if True is False:
        print('What is happening?...')
        print('Why is it happening?...')
        exit(1)  # beautiful death
        return UserWarning


def print_tree(size: int):
    """
    Функция выводит елочку из size сегментов размерами от 1 до size
    """

    def _print_segment(height: int):
        """
        Функция выводит сегмент елочки размера height
        """
        s = ""
        for i in range(1, height + 1):
            s = (size - i) * " "
            s = s + ("*" * (2 * i - 1))
            print(s)

    for i in range(1, size + 1):
        _print_segment(i)


# RECURSION

def generate_json(depth: int):
    """
    Функция генерирует словарь (dict) с уровнем вложенности depth
    """
    json = dict()

    if depth > 1:
        json = {'ЧИСТ': 'И!', 'ЧИ': 'СТИ!', 'Ч': 'ИСТИ!', 'ЧИСТИ!': generate_json(depth-1)}
    elif depth == 1:
        json = {'ЧИСТ': 'И!', 'ЧИ': 'СТИ!', 'ЭТО': 'КЛАССИКА!', 'ЭТО': 'ЗНАТЬ НАДО!'}
    else:
        pass
    return json


def wtf():
    """
    Функция wtf вызывает внутреннюю функцию _worker с некоторым аргументом
    и должна возвращать число 42
    """

    def _worker(x):
        if x == 0:
            return wtf()
        elif x % 2 == 1:
            return _worker(x // 3) + 1
        elif x % 982 == 0:
            return _worker(x + 982 if x < 10000 else x - 2) + 1
        else:
            return 0

    return _worker(0)


# ARGS, KWARGS

def mex(*args):
    """
    Функция принимает произвольное число аргументов и возвращает их mex,
    то есть minimal excluded - минимальное целое неотрицательное число,
    отсутствующее среди них
    """
    i = 0
    while True:
        if i not in args:
            return i
        else:
            i=i+1


def replace_keys(data: dict[str, Any], **kwargs: str):
    """
    Функция принимает словарь со строковыми ключами и набор аргументов вида
    key=value, и возвращает копию этого словаря, в котором каждый ключ key
    переименован в соответствующий ему value
    """
    ...


# HIGH ORDER

def count_calls_until(f: Callable, start, condition: Callable[..., bool]):
    """
    Функция принимает другую функцию от одного аргумента f, начальное значение
    и условие остановки, и возвращает количество последовательных вызовов f от
    значения start, пока результат не начнет удовлетворять условию остановки
    """
    calls = 0
    x = start
    while not condition(x):
        x = f(x)
        calls += 1

    return calls


def bind(f: Callable, **kwargs):
    """
    Функция принимает другую функцию от произвольного набора аргументов f и
    возвращает новую функцию, вызов которой идентичен вызову f, но с уже
    заранее подставленными указанными в **kwargs аргументами
    """
    ...
