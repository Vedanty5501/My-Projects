#Thi file takes player one name as input in GUI way

#main function to display single player name window
def p1():
    import pygame
    #importing file 
    import tic
    pygame.init()
    #colors
    black=(0,0,0)
    white=(255,255,255)
    purple=(102,0,102)
    green=(0,200,0)
    blue=(0,0,255)
    red=(255,0,0)
    yellow=(255,255,0)
    #coordinates
    x,y=660,400
    #creating window
    gamewin=pygame.display.set_mode((x,y))
    pygame.display.set_caption('Tic Tac Toe')
    clock=pygame.time.Clock()
    crashed=False
    inp_rect=pygame.Rect(390,100,200,50)
    p1name=''
    #game loop
    while not crashed:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                crashed=True
            if event.type==pygame.KEYDOWN:
                if event.key==8:
                    p1name=p1name[0:len(p1name)-1]
                elif event.key==13:
                    tic.single(p1name)
                else:
                    p1name=p1name+event.unicode
        gamewin.fill(yellow)
        # displaying text for player name input
        p1font=pygame.font.Font('BRUSHSCI.ttf',30)
        p1text=p1font.render("Enter the name of player one ",True,black,)
        gamewin.blit(p1text,(100,100))
        "#----------------------------------------------#"
        pygame.draw.rect(gamewin,(black),inp_rect,2)
        '#----------------------------------#'
        #displaying the typed text on game window
        p1nm=p1font.render(p1name,True,blue)
        gamewin.blit(p1nm,(inp_rect.x+10,inp_rect.y))
        inp_rect.w=max(100,p1nm.get_width()+15)
        "#---------------------------------------------#"
        p1guid=p1font.render("Press Backspace key to clear andEnter key to play the game",True,black,)
        gamewin.blit(p1guid,(50,190))
        "#-----------------------------------------------------------#"
        #Exit button
        b1text=p1font.render('Exit',True,black,red)
        b1surf=b1text.get_rect()
        b1surf.center=(300,270)
        gamewin.blit(b1text,b1surf)
        #condition to check if button is clicked
        if pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] in range(277,322) and pygame.mouse.get_pos()[1] in range(251,289):
            break
        #updating game window
        pygame.display.update()
    pygame.quit()
#End
def abc():
    x=2
