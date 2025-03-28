class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.heigth = height

    def show_square(self):
        print(self.width * self.heigth)

    def show_perimeter(self):
        print(2 * self.width + self.heigth * 2)

result_1 = Rectangle(4, 2)
result_2 = Rectangle(3, 7)
result_3 = Rectangle(2, 5)

result_1.show_square()
result_1.show_perimeter()

result_2.show_square()
result_2.show_perimeter()

result_3.show_square()
result_3.show_perimeter()


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def subtraction (self):
        return self.a - self.b

home = Math(10, 2)
print(home.addition())
print(home.multiplication())
print(home.division())
print(home.subtraction())


class Site:
    def __init__(self, text, type, loc = None):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        return 'Клик по кнопке {}'.format(self.text)


textbox = Site('Text Box', 'Кнопка')
checkbox = Site('Check Box', 'Кнопка')
radiobutton = Site('Radio Button', 'Кнопка')
webtables = Site('Web Tables', 'Кнопка')
buttons = Site('Buttons', 'Кнопка')
links = Site('Links', 'Кнопка')
brokenlinks = Site('Broken Links - Images', 'Кнопка')
upload = Site('Upload and Download', 'Кнопка')
dinamic = Site('Dinamic Properties', 'Кнопка')


print(textbox.text)
print(checkbox.text)
print(radiobutton.text)
print(webtables.text)
print(buttons.text)
print(links.text)
print(brokenlinks.text)
print(upload.text)
print(dinamic.text)

print('\n')

print(textbox.click())
print(checkbox.click())
print(radiobutton.click())
print(webtables.click())
print(buttons.click())
print(links.click())
print(brokenlinks.click())
print(upload.click())
print(dinamic.click())



