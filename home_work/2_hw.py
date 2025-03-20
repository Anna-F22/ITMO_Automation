def task_1(a, b, c, d, e)-> list:
    return type (a), type (b), type (c), type (d), type (e)

print(task_1(7, 2.8, 'Солнышко', [7,8], True))

#еще вариант решения
def task_1(a: int, b = float, c= str, d= list, e= bool)-> list:
    return type (a), type (b), type (c), type (d), type (e)

print(task_1(7, 2.8, 'Солнышко', [7,8], True))


def task_2(a = [1, 2, 3, 5, 8, 13, 21]) -> int:
    return a[0:3]

print(task_2())
# 1, 2, 3, 5, 8, 13, 21 - последовательность Фибоначчи

def task_3(a: int) -> int:
    return a*a

print(task_3(5))