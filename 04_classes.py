class App():
    def init_app(self):
        print('My class init method')

    def do_something(self):
        print('Swipe that mfka')
        self.third_method()

    def third_method(self):
        print('What is going on?')


class Mailing(App):
    def mail_to(self):
        print('Email has been sent')


app = App()
mail = Mailing()

app.init_app()
app.do_something()
mail.mail_to()
mail.do_something()


