# class A:
#     def __init__(self, width, height):
#         self.width = width
#         self.heigth = height
#
#     def show_square(self):
#         print(self.width * self.heigth)
#
#     def show_perimeter(self):
#         print(2 * self.width + self.heigth * 2)
#
# result_1 = A(4, 2)
# result_2 = A(3, 7)
# result_3 = A(2, 5)
#
# result_1.show_square()
# result_1.show_perimeter()
#
# result_2.show_square()
# result_2.show_perimeter()
#
# result_3.show_square()
# result_3.show_perimeter()
#
#
from distutils.command.check import check


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



