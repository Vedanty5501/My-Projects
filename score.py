#This file displays the score of players playing the game after tupdating the last game played

#This function scoreS displayes the score for single player
def scoreS(p1name,w):
    #importing necessary module
    import pygame
    import pickle
    #this function is for reading the stored name of the players
    #this function only reads the stored data and does not perform any operations on it
    def pfile():
        #this part reads the file
        try:
            nfile=open('players.dat','rb')
            plst=pickle.load(nfile)
            nfile.close()
            return plst
        #if the file is not created it creates the file and then read it
        except:
            nfile=open('players.dat','wb')
            pickle.dump(["CPU"],nfile)
            nfile.close()
            x=pfile()
            return x

    #this function is for reading the stored score of the players
    #this function only reads the stored data and does not perform any operations on it            
    def sfile():
        #this part reads the file
        try:
            scfile=open('scores.dat','rb')
            slst=pickle.load(scfile)
            scfile.close()
            return slst
        #if the file is not created it creates the file and then read it
        except:
            scfile=open('scores.dat','wb')
            pickle.dump([[0]],scfile)
            scfile.close()
            x=sfile()
            return x
    plst=pfile()
    slst=sfile()
    #this part of the code update the scores of the player
    try:
        i=plst.index(p1name)
        if w==1:
            slst[i][0]=slst[i][0]+1
        else:
            slst[0][i]=slst[0][i]+1
            slst[i][2]=slst[i][3]+1
    except:
        plst.append(p1name)
        if w==1:
            slst.append([1,0,0])
            slst[0].append(0)
        else:
            slst[0].append(0)
            slst.append([0,0,1])
    #this part of code writes the updated data in the file
    nfile=open('players.dat','wb')
    pickle.dump(plst,nfile)
    nfile.close()
    sfile=open('scores.dat','wb')
    pickle.dump(slst,sfile)
    sfile.close()
    #Here 'i' is the index number of player in the list stored in binary file
    #Corresponding to this 'i' scores are also saved at the same index i.e 'i'
    i=plst.index(p1name)
    
    pygame.init()
    #Defining colours
    black=(0,0,0)
    white=(255,255,255)
    purple=(102,0,102)
    green=(0,200,0)
    blue=(0,0,255)
    red=(255,0,0)
    yellow=(255,255,0)
    #Coordinates
    x,y=660,400
    gamewin=pygame.display.set_mode((x,y))
    pygame.display.set_caption('Tic Tac Toe')
    clock=pygame.time.Clock()
    crashed=False
    #Game loop
    while not crashed:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                crashed=True
            if event.type==pygame.KEYDOWN:
                if event.key==27:
                    crashed=True
        gamewin.fill(yellow)
        pfont=pygame.font.Font('BRUSHSCI.ttf',30)
        #Displaying Scores
        "#--------------------------------------------------------------------------#"
        p1text=pfont.render("Number of matches won over CPU by "+p1name+" :-- ",True,black,)
        gamewin.blit(p1text,(40,50))
        txt=slst[i][0]
        p1text=pfont.render(str(txt),True,black,)
        gamewin.blit(p1text,(565,50))
        "#--------------------------------------------------------------------------#"
        p1text=pfont.render("Number of matches won over other player by "+p1name+" :-- ",True,black,)
        gamewin.blit(p1text,(40,90))
        txt=slst[i][1]
        p1text=pfont.render(str(txt),True,black,)
        gamewin.blit(p1text,(595,90))
        "#--------------------------------------------------------------------------#"
        p1text=pfont.render("Number of matches lost from CPU by "+p1name+" :-- ",True,black,)
        gamewin.blit(p1text,(40,130))
        txt=slst[0][i]
        p1text=pfont.render(str(txt),True,black,)
        gamewin.blit(p1text,(565,130))
        "#--------------------------------------------------------------------------#"
        p1text=pfont.render("Number of matches lost from other player by "+p1name+" :-- ",True,black,)
        gamewin.blit(p1text,(40,170))
        txt=slst[i][2]
        p1text=pfont.render(str(txt),True,black,)
        gamewin.blit(p1text,(595,170))
        "#--------------------------------------------------------------------------#"
        if w==1:
            pfont=pygame.font.Font('BRUSHSCI.ttf',50)
            p1text=pfont.render("Congratulations "+p1name+" for victory ",True,black,)
            gamewin.blit(p1text,(50,240))
        else:
            pfont=pygame.font.Font('BRUSHSCI.ttf',50)
            p1text=pfont.render("better luck next time ",True,black,)
            gamewin.blit(p1text,(50,240))
        "#--------------------------------------------------------------------------------------------------#"
        pfont=pygame.font.Font('BRUSHSCI.ttf',20)
        p1text=pfont.render("Press Esc key to exit ",True,black,)
        gamewin.blit(p1text,(50,300))
        pygame.display.update()
    pygame.quit()
