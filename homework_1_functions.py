# Вводится целое число (любого размера).
# Написать функцию, которая разобьет это число на разряды символом "пробел", Функция возвращает тип данных str
# 1234567 -> 1 234 567, 267 -> 267, 34976 -> 34 976`

def split_number(num: int) -> str:
    num = str(num)
    if num.isdigit():
        num = str(num)
        num = [num[i] for i in range(len(num))]
        num.reverse()
        num = "".join(num)
        result = [num[i] + ' ' if i % 3 == 0 and i != 0 else num[i] for i in range(len(num))]
        result.reverse()
        return ''.join(result)
    else:
        print('Аргументом должны быть только цифры.')


print(split_number(1234567))
print(split_number(267))
print(split_number(34976))
print(split_number([12355]))
print(split_number(1234))

# Написать функцию, которая принимает строку текста и изменяет снейк_кейс на КамелКейс и наоборот
# my_first_func -> MyFirstFunc, AnotherFunction -> another_function


def convert_string(string: str) -> str:
    try:
        if "_" in string:
            list_string = string.split('_')
            conv_string = [word.title() for word in list_string]
        else:
            conv_string = ["_" + string[i].lower() if string[i] in "ZXCVBNMASDFGHJKLQWERTYUIOP" and i != 0
                       else string[i].lower() for i in range(len(string))]
        return ''.join(conv_string)
    except TypeError:
        print("Введите строку.")


print(convert_string('my_first_func'))
print(convert_string('AnotherFunction'))
print(convert_string(12312))


# Написать функцию, которая принимает на вход квадратное уравнение (одной строкой) и возвращает его корни,
# либо сообщает, что их нет
# "x**2 - 11*x + 28 = 0" -> x_1 = 4, x_2 = 7


def solve_equation(string: str) -> tuple:
    string = string.replace(" ", "")
    if '**2' not in string or 'x' not in string or not string.endswith('0'):
        print('Неверное написание уровнения.\nДолжны выполняться условия:\nОбязательно должен быть квадрат переменной\n'
              'Переменная обозначаться через символ "x"\nВ правой половине уравнения только 0.')
    equation = string.split('**2')
    if '+' in equation[0] or equation[0].count('-') > 1:
        print('Неверное написание уровнения.\nПорядок членов уровнения строго a, b, с')
    else:
        equation[1] = equation[1].rstrip('=0')
        if equation[0].startswith('x'):
            a = 1
        elif equation[0].startswith('-x'):
            a = -1
        else:
            a = int(equation[0].rstrip("*x"))
        if equation[1].startswith('x') and len(equation[1].lstrip('x')) != 0:
            b = 1
            c = int(equation[1]).lstrip('x')
        elif equation[1].startswith('-x') and len(equation[1].lstrip('-x')) != 0:
            b = -1
            c = int(equation[1].lstrip('-x'))
        elif 'x' not in equation[1] and len(equation[1]) != 0:
            b = 0
            c = int(equation[1])
        elif 'x' not in equation[1] and len(equation[1]) == 0:
            b = 0
            c = 0
        elif (equation[1].count('-') == 1 and '+' not in equation[1]) or (
                equation[1].count('+') == 1 and '-' not in equation[1]):
            c = 0
            if equation[1].startswith('-x'):
                b = -1
            elif equation[1].startswith('x'):
                b = 1
            else:
                b = int(equation[1].rstrip('*x'))
        else:
            b_c = equation[1].split('*x')
            b = int(b_c[0])
            c = int(b_c[1])
        discr = b ** 2 - 4 * a * c
        if discr < 0:
            print('Уравнение не имеет решения')
        elif discr == 0:
            x_1 = (-b + (discr ** (1 / 2))) / (2 * a)
            print('У уровнения одно решение : {}'.format(x_1))
        else:
            x_1 = (-b + (discr ** (1 / 2))) / (2 * a)
            x_2 = (-b - (discr ** (1 / 2))) / (2 * a)
            print('x_1 = {0}, x_2 = {1}'.format(x_1, x_2))


solve_equation('x**2 - 11*x + 28 = 0')

# Шифр Цезаря.
# Написать функцию, которая будет принимать два аргумента: слово (str) и ключ (int).
# Результат выполнения функции - шифрованое слово по методоту Шифр Цезаря.
# Написать вторую функцию, которая будет проводить обратный процесс (или написать одну, выполняющую оба действия)
# 'dog', 3 -> 'grj', 'python', 5 -> 'udymts'


def сaesar_shift(word: str, step: str) -> str:
    step = int(step)
    alfabet_letter = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
                      'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
                      't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    alfabet_digit = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
                     11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's',
                     20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}
    word = word.lower()
    cod = ''
    for letter in word:
        i = alfabet_letter[letter] + step
        if i <= 26:
            cod += alfabet_digit[i]
        else:
            i -= 26
            cod += alfabet_digit[i]
    return cod


print(сaesar_shift('python', '5'))
