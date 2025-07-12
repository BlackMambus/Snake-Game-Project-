import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
FPS = 10

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (213, 50, 80)
BLACK = (0, 0, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('🐍 Snake Game')

# Clock
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont("comicsansms", 35)

def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], BLOCK_SIZE, BLOCK_SIZE])

def message(msg, color):
    text = font.render(msg, True, color)
    screen.blit(text, [WIDTH / 6, HEIGHT / 3])

def game_loop():
    game_over = False
    game_close = False

    x = WIDTH // 2
    y = HEIGHT // 2
    dx = 0
    dy = 0

    snake = []
    length = 1

    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            message("Game Over! Press Q-Quit or C-Play Again", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -BLOCK_SIZE
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = BLOCK_SIZE
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -BLOCK_SIZE
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = BLOCK_SIZE
                    dx = 0

        x += dx
        y += dy

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        snake.append([x, y])
        if len(snake) > length:
            del snake[0]

        for segment in snake[:-1]:
            if segment == [x, y]:
                game_close = True

        draw_snake(snake)
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE



