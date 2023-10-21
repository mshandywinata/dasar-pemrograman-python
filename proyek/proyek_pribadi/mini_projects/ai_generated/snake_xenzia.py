import pygame
import time
import random

# Game variables
snake_speed = 15
window_x = 720
window_y = 480

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialize Pygame
pygame.init()
pygame.display.set_caption('Snake Xenzia')
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()

# Initialize snake position and fruit position
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True
direction = 'RIGHT'
change_to = direction

# Game loop
while True:
    # Game over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-20:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-20:
        game_over()

    # Fruit eaten condition
    if fruit_position == snake_position:
        score += 1
        fruit_spawn = False
    else:
        snake_body.pop()

    # Spawning fruit
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]
    fruit_spawn = True

    # Growing snake
    snake_body.insert(0, list(snake_position))

    # Game display
    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 20, 20))
    pygame.draw.rect(game_window, white,
                     pygame.Rect(fruit_position[0],
                                 fruit_position[1], 20, 20))

    # Game updates
    pygame.display.update()
    fps.tick(snake_speed)
