import pygame
import time
import random

# Khởi tạo Pygame
pygame.init()

# Định nghĩa màu sắc
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Kích thước màn hình
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))

# Tên của cửa sổ game
pygame.display.set_caption('Snake Game')

# Tốc độ khung hình
clock = pygame.time.Clock()
snake_speed = 15

# Kích thước của block (phần tử của con rắn)
snake_block = 10

# Định dạng font chữ
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

# Hiển thị điểm số
def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    dis.blit(value, [0, 0])

# Vẽ rắn
def our_snake(snake_block, snake_list):
    # Code ở đây 
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# Thông báo game
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Play game
def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Random vị trí x,y của mồi
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:
 

        # Kiểm tra di chuyển rắn 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        pygame.display.update()

        # Săn mồi: Kiểm tra va chạm của đầu rắn với vị trí của mồi
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)
    pygame.quit()
    quit()

gameLoop()