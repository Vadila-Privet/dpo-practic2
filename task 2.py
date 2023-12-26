import re
import os

my_number= 4
number=my_number % 3
print("Мой вариант:",number)

def Functionsplit(input_string: str) -> list:
    return str.split(input_string)

def Functionsplit2(input_string: str) -> list[str]:
    return re.split(r'\W+', str.lower(input_string))

def Function3() -> int:
    with open('task 2.py', encoding='utf-8') as file:
        contents = file.read()
        contents = Functionsplit(contents)
        count = 0
        for d in contents:
            if d == "def":
                count += 1
            else:
                continue
    return count

def Function4() -> list[str]:
    with open('task 2.py', encoding='utf-8') as file:
        contents = file.read()
        contents = Functionsplit(contents)
        count = []
        for d in range(len(contents)):
            if contents[d] == "def":
                name = contents[d + 1]
                end = name.find("(")
                count.append(str(name[:end]))
            else:
                continue
    return count


with open('Zergling.txt', encoding='utf-8') as txt_file:
    contents = txt_file.read()
    contents = Functionsplit2(contents)
    print('Все слова в файле')
    print(contents)
    # подсчет количества упоминаний каждого слова
    amount = {}
    for word in contents:
        if word in amount:
            amount[word] += 1
        else:
            amount[word] = 1
    print('Результат')
    # словарь с частотой слов
    for n in amount:
        print(str(n) + ' = ' + str(amount[n]) + ' раз(-а)')
print("Количество функций: " + str(Function3()) )
print("В файле прописаны функции " + str(Function4()))



