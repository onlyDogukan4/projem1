import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dönen Şekil")

clock = pygame.time.Clock()

def draw_rotated_rect(center, size, angle):
    rect_surface = pygame.Surface(size, pygame.SRCALPHA)  # SRCALPHA, yüzeyin alfa kanalını korur
    pygame.draw.rect(rect_surface, (0, 0, 0), (0, 0, *size), 5)
    rotated_surface = pygame.transform.rotate(rect_surface, angle)
    rotated_rect = rotated_surface.get_rect(center=center)
    screen.blit(rotated_surface, rotated_rect.topleft)

rotation_angle = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 0,0))

    center = (width // 2, height // 2)
    rect_size = (200, 5)

    draw_rotated_rect(center, rect_size, rotation_angle)
    
    pygame.display.flip()
    clock.tick(60)

    rotation_angle += 2  # Her karede dönen açıyı artır

    if rotation_angle >= 360:
        rotation_angle = 0  # 360 derecenin üzerine çıkınca sıfırla
