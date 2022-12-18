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
caesar_decode = lambda s, shift: caesar_encode(s, -shift)


# LISTS

def extract_each(array: list, k: int, cyclic: bool = False):
    """
    Функция принимает массив array и число k, и возвращает массив, состоящий из
    каждого k-го элемента массива array
    (если передан cyclic=True, при достижении конца массива выбор элементов
    продолжается с начала, пока не достигнет уже выбранного элемента)
    """
    arrayNew = []
    indexes = []
    i = 0
    if len(array) != 0:
        if not cyclic:
            while i < len(array):
                arrayNew.append(array[i])
                i = i + k
        else:
            while i not in indexes:
                indexes.append(i)
                arrayNew.append(array[i])
                i = i + k
                while i >= len(array):
                    i = i - len(array)
    return arrayNew


# SETS

def compare(s1: set[int], s2: set[int]):
    """
    Функция принимает два множества чисел и возвращает результат их сравнения -
    меньшим считается то множество, в котором лежит наименьший из их не-общих
    элементов
    """
    print(s1)
    print(s2)
    if len(s2) == len(s1):
        if len(s1) != 0:
            if max(s2) > max(s1):
                print(True)
                return True
            elif max(s2) < max(s1):
                print(False)
                return False
            else:
                a = set()
                b = set()
                a.add(max(s1))
                b.add(max(s2))
                return compare(s1.difference(a),s2.difference(b))
        else:
            return False
    elif len(s1) > len(s2):
        print(False)
        return False
    elif len(s1) < len(s2):
        print(True)
        return True



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
