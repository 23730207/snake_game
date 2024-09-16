# ĐỒ ÁN CUỐI KHOÁ NHÓM 11
# NHÓM SS004.10.11


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
pygame.display.set_caption('Snake Game - SS004.10 - Team 11')

# Tốc độ khung hình
clock = pygame.time.Clock()
snake_speed = 15

# Kích thước của block (phần tử của con rắn)
snake_block = 10

# Định dạng font chữ
font_style = pygame.font.Font('fonts/Roboto-Black.ttf', 25)
score_font = pygame.font.Font('fonts/Roboto-Black.ttf', 30)

# Hiển thị điểm số
def your_score(score):
    value = score_font.render("Điểm: " + str(score), True, yellow)
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

    while not game_close:

        while game_over == True:
            dis.fill(blue)
            message("Bạn thua! Nhấn C chơi lại hoặc Q để thoát", red)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = False
                        game_close = True
                    if event.key == pygame.K_c:
                        gameLoop()

        # Kiểm tra di chuyển rắn 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
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
        
        # Kiểm tra va chạm với đường biên
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Kiểm tra va chạm với thân rắn
        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True

        # Cập nhật độ dài con rắn -> Vẽ rắn
        our_snake(snake_block, snake_list)
        # Cập nhật điểm của người chơi
        your_score(length_of_snake - 1)

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