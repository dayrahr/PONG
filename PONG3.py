# -*- coding: utf-8 -*-
"""
@author: Dayra
PONG clone, now with each player's score and a timer'
"""
import pygame,random,sys

#placing the ball at the center
def ball_center():
    
    global points_ti, ball_vel_x, ball_vel_y, time_now
    
    time_now=pygame.time.get_ticks()
    ball.center = (screen_W/2, screen_H/2)
    
    #show a timer
    if time_now - points_ti < 700:
        three=ffont.render("3",False,lightblue)
        screen.blit(three,(screen_W/2 - 10, screen_H/2 + 20))
    if 700 < time_now - points_ti < 1400:
        two=ffont.render("2",False,lightblue)
        screen.blit(two,(screen_W/2 - 10, screen_H/2 + 20))
    if 1400 < time_now - points_ti < 2100:
        one=ffont.render("1",False,lightblue)
        screen.blit(one,(screen_W/2 - 10, screen_H/2 + 20))
    
    if time_now - points_ti < 2100:
        #the ball stays at the center
        ball_vel_x=0
        ball_vel_y=0
    else: 
        #direction
        ball_vel_x = 8 * random.choice((-1,1))
        ball_vel_y = 8 * random.choice((-1,1))
        points_ti=None

#how the ball is going to move    
def ball_movement():
    
    global points_ti, ball_vel_x, ball_vel_y, P1_points, P2_points
    ball.x+=ball_vel_x
    ball.y+=ball_vel_y
    
    if ball.left <= 0:
        P1_points += 1
        points_ti=pygame.time.get_ticks()
        
    if ball.right >= screen_W:
        P2_points += 1
        points_ti=pygame.time.get_ticks()
        
    if ball.top <= 0 or ball.bottom >= screen_H:
        ball_vel_y *= -1
    
    if ball.colliderect(P1) or ball.colliderect(P2):
        ball_vel_x *= -1

#player one - you           
def P1_movement():
    
    P1.y += P1_vel
    if P1.top <= 0:
        P1.top=0
    if P1.bottom >= screen_H:
        P1.bottom=screen_H

#player two - the computer
def P2_movement():
    
    if P2.top < ball.y:
        P2.top += P2_vel
    if P2.bottom > ball.y:
        P2.bottom -= P2_vel 
        
    if P2.top <= 0:
        P2.top=0
    if P2.bottom >= screen_H:
        P2.bottom=screen_H

#initialize
pygame.init()
clock=pygame.time.Clock()

#screen
screen_W=1000
screen_H=700
screen=pygame.display.set_mode((screen_W, screen_H))
pygame.display.set_caption('My First Game: PONG clone')

#objects
ball=pygame.Rect(screen_W/2 - 15, screen_H/2 - 15, 30, 30)
P1=pygame.Rect(screen_W - 20, screen_H/2 - 60, 10, 120)
P2=pygame.Rect(10, screen_H/2 - 60, 10, 120)

#colors
black=(0,0,0)
purple=(129,34,141)
blue=(0,0,255)
white=(255,255,255)
pink=(255,105,180)
lightblue=(23,236,236)

#direction, speed and score
ball_vel_x = 8 * random.choice((-1,1))
ball_vel_y = 8 * random.choice((-1,1))
P1_vel=0
P2_vel=8
P1_points=0
P2_points=0

#font 
ffont=pygame.font.Font("freesansbold.ttf",40)

#timer
points_ti=None

while True:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                P1_vel += 8
            if event.key == pygame.K_UP:
                P1_vel -= 8
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                P1_vel -= 8
            if event.key == pygame.K_UP:
                P1_vel += 8
    
    ball_movement()
    P1_movement()
    P2_movement()
    
    #drawing
    screen.fill(black)
    pygame.draw.aaline(screen,white,(screen_W/2,0),(screen_W/2,screen_H))
    pygame.draw.rect(screen,purple,P1) 
    pygame.draw.rect(screen,blue,P2)  
    pygame.draw.ellipse(screen,pink,ball)     
    
    if points_ti:
        ball_center()
    
    #Text - score
    P1_text=ffont.render(f"{P1_points}",False,white)
    screen.blit(P1_text,(515,10))
    P2_text=ffont.render(f"{P2_points}",False,white)
    screen.blit(P2_text,(440,10))
   
    pygame.display.flip()
    clock.tick(60)