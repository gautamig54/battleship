import pygame,sys
import random
import Tkinter
import tkMessageBox

top=Tkinter.Tk()

def Battleship():
    tkMessageBox.showinfo("start game","There are 5 ships hidden in the grid. length of ships are 2,3,3,4 and 5. Find out the ships in 50 moves \nclose the start game dialog box!!")
    
B1 = Tkinter.Button(top, text = "start game", command =Battleship )

B1.pack()


top.mainloop()

pygame.init()

screen=pygame.display.set_mode((600,550),0,32) #making the pygame window
clr1=(248,248,255)
clr2=(255,0,0)
clr3=(106,90,205)

clock=pygame.time.Clock() #to regulate time of the operations on the screen
FPS1=4
FPS2=0

img=pygame.image.load("image2.jpeg")
img1=pygame.image.load("missed.jpeg")
img2=pygame.image.load("image1.png")
myfont = pygame.font.SysFont("monospace", 30)
flag=0
l=[]
l1=[]
l3=[]
l2=[]

m=150
n=150
#making a list of the 100 blocks set on the screen initially
while(m<421):
    n=150
    while(n<421):
        l.append([m,n])
        n=n+30
    m=m+30


#selecting a block randomly from the list of 100 blocks initialised earlier
#selecting another valid block in sequence and within range to make a ship of 2 blocks
i=0
while i==0:
    l1.append(random.choice(l))
    x=l1[0][0]
    y=l1[0][1]

    if (y+30)<=420:
        if [x,y+30] not in l1 and [x,y+60] not in l1:
            l1.append([x,y+30])
            i=1
    elif (x+30)<=420:
        if [x+30,y] not in l1 and [x+60,y] not in l1:
            l1.append([x+30,y])
            i=1
    elif (x-30)>=150:
        if [x-30,y] not in l1 and [x-60,y] not in l1:
            l1.append([x-30,y])
            i=1
    
    elif (y-30)>=150:
        if [x,y-30] not in l1 and [x,y-60] not in l1:
            l1.append([x,y-30])
            i=1
    if i==0:
        l1.pop(0)

print l1

#selecting another block randomly from the list of 100 blocks initialised earlier except those already taken.
#selecting another 2 valid block in sequence and within range to make a ship of 3 blocks
i=0
while i==0:
    l1.append(random.choice(l))
    x=l1[2][0]
    y=l1[2][1]

    if (x+30)<=420 and (x+60)<=420:
        if [x+30,y] not in l1 and [x+60,y] not in l1 and [x+90,y] not in l1:
            l1.append([x+30,y])
            l1.append([x+60,y])
            i=1
    elif (x-30)>=150 and (x-60)>=150:
        if [x-30,y] not in l1 and [x-60,y] not in l1 and [x-90,y] not in l1:
            l1.append([x-30,y])
            l1.append([x-60,y])
            i=1
    elif (y+30)<=420 and (y+60)<=420:
        if [x,y+30] not in l1 and [x,y+60] not in l1 and [x,y+90] not in l1:
            l1.append([x,y+30])
            l1.append([x,y+60])
            i=1
    elif (y-30)>=150 and (y-60)>=150:
        if [x,y-30] not in l1 and [x,y-60] not in l1 and [x,y-90] not in l1:
            l1.append([x,y-30])
            l1.append([x,y-60])
            i=1
    if i==0:
        l1.pop(2)
    
print l1

#selecting another block randomly from the list of 100 blocks initialised earlier except those already taken.
#selecting another 2 valid block in sequence and within range to make a ship of 3 blocks

i=0
while i==0:
    l1.append(random.choice(l))
    x=l1[5][0]
    y=l1[5][1]

    if (y+30)<=420 and (y+60)<=420:
        if [x,y+30] not in l1 and [x,y+60] not in l1 and [x,y+90] not in l1:
            l1.append([x,y+30])
            l1.append([x,y+60])
            i=1
    elif (x+30)<=420 and (x+60)<=420:
        if [x+30,y] not in l1 and [x+60,y] not in l1 and [x+90,y] not in l1:
            l1.append([x+30,y])
            l1.append([x+60,y])
            i=1
    elif (x-30)>=150 and (x-60)>=150:
        if [x-30,y] not in l1 and [x-60,y] not in l1 and [x-90,y] not in l1:
            l1.append([x-30,y])
            l1.append([x-60,y])
            i=1
    
    elif (y-30)>=150 and (y-60)>=150:
        if [x,y-30] not in l1 and [x,y-60] not in l1 and [x,y-90] not in l1:
            l1.append([x,y-30])
            l1.append([x,y-60])
            i=1
    if i==0:
        l1.pop(5)

