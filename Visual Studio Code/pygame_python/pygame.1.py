import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Text Example")

clock = pygame.time.Clock()

# Fontu tanımla
font = pygame.font.Font(None, 36)  # Varsayılan fontu kullan, boyutu 36

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))  # Ekranı temizle

    # Metni render et
    text = font.render("Hello, Pygame!", True , (0, 0, 0))  # Siyah renkte metin

    # Metni ekrana çiz
    screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))

    pygame.display.flip()
    clock.tick(60)
