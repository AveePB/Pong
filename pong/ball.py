from pong.paddle import Paddle
import pong.settings as sett

import random
import pygame

class Ball:
    color = sett.BALL_COLOR
    speed = sett.BALL_SPEED
    radius = sett.BALL_RADIUS

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.vx = 1
        self.vy = 0


    def draw(self, surf: pygame.Surface) -> None:
        pygame.draw.circle(surf, self.color, (self.x, self.y), self.radius)


    def move(self, left_paddle: Paddle, right_paddle: Paddle) -> None:
        #ball moves
        self.x += (self.vx * self.speed)
        self.y += (self.vy * self.speed)

        #left paddle collision
        if ((left_paddle.x < self.x and self.x < left_paddle.x + left_paddle.width) and
            (left_paddle.y < self.y and self.y < left_paddle.y + left_paddle.height)):
            self.vx = abs(self.vx)
            self.vy = ((self.y - left_paddle.y) / left_paddle.height) * random.choice([-1, 1])
        
        #right paddle collision
        if ((right_paddle.x < self.x and self.x < right_paddle.x + right_paddle.width) and 
            (right_paddle.y < self.y and self.y < right_paddle.y + right_paddle.height)):
            self.vx = abs(self.vx)*-1
            self.vy = ((self.y - right_paddle.y) / right_paddle.height) * random.choice([-1, 1])
        
        #wall collisions
        if (self.y > sett.HEIGHT): self.vy = abs(self.vy) * -1
        if (self.y < 0): self.vy = abs(self.vy)

        #left paddle scores
        if (self.x > sett.WIDTH): 
            left_paddle.resetPosition()
            right_paddle.resetPosition()
            
            left_paddle.score += 1
            self.x = sett.WIDTH//2
            self.y = sett.HEIGHT//2

            self.vx = 1
            self.vy = 0

        #right paddle scores
        if (self.x < 0):
            left_paddle.resetPosition()
            right_paddle.resetPosition()

            right_paddle.score += 1
            self.x = sett.WIDTH//2
            self.y = sett.HEIGHT//2

            self.vx = -1
            self.vy = 0
        
        #vector normalization 
        if (self.vx < -1): self.vx = -1
        if (self.vx > 1): self.vx = 1
        
        if (self.vy < -1): self.vy = -1 
        if (self.vy > 1): self.vy = 1