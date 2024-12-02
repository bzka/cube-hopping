import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 800
HEIGHT = 600
PLAYER_SIZE = 50
PLAYER_SPEED = 5
JUMP_HEIGHT = 20
GRAVITY = 1

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define some colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the player
player = pygame.Rect(100, 100, PLAYER_SIZE, PLAYER_SIZE)
player_vy = 0
player_on_ground = False

# Set up the platforms
platforms = [
    pygame.Rect(0, HEIGHT - 50, WIDTH, 50),
    pygame.Rect(300, HEIGHT - 200, 200, 50),
    pygame.Rect(100, HEIGHT - 350, 200, 50),
    pygame.Rect(500, HEIGHT - 500, 200, 50)
]

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_on_ground:
                player_vy = -JUMP_HEIGHT
                player_on_ground = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player.x += PLAYER_SPEED

    player.y += player_vy
    player_vy += GRAVITY

    if player.y + player.height > HEIGHT:
        player.y = HEIGHT - player.height
        player_vy = 0
        player_on_ground = True

    # Check for collisions with platforms
    for platform in platforms:
        if player.colliderect(platform):
            if player_vy > 0:
                player.bottom = platform.top
                player_vy = 0
                player_on_ground = True
            elif player_vy < 0:
                player.top = platform.bottom
                player_vy = 0

    # Draw everything
    screen.fill(BLUE)
    pygame.draw.rect(screen, RED, player)
    for platform in platforms:
        pygame.draw.rect(screen, GREEN, platform)
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
