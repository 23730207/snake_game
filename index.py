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