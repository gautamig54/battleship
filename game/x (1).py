def display_invalid():
	root = tk.Tk()
	root.withdraw()
	tkMessageBox.showinfo("Message", "Sorry, Invalid block")	

import pygame,sys
from checks import *
from ships import *
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)
pygame.init()
screen = pygame.display.set_mode((1300,700))
pygame.display.set_caption("Battleship")
clock = pygame.time.Clock()

pygame.draw.rect(screen,white,(0,0,650,700))
pygame.draw.rect(screen,black,(650,0,650,700))


rect1= []
rectplayer1 = []
rectplayer2 = []
rect = [rectplayer1,rectplayer2]
count = 0
count1 = 3
ctr = 0
flag = 0
flag1 = 0
flag2 = 0
flag3 = 0
flag4 = 0
ctr = 0
check = 0

for i in range(10):
	for j in range(10):
		pygame.draw.rect(screen,black,((j+2)*50,(i+2)*50,50,50),2)	
for i in range(14,24):
	for j in range(10):
		pygame.draw.rect(screen,white,((i)*50,(j+2)*50,50,50),2)
myfont = pygame.font.SysFont("monospace",30)
text1 = myfont.render("Player 1",1, black)
text2 = myfont.render("Player 2",1, white)
screen.blit(text1, (250,50))
screen.blit(text2, (900,50))
pygame.display.update()

#Input Loop - start

