#This file is for playing the game in multiplayer mode
def multi(p1name,p2name):
    #importing modules
    import pygame
    import time
    #importing file  for displaying scorecar after the game
    import score
    #colors
    black=(0,0,0)
    white=(255,255,255)
    purple=(102,0,102)
    green=(0,200,0)
    blue=(0,0,255)
    red=(255,0,0)
    yellow=(255,255,0)
    pygame.init()
    #function to check if a player has won a game or not
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
    #game window
    gamewin=pygame.display.set_mode((x,y))
    pygame.display.set_caption('Tic Tac Toe')
    clock=pygame.time.Clock()
    crashed=False
    #image to display the blocks for playing game
    img=pygame.image.load('Capture.PNG')
    bg_var=0
    i=0
    #list of options for marking O orX in the game
    lst=[1,2,3,4,5,6,7,8,9]
    bx_1,bx_2,bx_3,bx_4,bx_5,bx_6,bx_7,bx_8,bx_9=0,0,0,0,0,0,0,0,0
    p1lst,p2lst=[],[]
    #Game loop
    while not crashed:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                crashed=True
        if bg_var==0:
            #displaying  the blocks for game
            gamewin.fill(yellow)
            gamewin.blit(img,(600*0.25,400*0.25))
            bg_var=1
        else:
            #code to execute in case of Draw
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
            #Code to mark O in the Game window by player one
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
                    #checking if player one has won
                    w=winner(p1lst)
                    if w==1:
                            text=font.render(p1name+" has won the game....... Congratulations",True,blue)
                            textrec=text.get_rect()
                            textrec.center=(267,329)
                            gamewin.blit(text,textrec)
                            font=pygame.font.SysFont('Arial Rounded MT Bold',40)
                            txt="Right Click anywhere to scorecard"
                            text=font.render(txt,True,blue)
                            textrec=text.get_rect()
                            textrec.center=(267,368)
                            gamewin.blit(text,textrec)
                            i=3
                            #to go to the scorecard
                            score.scoreM(p1name,p2name,0)
            #To mark the X in the game by player two
            else:
                    if pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] in range(184,235) and pygame.mouse.get_pos()[1] in range(132,182) and bx_1==0:
                        font=pygame.font.SysFont('Arial Rounded MT Bold',30)
                        text1=font.render('X',True,red)
                        text1rec=text.get_rect()
                        text1rec.center=(215,160)
                        gamewin.blit(text1,text1rec)
                        bx_1=1
                        i=0
                        p2lst.append(1)
                        lst.remove(1)
                    elif pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] in range(241,299) and pygame.mouse.get_pos()[1] in range(132,182) and bx_2==0:
                        font=pygame.font.SysFont('Arial Rounded MT Bold',30)
                        text1=font.render('X',True,red)
                        text1rec=text.get_rect()
                        text1rec.center=(268,160)
                        gamewin.blit(text1,text1rec)
                        bx_2=1
                        i=0
                        p2lst.append(2)
                        lst.remove(2)
                    elif pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] in range(301,352) and pygame.mouse.get_pos()[1] in range(132,182) and bx_3==0:
                        font=pygame.font.SysFont('Arial Rounded MT Bold',30)
                        text1=font.render('X',True,red)
                        text1rec=text.get_rect()
                        text1rec.center=(328,160)
                        gamewin.blit(text1,text1rec)
                        bx_3=1
                        i=0
                        p2lst.append(3)
                        lst.remove(3)
                    elif pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] in range(184,235) and pygame.mouse.get_pos()[1] in range(187,248) and bx_4==0:
                        font=pygame.font.SysFont('Arial Rounded MT Bold',30)
                        text1=font.render('X',True,red)
                        text1rec=text.get_rect()
                        text1rec.center=(215,217)
                        gamewin.blit(text1,text1rec)
                        bx_4=1
                        i=0
                        p2lst.append(4)
                        lst.remove(4)
                    elif pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] in range(241,299) and pygame.mouse.get_pos()[1] in range(187,248) and bx_5==0:
                        font=pygame.font.SysFont('Arial Rounded MT Bold',30)
                        text1=font.render('X',True,red)
                        text1rec=text.get_rect()
                        text1rec.center=(268,217)
                        gamewin.blit(text1,text1rec)
                        bx_5=1
                        i=0
                        p2lst.append(5)
                        lst.remove(5)
                    elif pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] in range(301,352) and pygame.mouse.get_pos()[1] in range(187,248) and bx_6==0:
                        font=pygame.font.SysFont('Arial Rounded MT Bold',30)
                        text1=font.render('X',True,red)
                        text1rec=text.get_rect()
                        text1rec.center=(328,217)
                        gamewin.blit(text1,text1rec)
                        bx_6=1
                        i=0
                        p2lst.append(6)
                        lst.remove(6)
                    elif pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] in range(184,235) and pygame.mouse.get_pos()[1] in range(251,303) and bx_7==0:
                        font=pygame.font.SysFont('Arial Rounded MT Bold',30)
                        text1=font.render('X',True,red)
                        text1rec=text.get_rect()
                        text1rec.center=(215,280)
                        gamewin.blit(text1,text1rec)
                        bx_7=1
                        i=0
                        p2lst.append(7)
                        lst.remove(7)
                    elif pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] in range(241,299) and pygame.mouse.get_pos()[1] in range(251,303) and bx_8==0:
                        font=pygame.font.SysFont('Arial Rounded MT Bold',30)
                        text1=font.render('X',True,red)
                        text1rec=text.get_rect()
                        text1rec.center=(268,280)
                        gamewin.blit(text1,text1rec)
                        bx_8=1
                        i=0
                        p2lst.append(8)
                        lst.remove(8)
                    elif pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] in range(301,352) and pygame.mouse.get_pos()[1] in range(251,303) and bx_9==0:
                        font=pygame.font.SysFont('Arial Rounded MT Bold',30)
                        text1=font.render('X',True,red)
                        text1rec=text.get_rect()
                        text1rec.center=(328,280)
                        gamewin.blit(text1,text1rec)
                        bx_9=1
                        i=0
                        p2lst.append(9)
                        lst.remove(9)
                    #Checking if player two has won 
                    w=winner(p2lst)
                    if w==1:
                            text=font.render(p2name+" has won the game....... Congratulations",True,blue)
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
                            #to display scorecard
                            scor.scoreM(p1name,p2name,1)
        #updating game window
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
#Exit
def dfg():
    x=2














