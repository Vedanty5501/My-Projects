#This file takes player one name and player two name as input in GUI way

#main function for inputting name for multiplayer game
def p2():
    import pygame
    #importing multiplayer game file
    import Tictoemanual
    pygame.init()
    #defining colors
    black=(0,0,0)
    white=(255,255,255)
    purple=(102,0,102)
    green=(0,200,0)
    blue=(0,0,255)
    red=(255,0,0)
    yellow=(255,255,0)
    #coordinates
    x,y=660,400
    #creating game window
    gamewin=pygame.display.set_mode((x,y))
    pygame.display.set_caption('Tic Tac Toe')
    clock=pygame.time.Clock()
    crashed=False
    inp_rect1=pygame.Rect(390,40,200,50)
    inp_rect2=pygame.Rect(390,100,200,50)
    p1name=""
    p2name=""
    inp=False
    #Game loop
    while not crashed:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                crashed=True
            if event.type==pygame.MOUSEBUTTONDOWN:
                if inp_rect1.collidepoint(event.pos):
                    inp=True
                elif inp_rect2.collidepoint(event.pos):
                    inp='a'
            if event.type==pygame.KEYDOWN:
                if inp==True:
                    if event.key==8:
                        p1name=p1name[0:len(p1name)-1]
                    else:
                        p1name=p1name+event.unicode
                if inp=='a':
                    if event.key==8:
                        p2name=p2name[:-1]
                    else:
                        p2name=p2name+event.unicode
        gamewin.fill(yellow)
        #Displaying text for player 1 name
        "#----------------------------------------------------------------------------------------------------------------#"
        pfont=pygame.font.Font('BRUSHSCI.ttf',30)
        "#----------------------------------------------------------------------------------------------#"
        p1text=pfont.render("Enter the name of player one ",True,black,)
        gamewin.blit(p1text,(100,40))
        "#----------------------------------------------#"
        pygame.draw.rect(gamewin,(black),inp_rect1,2)
        '#----------------------------------#'
        #Displaying the typed player 1 name
        p1nm=pfont.render(p1name,True,blue)
        gamewin.blit(p1nm,(inp_rect1.x+10,inp_rect1.y))
        inp_rect1.w=max(100,p1nm.get_width()+15)
        "#---------------------------------------------#"
        #Displaying text for player two name
        p2text=pfont.render("Enter the name of player two ",True,black,)
        gamewin.blit(p2text,(100,100))
        "#----------------------------------------------#"
        pygame.draw.rect(gamewin,(black),inp_rect2,2)
        '#----------------------------------#'
        #Displaying the typed player 2 name
        p2nm=pfont.render(p2name,True,blue)
        gamewin.blit(p2nm,(inp_rect2.x+10,inp_rect2.y))
        inp_rect2.w=max(100,p2nm.get_width()+15)
        "#---------------------------------------------#"
        pguid=pfont.render("Press Backspace key to clear ",True,black,)
        gamewin.blit(pguid,(50,190))
        "#-----------------------------------------------------------#"
        #Exit button
        b1text=pfont.render('Exit',True,black,red)
        b1surf=b1text.get_rect()
        b1surf.center=(200,270)
        gamewin.blit(b1text,b1surf)
        if pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] in range(178,222) and pygame.mouse.get_pos()[1] in range(251,289):
            break
        "#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#"
        #Play button
        b2text=pfont.render("Play",True,black,red)
        b2surf=b2text.get_rect()
        b2surf.center=(400,270)
        gamewin.blit(b2text,b2surf)
        if pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] in range(375,424) and pygame.mouse.get_pos()[1] in range(251,289):
            Tictoemanual.multi(p1name,p2name)
        #window update
        pygame.display.update()        
    pygame.quit()
#Exit
def acd():
    x=2
