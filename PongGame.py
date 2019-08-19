from kivy.app import App
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector


ball = ObjectProperty(None)

class PongBallWidget(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x,velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class Player1Widget(Widget):
    pass

class Player2Widget(Widget):
    pass


class PongGameWidget(Widget):
    def on_touch_down(self, touch):
        pass
        if touch.x < self.width/2:
            self.player1.center_y = touch.y
        if touch.x > self.width / 2:
            self.player2.center_y = touch.y

    def startgame(self):
        self.ball.velocity_x = 5
        self.ball.velocity_y = 2

    def update(self, delta_time):
        self.ball.move()
        #bounce off walls
        if(self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1
        if(self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1
        # bounce off player paddles
        if self.ball.collide_widget(self.player1) or self.ball.collide_widget(self.player2):
            self.ball.velocity_x *= -1
            # self.ball.velocity_y *= -1



class PongApp(App):
    def build(self):
        game = PongGameWidget()
        game.startgame()
        Clock.schedule_interval(game.update, 1.0/60.0)

        return game

if __name__ == "__main__":
    pong = PongApp()
    pong.run()


