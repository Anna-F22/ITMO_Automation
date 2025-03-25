from task_9_checks import Checks

class Input(Checks):
    def test_check(self, loc):
        super().__init__(loc)

    def second(self):
        Checks.check_text()


b = Input('testing_one')
print(b.second())






#
# class Parent():
#
#     def show(self):
#         print("Inside Parent")
#
#
# class Child(Parent):
#
#     def show(self):
#
#         Parent.show(self)
#         print("Inside Child")
#
#
#
# obj = Child()
# obj.show()
#
#
#
#
# from qwe import B
# class A:
#     def __init__(self, _list, value):
#         self._list = _list
#         self.value = value
#
#         self.b = B(self._list)
#
#     def qw(self):
#         if self._list[0] == self.value:
#             self.b.calculate()
#
#
# my_list = [1, 1, 2]
#
# a = A(my_list, 1)
# a.qw()


#
# class Button(Cheks):
#     def __init__(self, loc, text):
#         self.loc = loc
#         self.text = text
#
# class Title(Cheks):
#     def __init__(self, loc, text):
#         self.loc = loc
#         self.text = text
#
# class Link(Cheks):
#     def __init__(self, loc, text):
#         self.loc = loc
#         self.text = text

# find_search = Input()
# print(find_search.check_text())

# search = Input('input#search', 'Страница')
#
# print(search.loc)
# print(search.text)
#
#
# find = Button('button#find', 'Поиск')
#
# print(find.loc)
# print(find.text)
#
# document = Title('title#document', 'Заголовок')
#
# print(document.loc)
# print(document.text)
#
# head = Link('link#head', 'Начало')
#
# print(head.loc)
# print(head.text)