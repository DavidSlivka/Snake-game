import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

width = 600
height = 400

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_size = 10
snake_speed = 15
snake_list = []

font = pygame.font.SysFont("comicsans", 35)


def show_score(score):
    value = font.render(f"Your Score: {score}", True, BLACK)
    screen.blit(value, [0, 0])


def draw_snake(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, BLACK, [x[0], x[1], snake_size, snake_size])


def message(msg, color):
    msg = font.render(msg, True, color)
    screen.blit(msg, [width // 12, height // 2])


def main():
    run = True
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_size
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            run = False

        x1 += x1_change
        y1 += y1_change

        screen.fill(WHITE)
        pygame.draw.rect(screen, GREEN, [food_x, food_y, snake_size, snake_size])
        snake_h = [x1, y1]
        snake_list.append(snake_h)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_h:
                run = False

        draw_snake(snake_size, snake_list)
        show_score(snake_length - 1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    while not game_close:
        screen.fill(WHITE)
        message("You Lost! Press R to Play Again or Q to Quit", RED)
        show_score(snake_length - 1)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_close = True
                if event.key == pygame.K_r:
                    main()
    pygame.quit()
    quit()


if __name__ == '__main__':
    main()