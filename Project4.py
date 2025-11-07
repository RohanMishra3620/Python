import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Object")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Player (basket)
player_width, player_height = 100, 20
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 10

# Falling object
object_width, object_height = 30, 30
object_x = random.randint(0, WIDTH - object_width)
object_y = 0
object_speed = 5

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Update falling object
    object_y += object_speed
    if object_y > HEIGHT:
        object_y = 0
        object_x = random.randint(0, WIDTH - object_width)

    # Check collision
    if (player_x < object_x + object_width and
        player_x + player_width > object_x and
        player_y < object_y + object_height and
        player_y + player_height > object_y):
        score += 1
        object_y = 0
        object_x = random.randint(0, WIDTH - object_width)

    # Draw player
    pygame.draw.rect(screen, BLACK, (player_x, player_y, player_width, player_height))

    # Draw falling object
    pygame.draw.rect(screen, RED, (object_x, object_y, object_width, object_height))

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()

pygame.quit()
sys.exit()
