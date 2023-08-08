import pong.settings as sett
import pygame

class Paddle:
    color = sett.PADDLE_COLOR
    width = sett.PADDLE_WIDTH
    height = sett.PADDLE_HEIGHT
    speed = sett.PADDLE_SPEED
 
    def __init__(self, x: int, y: int) -> None:
        self.score = 0
        self.__init_x = x
        self.__init_y = y
        self.x = x
        self.y = y
    

    def draw(self, surf: pygame.Surface) -> None:
        pygame.draw.rect(surf, self.color, (self.x, self.y, self.width, self.height))


    def move(self, is_up: bool=True) -> None:
        if (is_up):
            self.y = max(self.y - self.speed, 0)
        else:
            self.y = min(self.y + self.speed, sett.HEIGHT - self.height)
    

    def resetPosition(self) -> None:
        self.x = self.__init_x
        self.y = self.__init_y