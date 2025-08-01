import pygame
import sys
import random
import time
pygame.init()
display = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Haraval's game.")
Clock = pygame.time.Clock()
car1X = 600 // 2
car1Y = 600 // 2
car1SIZE = 55
car1SPEED = 10            
car1COLOR = (255, 255, 25)
Score1=0

car2X = 500 // 2
car2Y = 230 // 2
car2SIZE = 55
car2SPEED = 10             
car2COLOR =(0, 255, 255)
Score2=0

car3X = 400 // 2
car3Y = 599 // 2
car3SIZE = 55
car3SPEED = 10            
car3COLOR = (255, 255, 255)
Score3=0
boxX=(random.randint(0,600))
boxY=(random.randint(0,600))
boxWIDTH=50
boxHEIGHT=50
carWIDTH=55
carHEIGHT=55
StartTIME=time.time()
DURATION=60
FontSIZE=pygame.font.SysFont(None,45)
                                          
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car1X-=car1SPEED
    if keys[pygame.K_RIGHT]:
        car1X+=car1SPEED
    if keys[pygame.K_q]:
        car2X-=car2SPEED
    if keys[pygame.K_w]:
        car2X+=car2SPEED
    if keys[pygame.K_k]:
        car3X-=car3SPEED
    if keys[pygame.K_l]:
        car3X+=car3SPEED    

    if keys[pygame.K_UP]:
         car1Y-=car1SPEED
    if keys[pygame.K_DOWN]:
        car1Y+=car1SPEED
    if keys[pygame.K_u]:
        car2Y-=car2SPEED
    if keys[pygame.K_d]:
        car2Y+=car2SPEED
    if keys[pygame.K_g]:
        car3Y-=car3SPEED
    if keys[pygame.K_h]:
        car3Y+=car3SPEED    
    if car1X<boxX+boxWIDTH and car1X+carWIDTH>boxX and car1Y <boxY+boxHEIGHT and car1Y+carHEIGHT>boxY:
        Score1+=1
        boxX=random.randint(0,600- boxWIDTH)
        boxY=random.randint(0,600- boxHEIGHT)

    elif car2X<boxX+boxWIDTH and car2X+carWIDTH>boxX and car2Y <boxY+boxHEIGHT and car2Y+carHEIGHT>boxY:
        Score2+=1
        boxX=random.randint(0,600- boxWIDTH)
        boxY=random.randint(0,600- boxHEIGHT)
    elif car3X<boxX+boxWIDTH and car3X+carWIDTH>boxX and car3Y <boxY+boxHEIGHT and car3Y+carHEIGHT>boxY:
        Score3+=1
        boxX=random.randint(0,600- boxWIDTH)
        boxY=random.randint(0,600- boxHEIGHT)
    car1X=max(0,min(600-carWIDTH,car1X))
    car1Y=max(0,min(600-carWIDTH,car1Y))
    car2X=max(0,min(600-carWIDTH,car2X))
    car2Y=max(0,min(600-carWIDTH,car2Y))
    car3X=max(0,min(600-carWIDTH,car3X))
    car3Y=max(0,min(600-carWIDTH,car3Y))
    if time.time()-StartTIME>=DURATION:
     print(f'Car1 Score: {Score1} Car2 Score: {Score2} Car3 Score: {Score3}')
     Max=max(Score1,Score2,Score3)
     if Max==Score1:
      Winner="Car1"
     elif Max==Score2:
       Winner="Car2"
     else:
      Winner="Car3"
     print(f'Winner of the game is {Winner}')
     pygame.quit()
     sys.exit()
    display.fill((0,0,0))
    pygame.draw.rect(display,(255,0,0),(car1X,car1Y,carWIDTH,carHEIGHT))
    pygame.draw.rect(display,(0,255,0),(car2X,car2Y,carWIDTH,carHEIGHT))
    pygame.draw.rect(display,(0,0,255),(car3X,car3Y,carWIDTH,carHEIGHT))
    pygame.draw.rect(display,(255,255,0),(boxX,boxY,boxWIDTH,boxHEIGHT))
    Text=   FontSIZE.render(  f'Car1 Score: {Score1}\n Car2 Score: {Score2}\n Car3 Score: {Score3}',True,(255,255,255)) 
    display.blit(Text,(5,5))
    pygame.display.flip()
    Clock.tick(60)