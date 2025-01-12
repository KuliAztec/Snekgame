import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 600, 400

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Create the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Clock
clock = pygame.time.Clock()
snake_block = 10  # Size of each block
snake_speed = 15  # Speed of the snake

# Font styles
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# High score
high_score = 0

# Functions
def score_display(score):
    value = score_font.render("Score: " + str(score), True, yellow)
    screen.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, green, [block[0], block[1], snake_block, snake_block])

def message(msg, color, y_displace=0):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3 + y_displace])

# Main game loop
def gameLoop():
    global high_score
    game_over = False
    game_close = False

    # Starting position of the snake
    x1 = width / 2
    y1 = height / 2

    # Change in position
    x1_change = 0
    y1_change = 0

    # Snake body
    snake_list = []
    length_of_snake = 1

    # Food position
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    # Special food position and timer
    special_foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    special_foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
    special_food_timer = 0
    special_food_duration = 3  # seconds
    start_time = pygame.time.get_ticks()

    # Rock positions
    num_rocks = 32
    rocks = []
    for _ in range(num_rocks):
        rock_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        rock_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
        rocks.append([rock_x, rock_y])


    while not game_over:

        while game_close:
            screen.fill(blue)
            message("You lost! Press Q-Quit or C-Play Again", red)
            score_display(length_of_snake - 1)
            if length_of_snake - 1 > high_score:
                high_score = length_of_snake - 1
            message(f"High Score: {high_score}", yellow, 50)  # Adjusted position
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change != snake_block:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change != -snake_block:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change != snake_block:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change != -snake_block:
                    y1_change = snake_block
                    x1_change = 0

        # Wrap the snake position when it goes out of bounds
        if x1 >= width:
            x1 = 0
        elif x1 < 0:
            x1 = width - snake_block
        if y1 >= height:
            y1 = 0
        elif y1 < 0:
            y1 = height - snake_block

        x1 += x1_change
        y1 += y1_change
        screen.fill(black)

        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])

        # Draw special food if timer is active
        if special_food_timer <= 0:
            special_food_timer = 0  # Ensure no negative timer
        else:
            pygame.draw.rect(screen, yellow, [special_foodx, special_foody, snake_block, snake_block])


        # Draw rocks
        for rock in rocks:
            pygame.draw.rect(screen, white, [rock[0], rock[1], snake_block, snake_block])

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        # Check collision with rocks
        for rock in rocks:
            if abs(rock[0] - x1) < snake_block and abs(rock[1] - y1) < snake_block:
                game_close = True


        our_snake(snake_block, snake_list)
        score_display(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        if x1 == special_foodx and y1 == special_foody:
            score = int(special_food_duration - special_food_timer)
            length_of_snake += score ** 2
            special_food_timer = 0

        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
        if elapsed_time >= special_food_duration:
            special_food_timer = 0
            start_time = pygame.time.get_ticks()

        if special_food_timer <= 0:
            special_foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            special_foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            special_food_timer = special_food_duration

        snake_speed = 15 + (length_of_snake // 5)
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
gameLoop()
