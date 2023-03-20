from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.checkbox import CheckBox
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.lang import Builder
# from kivy.uix.separator import Separator



from kivy.graphics import Rectangle, Ellipse, RoundedRectangle, Color
from kivy.core.window import Window
from kivy.properties import ListProperty


Window.size = (400, 500)
Window.clearcolor = (3/255, 53/255, 78/255, 1)

Builder.load_file('styles.kv')

class SpinnerOptions(SpinnerOption):

    def __init__(self, **kwargs):
        super(SpinnerOptions, self).__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (104/255, 199/255, 246/255, 1)
        self.color = (0, 0, 0, 1)
        self.height = 34


class MySpinner(Spinner):
    def __init__(self, **kwargs):
        super(MySpinner, self).__init__(**kwargs)
        self.option_cls = SpinnerOptions





class MyButton(Button):

    pass


class MyLabel(Label):
	pass

class MyApp(App):

	def __init__(self):
		super().__init__()
		self.label = Label(text='Новая задача:', size_hint=(1, 0.1))
		self.save_btn = MyButton(text = 'Сохранить', size_hint = (1, 0.1), background_normal = 'some/int_btn.png')

		# self.save_btn_label = MyLabel(text = 'Сохранить', color = (0, 0, 0, 1))
		self.save_btn.bind(on_press = MyApp.save_task)

		self.writer = TextInput(size_hint = (1, 0.503))
		self.label2 = Label(text = 'Удалить задачу:', size_hint = (1, 0.1))

		self.rm_selection = MySpinner(values = ('task1', 'task2', 'task3', 'task4'), size_hint = (1, 0.07), text = 'Выберите из списка', background_normal = "")
		# self.rm_selection.add_widget(Separator(color = (3/255, 53/255, 78/255, 1)))

		self.rm_btn = MyButton(text = 'Удалить', size_hint = (1, 0.1), background_normal = 'some/int_btn_rev.png')
		# self.rm_btn_label = MyLabel(text = 'Удалить задачу', color = (0, 0, 0, 1))



	def save_task(self):
		print('any')
	

	def build(self):
		self.title = 'task manager'
		
		tasks_tab = TabbedPanelItem(text = 'Список задач', background_normal = "")
		config_tab = TabbedPanelItem(text = 'Управление', background_normal = "")
		tabs = TabbedPanel(default_tab = tasks_tab)
		tasks_tab.background_normal = 'some/int_btn_rev.png'
		tasks_tab.background_down = 'some/int_btn.png'
		config_tab.background_normal = 'some/int_btn_rev.png'
		config_tab.background_down = 'some/int_btn.png'

		# self.save_btn.add_widget(self.save_btn_label)
		# self.rm_btn.add_widget(self.rm_btn_label)

		box = BoxLayout(orientation = 'vertical', spacing = 5)
		box.add_widget(self.label)
		box.add_widget(self.save_btn)
		box.add_widget(self.writer)
		box.add_widget(self.label2)
		box.add_widget(self.rm_selection)
		box.add_widget(self.rm_btn)

		config_tab.add_widget(box)
		tabs.add_widget(tasks_tab)
		tabs.add_widget(config_tab)
		return tabs


if __name__ == '__main__':

	MyApp().run()		