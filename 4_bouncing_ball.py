from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from kivy.clock import Clock
import numpy as np

class BounceBallApp(App):
	def build(self):
		env = Environment()
		env.ball_init_velocity()
		Clock.schedule_interval(env.update, 1.0/60.0)
		return env



class Ball(Widget):
	
	velocity_x = NumericProperty(0)
	velocity_y = NumericProperty(0)
	velocity = ReferenceListProperty(velocity_x, velocity_y)

	def move(self):
		self.pos = Vector(*self.velocity) + self.pos 



class Paddle(Widget):
	velocity_y = NumericProperty(0)
	velocity_x = NumericProperty(0)
	velocity = ReferenceListProperty(velocity_x, velocity_y)

	def move(self):
		self.pos = Vector(*self.velocity) + self.pos



class Environment(Widget):
	ball = ObjectProperty(None)  #get the which is ball defined within <Environment> as an object
	paddle = ObjectProperty(None) 

	def ball_init_velocity(self, vel=(np.random.randint(1,4), np.random.randint(1,3))):
		self.ball.center = np.random.randint(0,20), np.random.randint(0,50)
		self.ball.velocity = vel

	def update(self, dt):
		self.ball.move()
		self.paddle.move()

		if(self.ball.y < 36) or (self.ball.y > (self.top-20)):
			self.ball.velocity_y *= -1

		if(self.ball.x < 5) or (self.ball.x > (self.width-20)):
			self.ball.velocity_x *= -1

		if(self.paddle.center_x > (self.width - 100)):
			self.paddle.center_x = self.width - 101


		if(self.paddle.center_x) < (105):
			self.paddle.center_x = 106

		if(self.ball.y < self.height / 2):
			paddle_distance = self.ball.x - self.paddle.center_x
			self.paddle.velocity_x = self.ball.velocity_x * 2


if __name__ == '__main__':
	BounceBallApp().run()