while True and ctr<2:
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		print (event)

		if ctr == 0 and flag == 0:
			pygame.draw.circle(screen, black, (230,60),10)
			pygame.display.update()
		if ctr == 1 and flag == 0:
			pygame.draw.circle(screen, white, (870,60),10)
			pygame.display.update()

		if flag ==  0:
			flag = 1
			import Tkinter as tk
			import tkMessageBox
			root = tk.Tk()
			root.withdraw()
			tkMessageBox.showinfo("Message", "Player " + str(ctr+1) + ", place your destroyer, 2 adjacent blocks")

		if count == 2 and flag == 1:
			count+=1
			flag = 2

		if flag == 1 and event.type == pygame.MOUSEBUTTONDOWN :
			flag2 = 0
			[x,y] = pygame.mouse.get_pos()
			x = (x/50)
			y = (y/50)
			if check_if_in_box(ctr,x,y) == 1:
				flag2 = 1
				display_invalid()
			if check_if_ship_present(ctr,x,y,rect,rect1) == 1:
				flag2 = 1  
				root = tk.Tk()
				root.withdraw()
				tkMessageBox.showinfo("Message", "Sorry, there already is a ship on this block")
			if count<2 and flag2 == 0:
				if count == 1:
					flag1 = 0
					if  check_if_valid(x,y,rect1):
						flag1 = 0
						check = check_orientation(rect1[0],[x,y])
					else:
						display_invalid()
						flag1 = 1
				if flag1 == 0 or count == 0:
					rect1.append([x,y])
 					pygame.draw.rect(screen,blue,(x*50,y*50,50,50))
					pygame.display.update()
					count += 1
					

		if count == 3 and flag == 2:
			rect[ctr].append(rect1)
			rect1 = []
			root = tk.Tk()
			root.withdraw()
			tkMessageBox.showinfo("Message", "Player " + str(ctr+1) + ", place your submarine, 3 adjacent blocks")
			count = 0
			flag = 3

		if count == 3 and flag == 3:
			count+=1
			flag = 4

		if event.type == pygame.MOUSEBUTTONDOWN and flag == 3:
			flag2 = 0
			[x,y] = pygame.mouse.get_pos()
			x = (x/50)
			y = (y/50)
			if check_if_in_box(ctr,x,y) == 1:
				flag2 = 1
				display_invalid()
			if check_if_ship_present(ctr,x,y,rect,rect1) == 1:
				flag2 = 1  
				root = tk.Tk()
				root.withdraw()
				tkMessageBox.showinfo("Message", "Sorry, there already is a ship on this block")
			if count<3 and flag2 == 0:
				if count == 1:
					flag1 = 0
					if  check_if_valid(x,y,rect1):
						flag1 = 0
						check = check_orientation(rect1[0],[x,y])
						print check
					else:
						display_invalid()
						flag1 = 1
				if count>1:
					print check
					if check == 0:
						print check_if_horizontal(x,y,rect1,count)
						if check_if_horizontal(x,y,rect1,count) == 1:
							flag1 = 0
						else:
							flag1 = 1 
							display_invalid()
					else:
						if check_if_vertical(x,y,rect1,count) == 1:
							flag1 = 0
						else:
							flag1 = 1
							display_invalid()
				if flag1 == 0 or count == 0:
					rect1.append([x,y])
 					pygame.draw.rect(screen,blue,(x*50,y*50,50,50))
					pygame.display.update()
					count += 1

		if count == 4 and flag == 4:
			rect[ctr].append(rect1)
			rect1 = []
			root = tk.Tk()
			root.withdraw()
			tkMessageBox.showinfo("Message", "Player " + str(ctr+1) + ", place your cruiser, 3 adjacent blocks")
			count = 0
			flag = 5

		if count == 3 and flag == 5:
			count+=1
			flag = 6

		if event.type == pygame.MOUSEBUTTONDOWN and flag == 5:
			flag2 = 0
			[x,y] = pygame.mouse.get_pos()
			x = (x/50)
			y = (y/50)
			if check_if_in_box(ctr,x,y) == 1:
				flag2 = 1
				display_invalid()
			if check_if_ship_present(ctr,x,y,rect,rect1) == 1:
				flag2 = 1  
				root = tk.Tk()
				root.withdraw()
				tkMessageBox.showinfo("Message", "Sorry, there already is a ship on this block")
			if count<3 and flag2 == 0:
				if count == 1:
					flag1 = 0
					if  check_if_valid(x,y,rect1):
						flag1 = 0
						check = check_orientation(rect1[0],[x,y])
						print check
					else:
						display_invalid()
						flag1 = 1
				if count>1:
					print check
					if check == 0:
						print check_if_horizontal(x,y,rect1,count)
						if check_if_horizontal(x,y,rect1,count) == 1:
							flag1 = 0
						else:
							flag1 = 1 
							display_invalid()
					else:
						if check_if_vertical(x,y,rect1,count) == 1:
							flag1 = 0
						else:
							flag1 = 1
							display_invalid()
				if flag1 == 0 or count == 0:
					rect1.append([x,y])
 					pygame.draw.rect(screen,blue,(x*50,y*50,50,50))
					pygame.display.update()
					count += 1

		if count == 4 and flag == 6:
			rect[ctr].append(rect1)
			rect1 = []
			root = tk.Tk()
			root.withdraw()
			tkMessageBox.showinfo("Message", "Player " + str(ctr+1) + ", place your battleship, 4 adjacent blocks")
			count = 0
			flag = 7

		if count == 4 and flag == 7:
			count+=1
			flag = 8

		if event.type == pygame.MOUSEBUTTONDOWN and flag == 7:
			flag2 = 0
			[x,y] = pygame.mouse.get_pos()
			x = (x/50)
			y = (y/50)
			if check_if_in_box(ctr,x,y) == 1:
				flag2 = 1
				display_invalid()
			if check_if_ship_present(ctr,x,y,rect,rect1) == 1:
				flag2 = 1  
				root = tk.Tk()
				root.withdraw()
				tkMessageBox.showinfo("Message", "Sorry, there already is a ship on this block")
			if count<4 and flag2 == 0:
				if count == 1:
					flag1 = 0
					if  check_if_valid(x,y,rect1):
						flag1 = 0
						check = check_orientation(rect1[0],[x,y])
						print check
					else:
						display_invalid()
						flag1 = 1
				if count>1:
					print check
					if check == 0:
						print check_if_horizontal(x,y,rect1,count)
						if check_if_horizontal(x,y,rect1,count) == 1:
							flag1 = 0
						else:
							flag1 = 1 
							display_invalid()
					else:
						if check_if_vertical(x,y,rect1,count) == 1:
							flag1 = 0
						else:
							flag1 = 1
							display_invalid()
				if flag1 == 0 or count == 0:
					rect1.append([x,y])
 					pygame.draw.rect(screen,blue,(x*50,y*50,50,50))
					pygame.display.update()
					count += 1

		if count == 5 and flag == 8:
			rect[ctr].append(rect1)
			rect1 = []
			root = tk.Tk()
			root.withdraw()
			tkMessageBox.showinfo("Message", "Player " + str(ctr+1) + ", place your carrier, 5 adjacent blocks")
			count = 0
			flag = 9

		if count == 5 and flag == 9:
			count+=1
			flag = 10

		if event.type == pygame.MOUSEBUTTONDOWN and flag == 9:
			flag2 = 0
			[x,y] = pygame.mouse.get_pos()
			x = (x/50)
			y = (y/50)
			if check_if_in_box(ctr,x,y) == 1:
				flag2 = 1
				display_invalid()
			if check_if_ship_present(ctr,x,y,rect,rect1) == 1:
				flag2 = 1  
				root = tk.Tk()
				root.withdraw()
				tkMessageBox.showinfo("Message", "Sorry, there already is a ship on this block")
			if count<5 and flag2 == 0:
				if count == 1:
					flag1 = 0
					if  check_if_valid(x,y,rect1):
						flag1 = 0
						check = check_orientation(rect1[0],[x,y])
						print check
					else:
						display_invalid()
						flag1 = 1
				if count>1:
					print check
					if check == 0:
						print check_if_horizontal(x,y,rect1,count)
						if check_if_horizontal(x,y,rect1,count) == 1:
							flag1 = 0
						else:
							flag1 = 1 
							display_invalid()
					else:
						if check_if_vertical(x,y,rect1,count) == 1:
							flag1 = 0
						else:
							flag1 = 1
							display_invalid()
				if flag1 == 0 or count == 0:
					rect1.append([x,y])
 					pygame.draw.rect(screen,blue,(x*50,y*50,50,50))
					pygame.display.update()
					count += 1
					
		if count == 6 and flag == 10:
			rect[ctr].append(rect1)
			rect1 = []
			count = 0
			flag = 0
			ctr += 1
			pygame.draw.rect(screen,white,(0,0,650,700))
			for i in range(10):
				for j in range(10):
					pygame.draw.rect(screen,black,((j+2)*50,(i+2)*50,50,50),2)
			screen.blit(text1, (250,50))
	pygame.display.update()

