def argument(a, b):
    if a > b:
        return 'a'
    else:
        return 'b'

print(argument(8,7))



def differ(x, y):
    if x - y == 135 or y - x == 135:
        print ('yes')
    else:
        print ('No')

differ(136, 1)


def season(time_of_year):
    if time_of_year in range(3,5):
        print('Весна')
    elif 6 <= time_of_year <= 8:
        print('Лето')
    elif time_of_year in range(9,11):
        print('Осень')
    elif time_of_year == 12 or time_of_year == 1 or time_of_year == 2:
        print('Зима')
    else:
        print('Введите корректное число')

season(9)

def description(c, d, z):
    if c > 10 and d > 10 and z > 10:
        print('yes')
    else:
        print('no')

description(13, 78, 13)


def my_positive(my_list = [10, -2, -3, -5, 8]) -> int:
    pos = 0
    for n in my_list:
        if n > 0:
            pos += 1
    return pos




def quantity(a, b):
    return 29*12*a + 29*b

print(quantity(1, 2))