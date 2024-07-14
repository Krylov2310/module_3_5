thanks='Благодарю за внимание :-)'
def visitka(task,task2, avtor):
    print(task)
    print(task2)
    print(avtor)
    print()


visitka('Самостоятельная работа по уроку "Рекурсия"', 'Задача "Рекурсивное умножение цифр"','Студент Крылов Эдуард Васильевич')


def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    print(f'Number: {number}, Stack: {first}')
    if len(str_number) <= 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))


# Исходный код:
result = get_multiplied_digits(40203)
print('Результат умножения стековых чисел =', result)
print()
print(thanks)
