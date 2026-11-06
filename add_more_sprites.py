import pygame
import random
import math

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision Game")

WHITE = (255, 255, 255)
BACKGROUND = f"bg.jpg"
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

score = 0

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for i in range(7):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

background = pygame.image.load('bg.jpg')
clock = pygame.time.Clock()
font = pygame.font.Font(None, 40)
collision_sound = pygame.mixer.Sound('enemy_sound.wav')
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()

    for enemy in enemies:
        if player.rect.colliderect(enemy.rect):
            score += 1
            collision_sound.play()
            all_sprites.remove(enemy)
            enemies.remove(enemy) 

    all_sprites.draw(screen)

    score_text = font.render(f"Score: {score}", True, RED)
    screen.blit(score_text, (10, 10))

    if score == 7:
        victory_message = font.render(f"You have won the game!", True, RED)
        screen.blit(victory_message, (50, 50))

    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()