from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

import random

Window.size = (400, 500)
# Window.clearcolor = (3/255, 53/255, 78/255, 1)

class MyButton(Button):
    pass

class MyApp(App):

    def __init__(self):
        super().__init__()
        print(self, '1234567')
        self.some_button = MyButton(text = 'click to change color')
        self.writer = TextInput()



    def build(self):

        self.box = BoxLayout(orientation = 'vertical')
        self.box.add_widget(self.some_button)
        self.box.add_widget(self.writer)
        # self.some_button.bind(on_press = Functions.change_color)
        self.some_button.bind(on_press = self.change_color)

        return self.box

    def change_color(self, *args):
        self.writer.background_color = (random.randint(0,255)/255, random.randint(0,255)/255, random.randint(0,255)/255, 1)


\

class Functions(MyApp):

    # def change_color(self, *args):
    #     MyApp.writer.background_color = (random.randint(0,255)/255, random.randint(0,255)/255, random.randint(0,255)/255, 1)
    pass

if __name__ == '__main__':
    MyApp().run()   
