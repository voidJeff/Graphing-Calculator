from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset
import math

SCREEN_WIDTH = 1536
SCREEN_HEIGHT = 1024

class Axis(Sprite):
    
    xaxis = RectangleAsset(1500,1, thinline, black)
    yaxis = RectangleAsset(1,1050, thinline, black)
    
    def __init__(self, position):
        super().__init__(Axis.asset, position)

class Dot(Sprite):
    
    dot1 = RectangleAsset(2,2, thinline, red)
    dot2 = RectangleAsset(2,2, thinline, blue)

    def __init__(self, position):
        super().__init__(Dot.asset, position)
        self
    
    def Linear(self):
        self.y = k * self.x + b
        
    def step(self):
        self.Linear()
        Dot((self.x,self.y))
        self.x += 1

class Grapher(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        
        red = Color(0xff0000, 1.0)
        green = Color(0x00ff00, 1.0)
        blue = Color(0x0000ff, 1.0)
        black = Color(0x000000, 1.0)
        purple = Color(0xff00ff, 1.0)
        thinline = LineStyle(0, black)
        
        sprite1 = Sprite(xaxis, (0, 404))
        sprite2 = Sprite(yaxis, (718, 0))
        
    def step():
        for dot in self.getSpritesbyClass(Dot):
            dot.step()
            
myapp = Grapher(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
