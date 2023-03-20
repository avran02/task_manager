from kivy.app import App
from kivy.uix.button import Button
from kivy.graphics import RoundedRectangle

class RoundButton(Button):
    def __init__(self, **kwargs):
        super(RoundButton, self).__init__(**kwargs)

        self.border_radius = [50]
        with self.canvas:
            RoundedRectangle(pos=self.pos, size=self.size, radius=self.border_radius)
        self.bind(pos=self.redraw, size=self.redraw)

    def redraw(self, *args):
        self.canvas.clear()
        with self.canvas:
            RoundedRectangle(pos=self.pos, size=self.size, radius=self.border_radius)

class MyApp(App):
    def build(self):
        return RoundButton(text="Hello World", size_hint=(0.5, 0.5), pos_hint={"center_x": 0.5, "center_y": 0.5}, background_color = (1, 0, 0, 1))

if __name__ == "__main__":
    MyApp().run()
