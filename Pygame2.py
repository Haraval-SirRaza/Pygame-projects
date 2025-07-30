import pygame
import sys
import random

pygame.init()
display = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Haraval's game.")
Clock = pygame.time.Clock()

PlayerX = 600 // 2
PlayerY = 600 // 2
PlayerSIZE = 55
PlayerSPEED = 10
PlayerCOLOR = (255, 255, 255)
Score=0
FontSIZE=pygame.font.SysFont(None,45)
PointsRECT=pygame.Rect(300,300,90,90)
PlayerRECT=pygame.Rect(PlayerX,PlayerY,PlayerSIZE,PlayerSIZE)
InitialTIME=pygame.time.get_ticks()
BackgroundCOLOR=(123,123,9)

OBSTACLEcount=10
OBSTACLEsize=75
OBSTACLESlist=[]

for obstacles in range(1,10):
    obstaclesx=random.randint(0,600)
    obstaclesy=random.randint(0,600)
    OBSTACLESlist.append(pygame.Rect(obstaclesx,obstaclesy,OBSTACLEsize,OBSTACLEsize))
  
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        PlayerX -= PlayerSPEED
    if keys[pygame.K_RIGHT]:
        PlayerX += PlayerSPEED
    if keys[pygame.K_UP]:
        PlayerY -= PlayerSPEED
    if keys[pygame.K_DOWN]:
        PlayerY += PlayerSPEED
    if keys[pygame.K_SPACE]:
       BackgroundCOLOR=(random.randint(0,255),random.randint(0,255),random.randint(0,255)) 

    PlayerX = max(0, min(600 - PlayerSIZE, PlayerX))
    PlayerY = max(0, min(600 - PlayerSIZE, PlayerY))
    PlayerRECT=pygame.Rect(PlayerX,PlayerY,PlayerSIZE,PlayerSIZE)
    display.fill(BackgroundCOLOR)
    CurrentTIME= pygame.time.get_ticks()
    if CurrentTIME-InitialTIME>=10000:
       PointsRECT.x = random.randint(0,600)
       PointsRECT.y = random.randint(0,600)
       InitialTIME=CurrentTIME
    if PlayerRECT.colliderect(PointsRECT):
      Score+=1
      PointsRECT.x = random.randint(0,600)
      PointsRECT.y = random.randint(0,600)
    for colide in OBSTACLESlist:
        if PlayerRECT.colliderect(colide):
            print('Game over.')
            running=False
    pygame.draw.rect(display, (0, 0, 0),PointsRECT)
    pygame.draw.rect(display, PlayerCOLOR, PlayerRECT)
    for draw in OBSTACLESlist:
        pygame.draw.ellipse(display,(0,9,56),draw,width=0)
    Text=FontSIZE.render(f'Score:{Score}',True,(255,255,254))
    display.blit(Text,(5,5))
    pygame.display.flip()
    Clock.tick(60)
pygame.quit()
sys.exit()