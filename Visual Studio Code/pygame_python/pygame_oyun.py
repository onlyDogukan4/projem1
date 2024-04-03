import pygame
import sys
import random

pygame.init() 
width,height=800,800
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Dogukan")

clock=pygame.time.Clock()

font = pygame.font.Font(None, 36)

counter=100

#barrier oluşturucu
class Barrier:
    def __init__(self,x,y,widthx,widthy,speed=0):
        self.x = x
        self.y = y
        self.widthx=widthx
        self.widthy=widthy
        self.speed=speed
barrier1=Barrier(400,400,80,80)
barrier2=Barrier(200,200,60,60)
barrier3=Barrier(200,150,40,40,7)
barrier4=Barrier(100,0,40,40,9)

#oyuncu oluşturucu
class Player:
    def __init__(self,x,y,widthx,widthy):
        self.x = x
        self.y = y
        self.widthx=widthx
        self.widthy=widthy
player1=Player(200,400,50,50)

#yem
random_number = random.randint(1, 10)

def draw_rotated_fan(x, y, size, angle):
    rotated_fan = pygame.Surface(size, pygame.SRCALPHA)
    pygame.draw.rect(rotated_fan, (0, 255, 0), (0, 0, *size))
    rotated_fan = pygame.transform.rotate(rotated_fan, angle)
    rotated_rect=rotated_fan.get_rect(center=(x,y))
    screen.blit(rotated_fan,rotated_rect.topleft)


class Fan:
     def __init__(self,x,y,size,angle_speed):
        self.x=x
        self.y=y
        self.size=size
        self.angle_speed=angle_speed
        self.angle=0

fan1=Fan(200,400,(400,8),3)

def check_collision_barrier(player,barrier):
    return(
        player.x<barrier.x+barrier.widthx
        and barrier.x<player.x+player.widthx
        and player.y+player.widthy>barrier.y
        and barrier.y+barrier.widthy>player.y
    )    
def check_collision_fan(player,fan):
    return(
        player.x<fan.x+fan.size[0]
        and fan.x<player.x+player.widthx
        and player.y+player.widthy>fan.y
        and fan.y+fan.size[1]>player.y
    )    

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("blue")
    keys=pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        player1.x-=5
    if keys[pygame.K_RIGHT]:
        player1.x+=5
    if keys[pygame.K_UP]:
        player1.y-=5
    if keys[pygame.K_DOWN]:
        player1.y+=5

    #text ayarlamaları
    text1 = font.render(f"Yanlış yerdesin amk Luciferı !!! Kalan Canın:{counter}", True , (0, 0, 0))
    text2 = font.render(f"#Görev: Ölmeden 3 yem al", True , (0, 0, 0),(255,0,0))
    text3 = font.render(f"Kalan canın:{counter}", True , (0, 0, 0),(0,255,0))

    #pervane fonksiyonunu çağır
    fan1.angle+=fan1.angle_speed
    draw_rotated_fan(fan1.x,fan1.y,fan1.size,fan1.angle)
    if fan1.angle>=360:
        fan1.angle=0

    #karakter
    hero=pygame.draw.rect(screen,(255,0,0),(player1.x,player1.y,player1.widthx,player1.widthy))

    #bariyer döngüsü
    if barrier3.y>height:
         barrier3.y=0
    if barrier4.y>height:
         barrier4.y=0
    def infinity():
        if player1.x>width:
            player1.x=0
        if player1.x<0:
            player1.x=width
        if player1.y<0:
            player1.y=height
        if player1.y>height:
            player1.y=0
    infinity()
    #engel
    barrier=pygame.draw.rect(screen,(0,255,0),(barrier1.x,barrier1.y,barrier1.widthx,barrier1.widthy))
    barrier=pygame.draw.rect(screen,(0,255,0),(barrier2.x,barrier2.y,barrier2.widthx,barrier2.widthy))
    barrier=pygame.draw.rect(screen,(0,255,0),(barrier3.x,barrier3.y,barrier3.widthx,barrier3.widthy))
    barrier=pygame.draw.rect(screen,(0,255,0),(barrier4.x,barrier4.y,barrier4.widthx,barrier4.widthy))
    
    #hareketli engel
    barrier3.y+=barrier3.speed
    barrier4.y+=barrier4.speed


    #çarpışmaması gerekenler
    if (
        check_collision_barrier(player1,barrier1) or
        check_collision_barrier(player1,barrier2) or
        check_collision_barrier(player1,barrier3) 
        ):
        counter-=1
    if check_collision_fan(player1,fan1):
        counter-=1


    screen.blit(text2,(220,0))
    screen.blit(text3,(0,0))



    if counter==0:
         pygame.quit()
         sys.exit()


    pygame.display.flip()
    clock.tick(60)