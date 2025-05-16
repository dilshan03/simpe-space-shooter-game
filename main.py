import pygame
import os
import random

pygame.init()

# Game Window Setup
WIDTH, HEIGHT = 600, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Load Assets
PLAYER_IMG = pygame.image.load(os.path.join("assets", "player.png"))
ENEMY_IMG = pygame.image.load(os.path.join("assets", "enemy.png"))
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background.png")), (WIDTH, HEIGHT))

# Draw Window
def draw_window(player, enemies, bullets, score):
    WIN.blit(BG, (0, 0))
    WIN.blit(PLAYER_IMG, (player.x, player.y))

    for bullet in bullets:
        pygame.draw.rect(WIN, (255, 0, 0), bullet)

    for enemy in enemies:
        WIN.blit(ENEMY_IMG, (enemy.x, enemy.y))

    font = pygame.font.SysFont("comicsans", 30)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    WIN.blit(score_text, (10, 10))

    pygame.display.update()

# Main Game Loop
def main():
    run = True
    clock = pygame.time.Clock()
    player = pygame.Rect(WIDTH // 2 - 25, HEIGHT - 100, 50, 50)
    bullets = []
    enemies = []
    bullet_speed = 7
    player_speed = 5
    enemy_timer = 0
    score = 0

    while run:
        clock.tick(60)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = pygame.Rect(player.x + player.width // 2 - 2, player.y, 4, 10)
                    bullets.append(bullet)

        # Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_speed > 0:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.x + player_speed + player.width < WIDTH:
            player.x += player_speed

        # Bullet Movement
        for bullet in bullets[:]:
            bullet.y -= bullet_speed
            if bullet.y < 0:
                bullets.remove(bullet)

        # Enemy Spawning
        enemy_timer += 1
        if enemy_timer >= 50:
            enemy_timer = 0
            enemy = pygame.Rect(random.randint(0, WIDTH - 50), -50, 50, 50)
            enemies.append(enemy)

        # Enemy Movement
        for enemy in enemies[:]:
            enemy.y += 3
            if enemy.y > HEIGHT:
                enemies.remove(enemy)

        # Collision Detection
        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if bullet.colliderect(enemy):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 1
                    break

        draw_window(player, enemies, bullets, score)

    pygame.quit()

if __name__ == "__main__":
    main()
