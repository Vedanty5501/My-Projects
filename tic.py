#This file is to play the game in single player mode only
def single(p1name):
    #importing modules
    import pygame
    import time
    import random
    #importing file for next window of game
    import score
    pygame.init()
    #defining colors
    black=(0,0,0)
    white=(255,255,255)
    purple=(102,0,102)
    green=(0,200,0)
    blue=(0,0,255)
    red=(255,0,0)
    yellow=(255,255,0)
    #function to check for winner
    def winner(plst):
        if (1 in plst) and (4 in plst) and (7 in plst):
            return 1
        elif (2 in plst) and (5 in plst) and (8 in plst):
            return 1
        elif (3 in plst) and (6 in plst) and (9 in plst):
            return 1
        elif (1 in plst) and (2 in plst) and (3 in plst):
            return 1
        elif (4 in plst) and (5 in plst) and (6 in plst):
            return 1
        elif (7 in plst) and (8 in plst) and (9 in plst):
            return 1
        elif (1 in plst) and (5 in plst) and (9 in plst):
            return 1
        elif (3 in plst) and (5 in plst) and (7 in plst):
            return 1
        else:
            return 0
    red=(255,0,0)
    blue=(0,0,255)
    green=(0,255,0)
    white=(255,255,255)
    black=(0,0,0)
    #coordinates 
    x,y=600,400
    gamewin=pygame.display.set_mode((x,y))
    pygame.display.set_caption('Tic Tac Toe')
    clock=pygame.time.Clock()
    crashed=False
    #image to display blocks for playing game
    img=pygame.image.load('Capture.PNG')
    bg_var=0
    i=0
    #list for options where sign can be marked
    lst=[1,2,3,4,5,6,7,8,9]
    bx_1,bx_2,bx_3,bx_4,bx_5,bx_6,bx_7,bx_8,bx_9=0,0,0,0,0,0,0,0,0
    p1lst,p2lst=[],[]
    #Game loop
    while not crashed:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                crashed=True
        #displaying the image for blocks
        if bg_var==0:
            gamewin.fill(yellow)
            gamewin.blit(img,(600*0.25,400*0.25))
            bg_var=1
        #Code to execute in case match is draw
        else:
            if lst==[]:
                font=pygame.font.SysFont('Arial Rounded MT Bold',40)
                text=font.render("Game finished.......",True,blue)
                textrec=text.get_rect()
                textrec.center=(267,329)
                gamewin.blit(text,textrec)
                font=pygame.font.SysFont('Arial Rounded MT Bold',40)
                txt="Right Click anywhere to exit"
                text=font.render(txt,True,blue)
                textrec=text.get_rect()
                textrec.center=(267,368)
                gamewin.blit(text,textrec)
                if pygame.mouse.get_pressed()[2]==1:
                    crashed=True
                    continue
            if i==3:
                 if pygame.mouse.get_pressed()[2]==1:
                                    crashed=True
            #Code for marking O by player 1 in the game window
            if i==0:
                    if pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] in range(184,235) and pygame.mouse.get_pos()[1] in range(132,182) and bx_1==0:
                        font=pygame.font.SysFont('Arial Rounded MT Bold',30)
                        text=font.render('O',True,red)
                        textrec=text.get_rect()
                        textrec.center=(215,160)
                        gamewin.blit(text,textrec)
                        bx_1=1
                        i=1
                        p1lst.append(1)
                        lst.remove(1)
                    elif pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] in range(241,299) and pygame.mouse.get_pos()[1] in range(132,182) and bx_2==0:
                        font=pygame.font.SysFont('Arial Rounded MT Bold',30)
                        text=font.render('O',True,red)
                        textrec=text.get_rect()
                        textrec.center=(268,160)
                        gamewin.blit(text,textrec)
                        bx_2=1
                        i=1
                        p1lst.append(2)
                        lst.remove(2)
                    elif pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] in range(301,352) and pygame.mouse.get_pos()[1] in range(132,182) and bx_3==0:
                        font=pygame.font.SysFont('Arial Rounded MT Bold',30)
                        text=font.render('O',True,red)
                        textrec=text.get_rect()
                        textrec.center=(328,160)
                        gamewin.blit(text,textrec)
                        bx_3=1
                        i=1
                        p1lst.append(3)
                        lst.remove(3)
                    elif pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] in range(184,235) and pygame.mouse.get_pos()[1] in range(187,248) and bx_4==0:
                        font=pygame.font.SysFont('Arial Rounded MT Bold',30)
                        text=font.render('O',True,red)
                        textrec=text.get_rect()
                        textrec.center=(215,217)
                        gamewin.blit(text,textrec)
                        bx_4=1
                        i=1
                        p1lst.append(4)
                        lst.remove(4)
                    elif pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] in range(241,299) and pygame.mouse.get_pos()[1] in range(187,248) and bx_5==0:
                        font=pygame.font.SysFont('Arial Rounded MT Bold',30)
                        text=font.render('O',True,red)
                        textrec=text.get_rect()
                        textrec.center=(268,217)
                        gamewin.blit(text,textrec)
                        bx_5=1
                        i=1
                        p1lst.append(5)
                        lst.remove(5)
                    elif pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] in range(301,352) and pygame.mouse.get_pos()[1] in range(187,248) and bx_6==0:
                        font=pygame.font.SysFont('Arial Rounded MT Bold',30)
                        text=font.render('O',True,red)
                        textrec=text.get_rect()
                        textrec.center=(328,217)
                        gamewin.blit(text,textrec)
                        bx_6=1
                        i=1
                        p1lst.append(6)
                        lst.remove(6)
                    elif pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] in range(184,235) and pygame.mouse.get_pos()[1] in range(251,303) and bx_7==0:
                        font=pygame.font.SysFont('Arial Rounded MT Bold',30)
                        text=font.render('O',True,red)
                        textrec=text.get_rect()
                        textrec.center=(215,280)
                        gamewin.blit(text,textrec)
                        bx_7=1
                        i=1
                        p1lst.append(7)
                        lst.remove(7)
                    elif pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] in range(241,299) and pygame.mouse.get_pos()[1] in range(251,303) and bx_8==0:
                        font=pygame.font.SysFont('Arial Rounded MT Bold',30)
                        text=font.render('O',True,red)
                        textrec=text.get_rect()
                        textrec.center=(268,280)
                        gamewin.blit(text,textrec)
                        bx_8=1
                        i=1
                        p1lst.append(8)
                        lst.remove(8)
                    elif pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] in range(301,352) and pygame.mouse.get_pos()[1] in range(251,303) and bx_9==0:
                        font=pygame.font.SysFont('Arial Rounded MT Bold',30)
                        text=font.render('O',True,red)
                        textrec=text.get_rect()
                        textrec.center=(328,280)
                        gamewin.blit(text,textrec)
                        bx_9=1
                        i=1
                        p1lst.append(9)
                        lst.remove(9)
                    #Checking if player 1 has won or not
                    w=winner(p1lst)
                    if w==1:
                            text=font.render(p1name+" has won the game....... Congratulations",True,blue)
                            textrec=text.get_rect()
                            textrec.center=(267,329)
                            gamewin.blit(text,textrec)
                            font=pygame.font.SysFont('Arial Rounded MT Bold',40)
                            txt="Right Click anywhere to exit"
                            text=font.render(txt,True,blue)
                            textrec=text.get_rect()
                            textrec.center=(267,368)
                            gamewin.blit(text,textrec)
                            i=3
                            #if player 1 has one code for jumping to scorecard
                            score.scoreS(p1name,1)

            #Code for marking X in the Game
            #This is single player mode
            #so the X will be marked by Computer itself
            #For this random module is used
            if i==1:
                    cpu_ch=random.choice(lst)
                    if cpu_ch==1:
                        font=pygame.font.SysFont('Arial Rounded MT Bold',30)
                        text1=font.render('X',True,red)
                        text1rec=text.get_rect()
                        text1rec.center=(215,160)
                        gamewin.blit(text1,text1rec)
                        bx_1=1
                        i=0
                        p2lst.append(1)
                        lst.remove(1)
                    elif cpu_ch==2:
                        font=pygame.font.SysFont('Arial Rounded MT Bold',30)
                        text1=font.render('X',True,red)
                        text1rec=text.get_rect()
                        text1rec.center=(268,160)
                        gamewin.blit(text1,text1rec)
                        bx_2=1
                        i=0
                        p2lst.append(2)
                        lst.remove(2)
                    elif cpu_ch==3:
                        font=pygame.font.SysFont('Arial Rounded MT Bold',30)
                        text1=font.render('X',True,red)
                        text1rec=text.get_rect()
                        text1rec.center=(328,160)
                        gamewin.blit(text1,text1rec)
                        bx_3=1
                        i=0
                        p2lst.append(3)
                        lst.remove(3)
                    elif cpu_ch==4:
                        font=pygame.font.SysFont('Arial Rounded MT Bold',30)
                        text1=font.render('X',True,red)
                        text1rec=text.get_rect()
                        text1rec.center=(215,217)
                        gamewin.blit(text1,text1rec)
                        bx_4=1
                        i=0
                        p2lst.append(4)
                        lst.remove(4)
                    elif cpu_ch==5:
                        font=pygame.font.SysFont('Arial Rounded MT Bold',30)
                        text1=font.render('X',True,red)
                        text1rec=text.get_rect()
                        text1rec.center=(268,217)
                        gamewin.blit(text1,text1rec)
                        bx_5=1
                        i=0
                        p2lst.append(5)
                        lst.remove(5)
                    elif cpu_ch==6:
                        font=pygame.font.SysFont('Arial Rounded MT Bold',30)
                        text1=font.render('X',True,red)
                        text1rec=text.get_rect()
                        text1rec.center=(328,217)
                        gamewin.blit(text1,text1rec)
                        bx_6=1
                        i=0
                        p2lst.append(6)
                        lst.remove(6)
                    elif cpu_ch==7:
                        font=pygame.font.SysFont('Arial Rounded MT Bold',30)
                        text1=font.render('X',True,red)
                        text1rec=text.get_rect()
                        text1rec.center=(215,280)
                        gamewin.blit(text1,text1rec)
                        bx_7=1
                        i=0
                        p2lst.append(7)
                        lst.remove(7)
                    elif cpu_ch==8:
                        font=pygame.font.SysFont('Arial Rounded MT Bold',30)
                        text1=font.render('X',True,red)
                        text1rec=text.get_rect()
                        text1rec.center=(268,280)
                        gamewin.blit(text1,text1rec)
                        bx_8=1
                        i=0
                        p2lst.append(8)
                        lst.remove(8)
                    elif cpu_ch==9:
                        font=pygame.font.SysFont('Arial Rounded MT Bold',30)
                        text1=font.render('X',True,red)
                        text1rec=text.get_rect()
                        text1rec.center=(328,280)
                        gamewin.blit(text1,text1rec)
                        bx_9=1
                        i=0
                        p2lst.append(9)
                        lst.remove(9)
                    #Checking if Computer has won 
                    w=winner(p2lst)
                    if w==1:
                            text=font.render(p1name+" has loss the game....... ",True,blue)
                            textrec=text.get_rect()
                            textrec.center=(267,329)
                            gamewin.blit(text,textrec)
                            font=pygame.font.SysFont('Arial Rounded MT Bold',40)
                            txt="Right Click anywhere to exit"
                            text=font.render(txt,True,blue)
                            textrec=text.get_rect()
                            textrec.center=(267,368)
                            gamewin.blit(text,textrec)
                            i=3
                            #displaying scorecard
                            score.scoreS(p1name,0)
        #updating game window
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
#Exit
def sec():
    x=2














