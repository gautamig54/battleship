import pygame,sys
pygame.init()
bg=pygame.image.load("download.jpeg")
screen=pygame.display.set_mode((900,550))
bg=pygame.transform.scale(bg,(30,30))
screen.blit(bg,(0,0))
clr1=(248,248,255)
clr2=(255,0,0)
while True:

    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
      
    pygame.draw.rect(screen,clr2,(50,120,30,30))

    pygame.display.flip()

    a=pygame.Rect(50,120,30,30)


    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if a.collidepoint(pos):
                screen.fill(clr2)
                pygame.draw.rect(screen,clr1,(0,120,30,30))
