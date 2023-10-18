import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Load the player image (replace 'character.png' with your image file)
player_image = pygame.image.load("D:/Codes/Python/dasar-pemrograman-python/proyek_pribadi/mini_projects/ai_generated/0.png")
player = player_image.get_rect()
player.center = (WIDTH // 2, HEIGHT // 2)

# Set up the clock
clock = pygame.time.Clock()

while True:
    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the player
    screen.blit(player_image, player)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5

    # Make sure the player stays on the screen
    if player.x < 0:
        player.x = 0
    if player.x > WIDTH - player.width:
        player.x = WIDTH - player.width
    if player.y < 0:
        player.y = 0
    if player.y > HEIGHT - player.height:
        player.y = HEIGHT - player.height

    # Update the display
    pygame.display.flip()

    # Cap the frame rate to 60 FPS
    clock.tick(60)