print l1

#selecting another block randomly from the list of 100 blocks initialised earlier except those already taken.
#selecting another 3 valid block in sequence and within range to make a ship of 4 blocks

i=0
while i==0:
    l1.append(random.choice(l))
    x=l1[8][0]
    y=l1[8][1]

    if (x+30)<=420 and (x+60)<=420 and (x+90)<=420:
        if [x+30,y] not in l1 and [x+60,y] not in l1 and [x+90,y] not in l1 and [x+120,y] not in l1:
            l1.append([x+30,y])
            l1.append([x+60,y])
            l1.append([x+90,y])
            i=1
    elif (x-30)>=150 and (x-60)>=150 and (x-90)>=150:
        if [x-30,y] not in l1 and [x-60,y] not in l1 and [x-90,y] not in l1 and [x-120,y] not in l1:
            l1.append([x-30,y])
            l1.append([x-60,y])
            l1.append([x-90,y])
            i=1
    elif (y+30)<=420 and (y+60)<=420 and (y+90)<=420:
        if [x,y+30] not in l1 and [x,y+60] not in l1 and [x,y+90] not in l1 and [x,y+120] not in l1:
            l1.append([x,y+30])
            l1.append([x,y+60])
            l1.append([x,y+90])
            i=1
    elif (y-30)>=150 and (y-60)>=150 and (y-90)>=150:
        if [x,y-30] not in l1 and [x,y-60] not in l1 and [x,y-90] not in l1 and [x,y-120] not in l1:
            l1.append([x,y-30])
            l1.append([x,y-60])
            l1.append([x,y-90])
            i=1
    if i==0:
        l1.pop(8)

print l1    

#selecting another block randomly from the list of 100 blocks initialised earlier except those already taken.
#selecting another 4 valid block in sequence and within range to make a ship of 5 blocks

i=0
while i==0:
    l1.append(random.choice(l))
    x=l1[12][0]
    y=l1[12][1]

    if (y+30)<=420 and (y+60)<=420 and (y+90)<=420 and (y+120)<=420:
        if [x,y+30] not in l1 and [x,y+60] not in l1 and [x,y+90] not in l1 and [x,y+120] not in l1 and [x,y+150] not in l1:
            l1.append([x,y+30])
            l1.append([x,y+60])
            l1.append([x,y+90])
            l1.append([x,y+120])
            i=1

    elif (x+30)<=420 and (x+60)<=420 and (x+90)<=420 and (x+120)<=420 :
        if [x+30,y] not in l1 and [x+60,y] not in l1 and [x+90,y] not in l1 and [x+120,y] not in l1 and [x+150,y] not in l1 :
            l1.append([x+30,y])
            l1.append([x+60,y])
            l1.append([x+90,y])
            l1.append([x+120,y])
            i=1
    elif (x-30)>=150 and (x-60)>=150 and (x-90)>=150 and (x-120)>=150 :
        if [x-30,y] not in l1 and [x-60,y] not in l1 and [x-90,y] not in l1 and [x-120,y] not in l1 and [x-150,y] not in l1:
            l1.append([x-30,y])
            l1.append([x-60,y])
            l1.append([x-90,y])
            l1.append([x-120,y])
            i=1
    elif (y-30)>=150 and (y-60)>=150 and (y-90)>=150 and (y-120)>=150:
        if [x,y-30] not in l1 and [x,y-60] not in l1 and [x,y-90] not in l1 and [x,y-120] not in l1 and [x,y-150] not in l1:
            l1.append([x,y-30])
            l1.append([x,y-60])
            l1.append([x,y-90])
            l1.append([x,y-120])
            i=1
    if i==0:
        l1.pop(12)
        
print l1

