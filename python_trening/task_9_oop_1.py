class Input:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

class Button:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

class Title:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

class Link:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

search = Input('input#search', 'Страница')

print(search.loc)
print(search.text)


find = Button('button#find', 'Поиск')

print(find.loc)
print(find.text)

document = Title('title#document', 'Заголовок')

print(document.loc)
print(document.text)

head = Link('link#head', 'Начало')

print(head.loc)
print(head.text)