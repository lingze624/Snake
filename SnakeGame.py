import pygame
import sys
import random

# 初始化pygame
pygame.init()

# 设置屏幕大小
screen_width = 800
screen_height = 600
screen = None

# 设置游戏速度
clock = pygame.time.Clock()
speed = 4

# 定义蛇和食物的大小
block_size = 20

# 定义颜色
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 蛇的初始位置
snake_pos = [[100, 100], [80, 100], [60, 100]]

# 食物的初始位置
food_pos = [300, 300]

direction = 'right'

# 蛇的长度
snake_len = 3

# font = pygame.font.Font("Microsoft YaHei", 36)
font = pygame.font.SysFont("SimHei", 22)

def draw_snake(snake_pos):
    for pos in snake_pos:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], block_size, block_size))


def draw_food(food_pos):
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], block_size, block_size))


def move_snake(snake_pos, direction):
    x, y = snake_pos[0]
    if direction == 'right':
        x += block_size
    elif direction == 'left':
        x -= block_size
    elif direction == 'up':
        y -= block_size
    elif direction == 'down':
        y += block_size
    snake_pos.insert(0, [x, y])
    snake_pos.pop()


def check_collision(snake_pos, food_pos):
    if snake_pos[0] == food_pos:
        return True
    return False


def generate_food(snake_pos):
    while True:
        x = random.randrange(0, screen_width, block_size)
        y = random.randrange(0, screen_height, block_size)
        if [x, y] not in snake_pos:
            return [x, y]


def check_game_over(snake_pos):
    x, y = snake_pos[0]
    if x < 0 or x >= screen_width or y < 0 or y >= screen_height or snake_pos[0] in snake_pos[1:]:
        return True
    return False


def draw_length(snake_len):
    global speed
    text = font.render(f"当前长度: {snake_len}   按空格可暂停" , True, 'BLACK')
    screen.blit(text, (10, 10))
    if snake_len == 50:
        speed = 10
    if snake_len == 200:
        speed = 15
    if snake_len == 500:
        speed = 20


def start():
    paused = False
    global direction,snake_pos,food_pos,screen,snake_len
    screen = pygame.display.set_mode((screen_width, screen_height))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'down':
                    direction = 'up'
                elif event.key == pygame.K_DOWN and direction != 'up':
                    direction = 'down'
                elif event.key == pygame.K_LEFT and direction != 'right':
                    direction = 'left'
                elif event.key == pygame.K_RIGHT and direction != 'left':
                    direction = 'right'
                elif event.key == pygame.K_SPACE:
                    paused = not paused
        if paused:
            continue

        move_snake(snake_pos, direction)

        if check_collision(snake_pos, food_pos):
            food_pos = generate_food(snake_pos)
            snake_pos.append(snake_pos[-1])
            snake_len += 1

        if check_game_over(snake_pos):
            break

        screen.fill(WHITE)
        draw_snake(snake_pos)
        draw_food(food_pos)
        draw_length(snake_len)  # 添加这一行来显示当前长度
        pygame.display.flip()
        clock.tick(speed)


if __name__ == '__main__':
    start()