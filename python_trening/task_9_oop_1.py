from task_9_checks import Checks

class Input(Checks):

    def text_one(self):
        super().check_text()

class Button(Checks):
    def text(self):
        super().check_text()

class Title(Checks):
    def heading(self):
        super().check_text()

class Link(Checks):
    def connect(self):
        super().check_text()


incoming = Input('#income')
incoming.text_one()

btn_first = Button('#btn-first')
btn_first.text()

title_head = Title('#heading_new')
title_head.heading()

conn_link = Link('#connect_test')
conn_link.connect()
