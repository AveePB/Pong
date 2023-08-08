from pong.paddle import Paddle
from pong.ball import Ball

import pong.settings as sett

import pygame
pygame.init()

MAIN_SURF = pygame.display.set_mode((sett.WIDTH, sett.HEIGHT))
FONT = pygame.font.Font(sett.FONT_PATH, sett.FONT_SIZE)

pygame.display.set_caption(sett.TITLE)
pygame.display.set_icon(pygame.image.load(sett.ICON_PATH))

def update(left_paddle: Paddle, right_paddle: Paddle, ball: Ball) -> None:
    MAIN_SURF.fill(sett.BACKGROUND_COLOR)
    
    for curr_y in range(10, sett.HEIGHT, sett.HEIGHT//20):
        if (curr_y%2 == 1): continue
        curr_x = sett.WIDTH//2 - 5
        pygame.draw.rect(MAIN_SURF, sett.FOREGROUND_COLOR, (curr_x, curr_y, 10, sett.HEIGHT//20))
    
    left_score_surf = FONT.render(str(left_paddle.score), False, sett.FOREGROUND_COLOR)
    left_score_rect = left_score_surf.get_rect(center=(sett.WIDTH//4, sett.HEIGHT//5))
    MAIN_SURF.blit(left_score_surf, left_score_rect)

    right_score_surf = FONT.render(str(right_paddle.score), False, sett.FOREGROUND_COLOR)
    right_score_rect = right_score_surf.get_rect(center=(sett.WIDTH-sett.WIDTH//4, sett.HEIGHT//5))
    MAIN_SURF.blit(right_score_surf, right_score_rect)
    
    left_paddle.draw(MAIN_SURF)
    right_paddle.draw(MAIN_SURF)

    ball.draw(MAIN_SURF)

    if ((left_paddle.score == sett.MAX_SCORE) or (right_paddle.score == sett.MAX_SCORE)):
        game_over_surf = FONT.render("GAME OVER", False, sett.FOREGROUND_COLOR)
        game_over_rect = game_over_surf.get_rect(center=(sett.WIDTH//2, sett.HEIGHT//2))
        MAIN_SURF.blit(game_over_surf, game_over_rect)
    
    pygame.display.update()


def handlePaddleMovement(keys: pygame.key.ScancodeWrapper, left_paddle: Paddle, right_paddle: Paddle) -> None:
    if (keys[pygame.K_w]): left_paddle.move()
    if (keys[pygame.K_s]): left_paddle.move(False)

    if (keys[pygame.K_UP]): right_paddle.move()
    if (keys[pygame.K_DOWN]): right_paddle.move(False)


def main() -> None:
    clock = pygame.time.Clock()
    paddle_starting_y = sett.HEIGHT//2 - sett.PADDLE_HEIGHT//2

    left_paddle = Paddle(10, paddle_starting_y)
    right_paddle = Paddle(sett.WIDTH-10-sett.PADDLE_WIDTH, paddle_starting_y)

    ball = Ball(sett.WIDTH//2, sett.HEIGHT//2)

    is_running = True
    while (is_running):
        clock.tick(sett.MAX_FRAMERATE)
        update(left_paddle, right_paddle, ball)
        
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                is_running = False
                break

        if ((left_paddle.score == sett.MAX_SCORE) or 
            (right_paddle.score == sett.MAX_SCORE)):
            continue
        
        keys = pygame.key.get_pressed()
        handlePaddleMovement(keys, left_paddle, right_paddle)

        ball.move(left_paddle, right_paddle)
    pygame.quit()

if (__name__ == '__main__'):
    main()
