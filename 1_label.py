from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class SomeClassApp(App):

	def build(self):
		return LoginScreen()

class LoginScreen(GridLayout):
	def __init__(self, **kwards):
		super(LoginScreen, self).__init__(**kwards)
		self.cols = 2
		self.add_widget(Label(text='User Name'))
		self.username = TextInput(multiline=False)
		self.add_widget(self.username)
		self.add_widget(Label(text='password'))
		self.password = TextInput(password=True, multiline=False)
		self.add_widget(self.password)

if __name__ == '__main__':
	SomeClassApp().run()