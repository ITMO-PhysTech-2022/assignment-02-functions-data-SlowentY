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
    sa = s1.difference(s2)
    sb = s2.difference(s1)

    if len(sa) == 0 and len(sb) != 0:
        return True
    elif len(sa) == 0:
        return False
    else:
        return min(sa) < min(sb)



# DICTIONARIES

def merge(d1: dict, d2: dict, recursive: bool = False):
    """
    Функция принимает два json-словаря и возвращает результат их объединения
    (при наличии одинаковых ключей recursive=False означает, что надо оставить
    значение из d1, а recursive=True - что значения надо объединить рекурсивно)
    """
    if not recursive:
        return {**d2, **d1}
    else:
        universum = d1
        for key1 in d2:
            if key1 in d1.keys():
                if type(d1[key1]) == dict and type(d2[key1]) == dict:
                    universum[key1] = merge(d1[key1], d2[key1], True)
        else:
            return {**d2, **d1}
        return universum


def translate_back(d: dict[str, list[str]]):
    """
    Функция принимает словарь, задающий возможные способы перевода слов с
    одного языка на другой, и возвращает словарь, описывающий перевод в
    обратном направлении
    """
    dn = dict()
    for key in d.keys():
        for item in d[key]:
            try:
                ex = len(dn[item])
            except:
                dn[item] = []
            dn[item].append(key)
    return dn
