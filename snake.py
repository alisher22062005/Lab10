import pygame
import time
import random
import psycopg2
import mysql.connector

snake_speed = 15

conn = psycopg2.connect(
    host="localhost",
    database="students_data",
    user="postgres",
    password="Alisher_18"
)
cur=conn.cursor()



name="hhbb" 
# Window size
window_x = 600
window_y = 600
 
# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
 
# Initialising pygame
pygame.init()
 
game_window = pygame.display.set_mode((window_x, window_y))
 
# FPS
fps = pygame.time.Clock()
 
# defining snake default position
snake_position = [100, 50]
 
# defining first 4 blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# fruit position
fruit_position = [50,50]
weight_of_food=random.randint(1,5)


#timer
timer_of_food=random.randint(20,100)
 
fruit_spawn = True
 
# setting default snake direction towards
direction = 'RIGHT'
change_to = direction
 
# initial score
score = 0
 
# displaying Score function
def show_score( color, font, size,score):
   
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
     
    # create the display surface object 
    score_surface = score_font.render('Score : ' + str(score), True, color)
     
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect(topright=(550,0))
     
    # displaying text
    game_window.blit(score_surface, score_rect)
 
# game over function
def game_over():
   
    # creating font object my_font
    my_font = pygame.font.SysFont('any_name', 50)
     
    # creating a text surface on which text 
    # will be drawn
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
     
    # create a rectangular object for the text 
    # surface object
    game_over_rect = game_over_surface.get_rect()
     
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
     
    game_window.fill(black)

    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    cur.execute("DROP TABLE students_data")
    a=1
    list_of_players=['alisher','ivan','kirill',"David","Batir"]
    index_players=0
    
    cur.execute("""CREATE TABLE students_data(
            name VARCHAR (255),
            score VARCHAR(255));""")
        

      
    for name in list_of_players:
        if list_of_players[index_players]==name:
             cur.execute("""INSERT INTO students_data(name,score) VALUES(%s,%s);""",((name,score)))
             conn.commit()
             continue
        cur.execute("""INSERT INTO students_data(name,score) VALUES(%s,%s);""",((name,'0'))) 
        conn.commit()
    

   
        
    
    time.sleep(2)
    

           
# Main Function
while True:
     
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
 
    #case when snake can't move in oposite directions
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
 
    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += weight_of_food
        fruit_spawn = False
        weight_of_food=random.randint(1,5)
    else:
        snake_body.pop()
         
    if  fruit_spawn==0:
        fruit_position[0] = random.randint(0,600/10-1)*10
        #print(fruit_position[0])
        fruit_position[1]=random.randint(0,600/10-1)*10
        #print(fruit_position[1])
         
    fruit_spawn = True
    game_window.fill(black)
     
    for pos in snake_body:
        pygame.draw.rect(game_window, green,[pos[0], pos[1], 10, 10],10)
                         
    pygame.draw.rect(game_window,white,[fruit_position[0],fruit_position[1],10,10],10)
    timer_of_food-=1
    if timer_of_food==0:
         pygame.draw.rect(game_window,black,[fruit_position[0],fruit_position[1],10,10],10)
         fruit_position[0] = random.randint(0,600/10-1)*10
         fruit_position[1] = random.randint(0,600/10-1)*10
         timer_of_food=random.randint(20,100)

 
    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
 
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
 
    # displaying score continuously
    show_score( white, 'any_name', 40,score)
 
    # Refresh game screen
    pygame.display.update()
 
    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)