#Exit


#This function scoreS displayes the score for single player
def scoreM(p1name,p2name,w):
    #importing necessary module
    import pygame
    import pickle
    #this function is for reading the stored name of the players
    #this function only reads the stored data and does not perform any operations on it
    def pfile():
        #this part reads the file
        try:
            nfile=open('players.dat','rb')
            plst=pickle.load(nfile)
            nfile.close()
            return plst
        #if the file is not created it creates the file and then read it
        except:
            nfile=open('players.dat','wb')
            pickle.dump(["CPU"],nfile)
            nfile.close()
            x=pfile()
            return x
            
    def sfile():
        try:
            scfile=open('scores.dat','rb')
            slst=pickle.load(scfile)
            scfile.close()
            return slst
        #if the file is not created it creates the file and then read it
        except:
            scfile=open('scores.dat','wb')
            pickle.dump([[0]],scfile)
            scfile.close()
            x=sfile()
            return x
    plst=pfile()
    slst=sfile()
    #this part of the code updates the scores of the both the players
    try:
        i=plst.index(p1name)
        try:
            j=plst.index(p2name)
            if w==0:
                slst[i][1]=slst[i][1]+1
                slst[j][2]=slst[j][2]+1
            else:
                slst[j][1]=slst[j][1]+1
                slst[i][2]=slst[i][2]+1
        except:
            plst.append(p2name)
            if w==0:
                slst[i][1]=slst[i][1]+1
                slst.append([0,0,1])
                slst[0].append(0)
            else:
                slst[0].append(0)
                slst.append([0,1,0])
                slst[i][2]=slst[i][2]+1
    except:
        plst.append(p1name)
        try:
            j=plst.index(p2name)
            if w==0:
                slst[0].append(0)
                slst.append([0,1,0])
                slst[j][2]=slst[j][2]+1
            else:
                slst[0].append(0)
                slst.append([0,0,1])
                slst[j][1]=slst[j][1]+1
        except:
            plst.append(p2name)
            if w==0:
                slst[0].append(0)
                slst[0].append(0)
                slst.append([0,1,0])
                slst.append([0,0,1])
            else:
                slst[0].append(0)
                slst[0].append(0)
                slst.append([0,0,1])
                slst.append([0,1,0])
    #this part of code writes the updated data in the file
    nfile=open('players.dat','wb')
    pickle.dump(plst,nfile)
    nfile.close()
    sfile=open('scores.dat','wb')
    pickle.dump(slst,sfile)
    sfile.close()
    
    #Here 'i' and 'j' are the index number of player in the list stored in binary file
    #Corresponding to this 'i' and 'j' , scores are also saved at the same index i.e 'i' and 'j'
    i=plst.index(p1name)
    j=plst.index(p2name)
    
    pygame.init()
    #defining colors
    black=(0,0,0)
    white=(255,255,255)
    purple=(102,0,102)
    green=(0,200,0)
    blue=(0,0,255)
    red=(255,0,0)
    yellow=(255,255,0)
    #defining coordinates
    x,y=660,500
    gamewin=pygame.display.set_mode((x,y))
    pygame.display.set_caption('Tic Tac Toe')
    clock=pygame.time.Clock()
    crashed=False
    #Game loop
    while not crashed:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                crashed=True
            if event.type==pygame.KEYDOWN:
                if event.key==27:
                    crashed=True
        gamewin.fill(yellow)
        #Displaying scores on game window
        pfont=pygame.font.Font('BRUSHSCI.ttf',30)
        "#--------------------------------------------------------------------------#"
        p1text=pfont.render("Number of matches won over CPU by "+p1name+" :-- ",True,black,)
        gamewin.blit(p1text,(40,25))
        txt=slst[i][0]
        p1text=pfont.render(str(txt),True,black,)
        gamewin.blit(p1text,(565,25))
        "#--------------------------------------------------------------------------#"
        p1text=pfont.render("Number of matches won over other player by "+p1name+" :-- ",True,black,)
        gamewin.blit(p1text,(40,65))
        txt=slst[i][1]
        p1text=pfont.render(str(txt),True,black,)
        gamewin.blit(p1text,(595,65))
        "#--------------------------------------------------------------------------#"
        p1text=pfont.render("Number of matches lost from CPU by "+p1name+" :-- ",True,black,)
        gamewin.blit(p1text,(40,105))
        txt=slst[0][i]
        p1text=pfont.render(str(txt),True,black,)
        gamewin.blit(p1text,(565,105))
        "#--------------------------------------------------------------------------#"
        p1text=pfont.render("Number of matches lost from other player by "+p1name+" :-- ",True,black,)
        gamewin.blit(p1text,(40,145))
        txt=slst[i][2]
        p1text=pfont.render(str(txt),True,black,)
        gamewin.blit(p1text,(595,145))
        "#--------------------------------------------------------------------------#"
        p1text=pfont.render("Number of matches won over CPU by "+p2name+" :-- ",True,black,)
        gamewin.blit(p1text,(40,185))
        txt=slst[j][0]
        p1text=pfont.render(str(txt),True,black,)
        gamewin.blit(p1text,(565,185))
        "#--------------------------------------------------------------------------#"
        p1text=pfont.render("Number of matches won over other player by "+p2name+" :-- ",True,black,)
        gamewin.blit(p1text,(40,225))
        txt=slst[j][1]
        p1text=pfont.render(str(txt),True,black,)
        gamewin.blit(p1text,(598,225))
        "#--------------------------------------------------------------------------#"
        p1text=pfont.render("Number of matches lost from CPU by "+p2name+" :-- ",True,black,)
        gamewin.blit(p1text,(40,265))
        txt=slst[0][j]
        p1text=pfont.render(str(txt),True,black,)
        gamewin.blit(p1text,(565,265))
        "#--------------------------------------------------------------------------#"
        p1text=pfont.render("Number of matches lost from other player by "+p2name+" :-- ",True,black,)
        gamewin.blit(p1text,(40,305))
        txt=slst[j][2]
        p1text=pfont.render(str(txt),True,black,)
        gamewin.blit(p1text,(598,305))
        "#--------------------------------------------------------------------------#"
        if w==0:
            pfont=pygame.font.Font('BRUSHSCI.ttf',50)
            p1text=pfont.render("Congratulations "+p1name+" for victory ",True,black,)
            gamewin.blit(p1text,(50,345))
        else:
            pfont=pygame.font.Font('BRUSHSCI.ttf',50)
            p1text=pfont.render("Congratulations "+p2name+" for victory ",True,black,)
            gamewin.blit(p1text,(50,345))
        "#---------------------------------------------------------------------------------------------------------------------------#"
        pfont=pygame.font.Font('BRUSHSCI.ttf',20)
        p1text=pfont.render("Press Esc key to exit ",True,black,)
        gamewin.blit(p1text,(50,400))
        pygame.display.update()
    pygame.quit()
#Exit

def abcd():
    x=2

