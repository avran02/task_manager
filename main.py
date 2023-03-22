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
		self.save_btn = MyButton(text = 'Сохранить', size_hint = (1, 0.1), background_normal = 'some/int_btn.png')


		# self.save_btn.bind(on_press = Back.save_task)

		self.writer = TextInput(size_hint = (1, 0.503))
		self.label2 = Label(text = 'Удалить задачу:', size_hint = (1, 0.1))

		self.rm_selection = MySpinner(values = ('task1', 'task2', 'task3', 'task4'), size_hint = (1, 0.07), text = 'Выберите из списка', background_normal = "")


		self.rm_btn = MyButton(text = 'Удалить', size_hint = (1, 0.1), background_normal = 'some/int_btn_rev.png')




	
	

	def build(self):
		self.title = 'task manager'
		
		self.tasks_tab = MyTabbedPanelItem(text = 'Список задач')
		self.config_tab = MyTabbedPanelItem(text = 'Управление')
		self.tabs = TabbedPanel(default_tab = self.tasks_tab)
		self.tasks_tab.background_normal = 'some/my_tab.xcf'
		self.tasks_tab.background_down = 'some/int_btn.png'
		self.config_tab.background_normal = 'some/my_tab.xcf'
		self.config_tab.background_down = 'some/int_btn.png'

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

		return self.tabs


class Back(App):
	MyApp.grid = dict()

	def func(self):
		Back.init_tasks(self)



	# def checkbox_callback(self, checkbox, value):
	# 	if value:
	# 		print("Checkbox is checked")
	# 	else:
	# 		print("Checkbox is unchecked")




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
			self.cb_label = MyLabel(text = f'[i]{text[1:]}[/i]', markup = True)
			
		else:
			self.checkBox.active = True
			self.cb_label = MyLabel(text = f'[s]{text[1:]}[/s]', markup = True)
			
		self.grid[self.checkBox] = self.cb_label
		self.tasks.add_widget(self.cb_label)
		print(self.grid)
		# self.checkBox.stateChanged.connect(lambda: self.on_checkBox_state_change)	


		# def on_checkBox_state_changed(self, text):
		# for wid in self.tab.findChildren(QtWidgets.QCheckBox):
		# 	if wid.objectName() == text[1:]:
		# 		state = wid.checkState()
		# 		if state == 2:  # 2 - значит, что чекбокс отмечен
		# 			font = QtGui.QFont()
		# 			font.setStrikeOut(True)
		# 			font.setPointSize(14)
		# 			wid.setFont(font)
		# 			self.change_txt(text)
		# 		else:
		# 			font = QtGui.QFont()
		# 			font.setStrikeOut(False)
		# 			font.setPointSize(14)
		# 			wid.setFont(font)
		# 			self.change_txt(text)




if __name__ == '__main__':

	MyApp().run()		