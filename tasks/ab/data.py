# STRINGS
import re
def wordcount(s: str):
    """
    Функция принимает строку s и возвращает словарь, считающий количество
    вхождений каждого слова в нее
    (слова стоит рассматривать без учета регистра и без знаков препинания)
    """
    words = re.split("[ ,.!?&^1-9@#$%:;*()+]", s)
    countwords = dict()
    for word in words:
        if word != '':
            if word.lower() in countwords and word:
                countwords[word.lower()] = countwords[word.lower()] + 1
            else:
                countwords[word.lower()] = 1

    return countwords


def caesar_encode(s: str, shift: int):
    """
    Функция принимает строку s и величину сдвига shift и возвращает результат
    применения шифра Цезаря к строке, со сдвигом на shift влево
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sNew = ""
    sym = ""
    for i in range(0, len(s)):
        if (s[i] == " "):
            sNew = sNew + " "
            continue
        index = alphabet.find(s[i].lower()) - shift
        while index < 0:
            index = index + 26
        while index > 25:
            index = index - 26
        if (s[i].isupper()):
            sym = alphabet[index].upper()
        else:
            sym = alphabet[index]
        sNew = sNew + sym
    return sNew


# Упражнение на функции:
# определите дешифратор для шифра Цезаря, используя только вызов шифратора
caesar_decode = lambda s, shift: caesar_encode(s,-shift)

# LISTS

def extract_each(array: list, k: int, cyclic: bool = False):
    """
    Функция принимает массив array и число k, и возвращает массив, состоящий из
    каждого k-го элемента массива array
    (если передан cyclic=True, при достижении конца массива выбор элементов
    продолжается с начала, пока не достигнет уже выбранного элемента)
    """
    ...


# SETS

def compare(s1: set[int], s2: set[int]):
    """
    Функция принимает два множества чисел и возвращает результат их сравнения -
    меньшим считается то множество, в котором лежит наименьший из их не-общих
    элементов
    """
    ...


# DICTIONARIES

def merge(d1: dict, d2: dict, recursive: bool = False):
    """
    Функция принимает два json-словаря и возвращает результат их объединения
    (при наличии одинаковых ключей recursive=False означает, что надо оставить
    значение из d1, а recursive=True - что значения надо объединить рекурсивно)
    """
    ...


def translate_back(d: dict[str, list[str]]):
    """
    Функция принимает словарь, задающий возможные способы перевода слов с
    одного языка на другой, и возвращает словарь, описывающий перевод в
    обратном направлении
    """
    ...
