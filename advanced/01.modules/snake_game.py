import pygame
import random

pygame.init()

dis_width = 500
dis_height = 500
dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption("Snake game -> chuss")

blue = (0,0,255)
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)


snake_size = 10
snake_speed = 15

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 15, italic=True)
score_font = pygame.font.SysFont("comicsansms",40)

def your_score(score):
    value = score_font.render("SCORE: " + str(score), True, red)
    dis.blit(value,[0,0])



def snake(snake_size,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,white,[x[0],x[1], snake_size, snake_size])


def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/12,dis_height/2])

def game_loop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0
    snake_list = []
    snake_length = 1

    foodx = round(random.randrange(0,dis_width - snake_size) / snake_size) * snake_size
    foody = round(random.randrange(0, dis_height - snake_size)/ snake_size) * snake_size

    while not game_over:
        while game_close == True:
            dis.fill(black)
            message("You LOST MAN! Press ESC-QUIT or SPACE-PLAY AGAIN", white)
            your_score(snake_length -1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y1_change = -snake_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_size
                    x1_change = 0
                elif event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
        if x1 >= dis_width or x1 < 0 or y1>= dis_height or y1<0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, blue, [foodx, foody, snake_size, snake_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        snake(snake_size,snake_list)
        your_score(snake_length -1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_size) / snake_size) * snake_size
            foody = round(random.randrange(0, dis_height - snake_size) / snake_size) * snake_size
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()