l4=[[l1[0],l1[1]],[l1[2],l1[3],l1[4]],[l1[5],l1[6],l1[7]],[l1[8],l1[9],l1[10],l1[11]],[l1[12],l1[13],l1[14],l1[15],l1[16]]]
print l4
h=50        
ships=5
c=True
flag=0
#loop to show the screen and play game until the game gets over 
while c and h>0:


    
    
    label = myfont.render("BATTLESHIP", 2,clr1) #printing battleship title on screen
    screen.blit(label, (220,40))
    pygame.display.update()

    label = myfont.render("HIT", 2,clr1) #showing the hit ship denotion on screen
    screen.blit(label, (70,95))
    pygame.display.update()

    label = myfont.render("MISSED", 2,clr1) #showing the missed ship deno
    screen.blit(label, (200,95))
    pygame.display.update()

    screen.blit(img2,(130,95))
    screen.blit(img1,(320,95))

    label = myfont.render("MOVES="+ str(h), 2,clr1) # shows the number of moves left out of 50 
    screen.blit(label, (375,95))
    pygame.display.update()

    if l4[0]==[] or l4[1]==[] or l4[2]==[] or l4[3]==[] or l4[4]==[]:
        ships=ships-1
        if l4[0]==[]:
            l4[0]=[1]
        if l4[1]==[]:
            l4[1]=[1]
        if l4[2]==[]:
            l4[2]=[1]
        if l4[3]==[]:
            l4[3]=[1]
        if l4[4]==[]:
            l4[4]=[1]

    label = myfont.render("SHIPS REMAINING="+str(ships),2,clr1) #shows the number of ships yet to blast 
    screen.blit(label,(155,480))
    pygame.display.update()

    clock.tick(FPS1)
    
    screen.fill((0,0,0))
           
    #setting the grid on screen
    for j in range(150,421,30):
        for k in range(150,421,30):
            screen.blit(img,(j,k))
    
                

            
    for j in l2:
        screen.blit(img2,(j[0]+2,j[1]+2))
    for j in l3:
        screen.blit(img1,(j[0]+2,j[1]+2))
        
    
    
    

    #action coressponding to the mouse click
    #selecting the block clicked on and storing it in a list
    #opening the blocks that have ship and that do not have ship with different denotions
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen,(0,0,0),(375,95,30,30))
            pygame.display.update()
            pos=pygame.mouse.get_pos()
            x=pos[0]
            y=pos[1]
            while x%30!=0:
                x=x-1
            while y%30!=0:
                y=y-1
            if (x>=150 and x<=420 and y>=150 and y<=420):
                if [x,y] in l1 :
                    screen.blit(img2,(x+4,y+4))
                    l1.remove([x,y])
                    l2.append([x,y])
                    for i in l4:
                        if [x,y] in i:
                            i.remove([x,y])
                    h=h-1
                elif [x,y] not in l1 and [x,y] not in l2 and [x,y] not in l3:
                    screen.blit(img1,(x+4,y+4))
                    l3.append([x,y])
                    h=h-1

        
        
        elif event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        if l1==[]:
            c=False
    



    pygame.display.flip()

root=Tkinter.Tk()

#displaying the result after the game
#if looser then the correct solution appeears and the screen closes after the game is over
if len(l1) is 0:

    
    while True:  
    
        label = myfont.render("BATTLESHIP", 2,clr1)
        screen.blit(label, (220,40))
        pygame.display.update()

        label = myfont.render("WINNER", 2,clr1)
        screen.blit(label, (250,80))
        pygame.display.update()

        
    
    


        if flag==0:
            for j in range(150,421,30):
                for k in range(150,421,30):
                    screen.blit(img,(j,k))
             
                
            flag=1

       
        for i in l2:
            screen.blit(img2,(i[0]+5,i[1]+5))
        for i in l:
            if i not in l2:
                screen.blit(img1,(i[0]+5,i[1]+5))

        
        
        clock.tick(FPS2)
        pygame.quit()
        sys.exit()
    


    
        pygame.display.flip()

else:
    
    
    while True: 
    
        label = myfont.render("BATTLESHIP", 2,clr1)
        screen.blit(label, (220,40))
        pygame.display.update()

        label = myfont.render("LOOSER", 2,clr1)
        screen.blit(label, (265,80))
        pygame.display.update()

        
    
    


        if flag==0:
            for j in range(150,421,30):
                for k in range(150,421,30):
                    screen.blit(img,(j,k))
             
                
            flag=1

        
        for i in l2:
            screen.blit(img2,(i[0]+5,i[1]+5))
        for i in l1:
            screen.blit(img2,(i[0]+5,i[1]+5))
        for i in l:
            if i not in l1 and i not in l2:
                screen.blit(img1,(i[0]+5,i[1]+5))

        
        clock.tick(FPS2)
        pygame.quit()
        sys.exit()
    
    


    
        pygame.display.flip()






