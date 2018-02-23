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

screen=pygame.display.set_mode((600,550),0,32)
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)

img=pygame.image.load("image2.jpeg")
img1=pygame.image.load("missed.jpeg")
img2=pygame.image.load("image1.png")
myfont = pygame.font.SysFont("monospace", 30)
flag=0
l=[]
l1=[]
l3=[2,3,3,4,5]
l2=[]
m=150
n=150
while(m<421):
    n=150
    while(n<421):
        l.append([m,n])
        n=n+30
    m=m+30



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

h=1        
    
while True and h<=50:
    
    label = myfont.render("BATTLESHIP", 2,white)
    screen.blit(label, (220,40))
    pygame.display.update()


    if flag==0:
        for j in range(150,421,30):
            for k in range(150,421,30):
                pygame.draw.rect(screen,white,(j,k,30,30),2)`
                
        flag=1


    
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            x=pos[0]
            y=pos[1]
            while x%30!=0:
                x=x-1
            while y%30!=0:
                y=y-1
            if (x>=150 and x<=420 and y>=150 and y<=420):
                if [x,y] in l1 :
                    screen.draw.rect(screen,red,(x+2,y+2,30,30))
                    l1.remove([x,y])
                    l2.append([x,y])
                elif [x,y] not in l1 and [x,y] not in l2:
                    screen.draw.rect(screen,blue,(x+2,y+2,30,30))
        
            h=h+1

            
    
        elif event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    


    
    pygame.display.flip()

root=Tkinter.Tk()

if len(l1) is 0:
    
    root.withdraw()
    tkMessageBox.showinfo("results","WINNER!! you shot all the hidden ships! ")

else:
    root.withdraw()
    tkMessageBox.showinfo("results","looser!! you did not shot all the hidden ships! ")   

root.mainloop()

