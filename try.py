#This is the main page of the Game
#To start playing the game we have to run this page
#importing module 
import pygame
#importing the files for the 
import p1name
import p2name
pygame.init()
#color
black=(0,0,0)
white=(255,255,255)
purple=(102,0,102)
green=(0,200,0)
blue=(0,0,255)
red=(255,0,0)
yellow=(255,255,0)
#coordinates
x,y=660,400
#game window
gamewin=pygame.display.set_mode((x,y))
pygame.display.set_caption('Tic Tac Toe')
clock=pygame.time.Clock()
crashed=False
#Game loop
while not crashed:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            crashed=True
    gamewin.fill(yellow)
    #printing welcome message
    font=pygame.font.Font('BRUSHSCI.ttf',60)
    text=font.render('WELCOME',True,purple)
    surf=text.get_rect()
    surf.center=(x//2,y//3)
    gamewin.blit(text,surf)
    "#--------------------------------------------------------------#"
    #Single player Button
    b1font=pygame.font.Font('BRUSHSCI.ttf',30)
    b1text=b1font.render('Single Player',True,black,green)
    b1surf=b1text.get_rect()
    b1surf.center=(200,270)
    gamewin.blit(b1text,b1surf)
    "#--------------------------------------------------------------#"
    #Multiplayer Button
    b2font=pygame.font.Font('BRUSHSCI.ttf',30)
    b2text=b2font.render('Multi Player',True,black,green)
    b2surf=b2text.get_rect()
    b2surf.center=(450,270)
    gamewin.blit(b2text,b2surf)
    pygame.display.update()
    #Checking if any button is pressed
    "#------------------------------------------------------------------------------------#"
    if pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] in range(129,271) and pygame.mouse.get_pos()[1] in range(251,289):
        p1name.p1()
    if pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] in range(382,519) and pygame.mouse.get_pos()[1] in range(251,289):
        p2name.p2()
pygame.quit()
quit()
#Exit
