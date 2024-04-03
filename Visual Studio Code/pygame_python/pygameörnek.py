import pygame
import sys

# Pygame'i başlat
pygame.init()

# Ekran ayarları
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Basit 2D Oyun")

# Oyuncu ayarları
player_width, player_height = 50, 50
player_x, player_y = width // 2 - player_width // 2, height - 2 * player_height
player_speed = 5

# Düşman ayarları
enemy_width, enemy_height = 50, 50
enemy_x, enemy_y = width // 2 - enemy_width // 2, 50
enemy_speed = 3

# Renk tanımlamaları
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

clock = pygame.time.Clock()

# Oyun döngüsü
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Klavye kontrolleri
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_width:
        player_x += player_speed

    # Düşman hareketi
    enemy_y += enemy_speed
    if enemy_y > height:
        enemy_y = 0

    # Çarpışma kontrolü
    if (
            player_x < enemy_x + enemy_width
        and player_x + player_width > enemy_x
        and player_y < enemy_y + enemy_height
        and player_y + player_height > enemy_y
    ):
        print("Oyun Bitti!")
        pygame.quit()
        sys.exit()

    # Ekran temizleme
    screen.fill(white)

    # Oyuncu çizimi
    pygame.draw.rect(screen, blue, (player_x, player_y, player_width, player_height))

    # Düşman çizimi
    pygame.draw.rect(screen, red, (enemy_x, enemy_y, enemy_width, enemy_height))

    # Ekranı güncelleme
    pygame.display.update()

    # Oyun hızı
    clock.tick(60)

