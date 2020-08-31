import time
import random
import pygame

pygame.init()

#Colors that can be used for this game.
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 102)

#Coding for the display.
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake game by Edureka. Modified by Sean Serra.')

clock = pygame.time.Clock()

snake_block = 20
snake_speed = 12

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("bahnschrift", 25)

game_over = False
game_close = False 


def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, blue) 
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 2.5, dis_height / 3])


def message2(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 3.4, dis_height / 2])


def game_loop():
    game_over = False
    game_close = False 


    x1 = dis_width/2
    y1 = dis_height/2
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    food_x_coord = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
    food_y_coord = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0

#This gives the user the option to exit or play again when the player loses.
    while not game_over:
       
        while game_close == True:
            dis.fill(white)
            message("GAME OVER!", red)
            message2("Press Q-Quit or P-Play Again", red)
            your_score(length_of_snake - 1)
            pygame.display.update()
            

            for event in pygame.event.get(): 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                
#The directional movement for the snake is coded here. You can use arrow keys or WASD to move the snake.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    x1_change = 0
                    y1_change = snake_block

#This if statement defines the limits of the x and y coordinates so that when the snake hits the wall the game ends.
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis, black, [food_x_coord, food_y_coord, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list) 
        your_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == food_x_coord and y1 == food_y_coord:
            food_x_coord = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
            food_y_coord = round(random.randrange(0, dis_height -snake_block) / 20.0) * 20.0
            length_of_snake += 1
        
        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