#Input Loop - end	
#Game Loop - start 

if ctr == 2:
	moves_of_p1 = []
	moves_of_p2 = []
	index1 = -1
	for i in range(5):
		rectplayer1[i] = map(lambda x : (x[0]+12,x[1]),rectplayer1[i])
	for i in range(5):
		rectplayer2[i] = map(lambda x : (x[0]-12,x[1]),rectplayer2[i])
	rect = [rectplayer1,rectplayer2]

	myfont = pygame.font.SysFont("monospace",30)
	text1 = myfont.render("Player 1",1, black)
	text2 = myfont.render("Player 2",1, white)
	text3 = myfont.render(" = Miss",1,black)
	text4 = myfont.render("Hit = ",1,white)
	ctr = 0
	pygame.draw.rect(screen,white,(0,0,650,700))
	pygame.draw.rect(screen,black,(650,0,650,700))
	for i in range(10):
		for j in range(10):
			pygame.draw.rect(screen,black,((j+2)*50,(i+2)*50,50,50),2)
	for i in range(14,24):
		for j in range(10):
			pygame.draw.rect(screen,white,((i)*50,(j+2)*50,50,50),2)
	screen.blit(text1, (250,50))
	screen.blit(text2, (900,50))
	screen.blit(text3, (505,50))
	screen.blit(text4, (680,50))
	pygame.draw.rect(screen,green,(450,40,50,50))
	pygame.draw.rect(screen,red,(800,40,50,50))
	pygame.display.update()
	while True and ctr<=2:
		flag2 = 0
		if flag == 0:
			flag = 1
			import random
			ctr = random.randrange(1,3) 
			root = tk.Tk()
			root.withdraw()
			tkMessageBox.showinfo("Message", "Player " + str(ctr) + " starts the attack!!")
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if ctr == 1:
				pygame.draw.circle(screen, black, (230,60),10)
				pygame.draw.circle(screen, black, (870,60),10)
			elif ctr == 2:
				pygame.draw.circle(screen, white, (870,60),10)
				pygame.draw.circle(screen, white, (230,60),10)
			pygame.display.update()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if ctr == 1:
					if check_if_in_box(ctr,x,y):
						flag2 = 1  
						display_invalid() 
					if check_if_attacked(ctr,x,y,moves_of_p1,moves_of_p2):
						flag2 = 1
						root = tk.Tk()
						root.withdraw()
						tkMessageBox.showinfo("Message", "This block has already been attacked")
					flag4 = 0
					[x,y] = pygame.mouse.get_pos()
					x = x/50
					y = y/50 
					if flag2 == 0:
						index1 = -1
						for i in rect[1]:
							index1 += 1
							index = -1
							for [xc,yc] in i:
								index += 1
								if x == xc and y == yc:
									flag4 = 1
									moves_of_p1.append([x,y])
									pygame.draw.rect(screen,red,(x*50,y*50,50,50))
									pygame.display.update()
									rect[1][index1].pop(index)
									rect[1][index1].append([0,0])
									break
							if flag4 == 1:
								break
						if flag4 == 1:
							if rect[1][index1][0][0] == 0 and rect[1][index1][0][1] == 0:
								root = tk.Tk()
								root.withdraw()
								tkMessageBox.showinfo("Message", "Congratulations, you have sunken the Player 2's " + check_ship(index1).name + " !!!")
							if check_if_win(rect,ctr) == 1:
								ctr = 3
								root = tk.Tk()
								root.withdraw()
								tkMessageBox.showinfo("Message", "Player 1 wins!!!")
							ctr += 1
						if flag4 == 0 and flag2 == 0:
							moves_of_p1.append([x,y])
							pygame.draw.rect(screen, green, (x*50, y*50, 50, 50))
							pygame.display.update()
							ctr += 1

				elif ctr == 2:
					if check_if_in_box(ctr,x,y):
						flag2 = 1  
						display_invalid() 
					if check_if_attacked(ctr,x,y,moves_of_p1,moves_of_p2):
						flag2 = 1
						root = tk.Tk()
						root.withdraw()
						tkMessageBox.showinfo("Message", "This block has already been attacked")
					flag4 = 0
					[x,y] = pygame.mouse.get_pos()
					x = x/50
					y = y/50
					if flag2 == 0:
						index1 = -1
						for i in rect[0]:
							index1 += 1
							index = -1
							for [xc,yc] in i:
								index += 1
								if x == xc and y == yc:
									flag4 = 1
									moves_of_p2.append([x,y])
									pygame.draw.rect(screen,red,(x*50,y*50,50,50))
									pygame.display.update()
									rect[0][index1].pop(index)
									rect[0][index1].append([0,0])
									break
							if flag4 == 1:
								break
						if flag4 == 1:
							if rect[0][index1][0][0] == 0 and rect[0][index1][0][1] == 0:
								root = tk.Tk()
								root.withdraw()
								tkMessageBox.showinfo("Message", "Congratulations, you have sunken Player 1's " + check_ship(index1).name + " !!!")
							if check_if_win(rect,ctr):
								ctr = 4
								root = tk.Tk()
								root.withdraw()
								tkMessageBox.showinfo("Message", "Player 2 wins!!!")
							ctr-=1
						if flag4 == 0 and flag2 == 0:
							moves_of_p2.append([x,y])
							pygame.draw.rect(screen, green, (x*50, y*50, 50, 50))
							pygame.display.update()
							ctr -= 1
		if ctr>2:
			pygame.quit()
			sys.exit()

