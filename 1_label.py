from kivy.app import App
from kivy.uix.button import Label

class SomeClassApp(App):

	def build(self):
		return Label()

c1 = SomeClassApp()
c1.run()