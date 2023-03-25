a = ('S', 'o', 'r', 'r', 'y', ' ', 'f', 'o', 'r', ' ', 't' , 'u', 'p', 'l', 'e')
for i in a:
    print(i, end='')
print('\n')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.checkbox import CheckBox
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout

from kivy.graphics import Rectangle, Ellipse, RoundedRectangle, Color
from kivy.core.window import Window
from kivy.properties import ListProperty


Window.borderless = True
Window.size = (400, 500)
Window.clearcolor = (3/255, 53/255, 78/255, 1)
Window.left = 0
Window.top = 0

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


class MyTabbedPanelItem(TabbedPanelItem):

	background_normal = ""


class MyButton(Button):

    pass


class MyLabel(Label):

	pass
			

class MyApp(App):

	def __init__(self):
		super().__init__()
		self.label = Label(text='Новая задача:', size_hint=(1, 0.1))
		self.save_btn = MyButton(text = 'Сохранить', size_hint = (1, 0.1), background_normal = 'Icons/int_btn.png')

		self.writer = TextInput(size_hint = (1, 0.503))
		self.label2 = Label(text = 'Удалить задачу:', size_hint = (1, 0.1))

		self.rm_selection = MySpinner(size_hint = (1, 0.07), text = 'Выберите из списка', background_normal = "")
		Back.add_removing_el(self)

		self.rm_btn = MyButton(text = 'Удалить', size_hint = (1, 0.1), background_normal = 'Icons/int_btn_rev.png')

		
	def add_task_with_btn(self, state):
		text = self.writer.text
		if text != '':
			if text[0] == ' ':
				TXT.clear_txt()# а нужен ли этот метод он медленный
			else:
				TXT.clear_txt(self)
				text = '0' + text
				TXT.backup_tasks(self, text)
				Back.add_task_to_screen(self,text)
				Back.add_removing_el(self)


	def build(self):
		self.title = 'task manager'

		self.tasks_tab = MyTabbedPanelItem(text = 'Список задач')
		self.config_tab = MyTabbedPanelItem(text = 'Управление')
		self.tabs = TabbedPanel(default_tab = self.config_tab)
		self.tasks_tab.background_normal = 'Icons/my_tab.xcf'
		self.tasks_tab.background_down = 'Icons/int_btn.png'
		self.config_tab.background_normal = 'Icons/my_tab.xcf'
		self.config_tab.background_down = 'Icons/int_btn.png'

		self.box = BoxLayout(orientation = 'vertical', spacing = 5)
		self.box.add_widget(self.label)
		self.box.add_widget(self.save_btn)
		self.box.add_widget(self.writer)
		self.box.add_widget(self.label2)
		self.box.add_widget(self.rm_selection)
		self.box.add_widget(self.rm_btn)

		self.tasks = GridLayout(cols = 2)

		self.tasks_tab.add_widget(self.tasks)
		self.config_tab.add_widget(self.box)
		self.tabs.add_widget(self.tasks_tab)
		self.tabs.add_widget(self.config_tab)

		Back.func(self)
		self.save_btn.bind(on_press = self.add_task_with_btn)
		self.rm_btn.bind(on_press = self.rm_task_from_tab)

		return self.tabs


	def rm_task_from_tab(self, state):
		text = self.rm_selection.text
		with open ('tasks.txt', 'r') as tasks:
			lines = ''
			for line in tasks:
				if line[1:-1] == text:
					pass
				else:
					lines += line
		with open ('tasks.txt', 'w') as tasks:
			tasks.write(lines)
		for wid in self.grid:
			if self.grid[wid].text[3:-4] == text:
				self.tasks.remove_widget(wid)
				self.tasks.remove_widget(self.grid[wid]) #todo: убрать утечку памяти
		Back.add_removing_el(self)
		self.rm_selection.text = 'Выберите из списка'


class Back():
	MyApp.grid = dict()

	def func(self):
		Back.init_tasks(self)


	def checkbox_callback(self, value):
		self.cb_label = MyApp.grid[self]
		text = self.cb_label.text[3:-4]
		if value:
			self.cb_label.text = f'[s]{text}[/s]'
			TXT.set_checked_in_txt(self, text)
		else:
			self.cb_label.text = f'[i]{text}[/i]'
			TXT.set_unchecked_in_txt(self, text)


	def init_tasks(self): #text <= 42 el
		with open('tasks.txt','r') as tasks:
			for line in tasks:
				if line == '\n' or line[0] == ' ':
					pass
				else:
					Back.add_task_to_screen(self, line[:-1])


	def add_task_to_screen(self, text):
		self.checkBox = CheckBox(width = 50, size_hint_x = None)
		self.tasks.add_widget(self.checkBox)
		self.writer.text = ''
		if text[0] == '0':
			self.checkBox.active = False
			self.cb_label = MyLabel(markup = True)
			self.cb_label.text = f'[i]{text[1:]}[/i]'
		else:
			self.checkBox.active = True
			self.cb_label = MyLabel(markup = True)
			self.cb_label.text = f'[s]{text[1:]}[/s]'
		self.grid[self.checkBox] = self.cb_label
		self.tasks.add_widget(self.cb_label)
		self.checkBox.bind(active = Back.checkbox_callback)


	def add_removing_el(self):
		lines = tuple()
		with open('tasks.txt','r') as tasks:
			for line in tasks:
				if line == '\n' or line[0] == ' ':
					pass
				else:
					lines += (line[1:-1], )
			self.rm_selection.values = lines
		

class TXT(Back):
	def set_checked_in_txt(self, text):
			with open('tasks.txt','r') as tasks:
				lines = ''
				for line in tasks:
					if line[1:-1] == text:
						list_line = list(line)
						list_line[0] = '1'
						line = ''.join(list_line)
						lines += line
					else:
						lines += line
					with open('tasks.txt', 'w') as tasks:
						tasks.write(lines)


	def set_unchecked_in_txt(self, text):
			with open('tasks.txt','r') as tasks:
				lines = ''
				for line in tasks:
					if line[1:-1] == text:
						list_line = list(line)
						list_line[0] = '0'
						line = ''.join(list_line)
						lines += line
					else:
						lines += line
					with open('tasks.txt', 'w') as tasks:
						tasks.write(lines)


	def clear_txt(self):
		with open('tasks.txt','r') as tasks:
			lines = ''
			for line in tasks:
				if line == '\n' or line[0] == ' ':
					pass
				else:
					lines += line
		with open('tasks.txt', 'w') as tasks:
			tasks.write(lines)


	def backup_tasks(self, text):
		with open('tasks.txt', 'a') as tasks:
			tasks.write(f'{text}\n')
	


if __name__ == '__main__':
	MyApp().run()		