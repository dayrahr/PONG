# -*- coding: utf-8 -*-
"""
First Game with pygame (Pong)
@author: Dayra
"""
import pygame,random,sys
pygame.init()
clock=pygame.time.Clock()

def ball_center():
    
    global ball_vel_x, ball_vel_y
    ball.center = (screen_W/2, screen_H/2)
    ball_vel_x *= random.choice((-1,1))
    ball_vel_y *= random.choice((-1,1))
    
def ball_movement():
    
    global ball_vel_x, ball_vel_y
    ball.x+=ball_vel_x
    ball.y+=ball_vel_y
    
    if ball.left <= 0 or ball.right >= screen_W:
        ball_center()
    if ball.top <= 0 or ball.bottom >= screen_H:
        ball_vel_y *= -1
    
    if ball.colliderect(P1) or ball.colliderect(P2):
        ball_vel_x *= -1
    
def P1_movement():
    
    P1.y += P1_vel
    if P1.top <= 0:
        P1.top=0
    if P1.bottom >= screen_H:
        P1.bottom=screen_H

def P2_movement():
    
    if P2.top < ball.y:
        P2.top += P2_vel
    if P2.bottom > ball.y:
        P2.bottom -= P2_vel 
        
    if P2.top <= 0:
        P2.top=0
    if P2.bottom >= screen_H:
        P2.bottom=screen_H

screen_W=1000
screen_H=700
screen=pygame.display.set_mode((screen_W, screen_H))
pygame.display.set_caption('My First Game')

ball=pygame.Rect(screen_W/2 - 15, screen_H/2 - 15, 30, 30)
P1=pygame.Rect(screen_W - 20, screen_H/2 - 60, 10, 120)
P2=pygame.Rect(10, screen_H/2 - 60, 10, 120)

background=(0,0,0)
red=(255,0,0)
blue=(0,0,255)
white=(255,255,255)

ball_vel_x = 8 * random.choice((-1,1))
ball_vel_y = 8 * random.choice((-1,1))
P1_vel=0
P2_vel=8

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
    
    screen.fill(background)
    pygame.draw.rect(screen,red,P1) 
    pygame.draw.rect(screen,blue,P2)  
    pygame.draw.ellipse(screen,white,ball)     
    pygame.draw.aaline(screen,white,(screen_W/2,0),(screen_W/2,screen_H))
    
    pygame.display.flip()
    clock.tick(60)
