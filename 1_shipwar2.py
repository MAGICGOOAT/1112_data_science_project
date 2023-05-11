import pygame
import random
import tkinter as tk
# import tkinter_test as tt
import subprocess
import time

black = (0, 0, 0)
red = "#FF0000"
white = (255, 255, 255)
CUSTOMEVENT = pygame.USEREVENT + 1
pygame.init()

score = 0
font = pygame.font.SysFont("Arial", 30)

# 定義計分方法
def update_score(points):
    global score
    score += points


# 顯示得分
def show_score():
    score_surface = font.render(f"Score: {score}", True, (255, 255, 255))
    WINDOW.blit(score_surface, (10, 10))

# 設置遊戲視窗的大小
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 600

# 設置遊戲視窗
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("飛機大戰")

# 加入遊戲圖片
BACKGROUND_IMAGE = pygame.image.load("background.jpg").convert()
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (WINDOW_WIDTH, WINDOW_HEIGHT))
PLAYER_IMAGE = pygame.image.load("player.jpg").convert()
ENEMY_IMAGE = pygame.image.load("enemy.png").convert()

BULLET_IMAGE = pygame.image.load("bullet.png").convert_alpha()
BULLET_IMAGE = pygame.transform.scale(BULLET_IMAGE, (20, 20))

BULLET_IMAGE_G = pygame.image.load("bullet.png").convert_alpha()
BULLET_IMAGE_G = pygame.transform.scale(BULLET_IMAGE, (30, 30))

ENEMY_IMAGE = pygame.transform.scale(ENEMY_IMAGE, (40, 40))
PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE, (40, 40))



CLOCK = pygame.time.Clock()

# 定義遊戲元素
class Element:
    def __init__(self, image, x, y, speed):
        
        self.image = image
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def move(self):
        self.rect.y += self.speed
        
        # self.rect.x += self.speed

    def draw(self):
        WINDOW.blit(self.image, self.rect)

# 玩家
class Player(Element):
    def __init__(self, image, x, y, speed):
        super().__init__(image, x, y, speed)
        self.bullets = []

    def fire_1(self):
        bullet = Element(BULLET_IMAGE, self.rect.centerx, self.rect.y, -10)
        self.bullets.append(bullet)
        
    def fire_2(self):
        bullet = Element(BULLET_IMAGE, self.rect.centerx, self.rect.y, -20)
        self.bullets.append(bullet)
        
    def fire_3(self):        
        bullet = Element(BULLET_IMAGE_G, self.rect.centerx, self.rect.y, -20)
        self.bullets.append(bullet)

    

    def move_bullets(self):
        for bullet in self.bullets:
            bullet.move()
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

    def draw_bullets(self):
        for bullet in self.bullets:
            bullet.draw()

# 敵機
class Enemy(Element):
    def __init__(self, image, x, y, speed):
        super().__init__(image, x, y, speed)

    def reset(self):
        # 重置敵機位置和速度
        x = random.randint(0, WINDOW_WIDTH - self.rect.width)
        y = random.randint(-2 * self.rect.height, -self.rect.height)
        self.rect.x = x
        self.rect.y = y
        self.speed = random.randint(1, 4)

# 創建
player = Player(PLAYER_IMAGE, 200, 500, 0)
enemies = []
for i in range(10):
    x = random.randint(0, WINDOW_WIDTH - ENEMY_IMAGE.get_width())
    y = random.randint(-WINDOW_HEIGHT, -2*ENEMY_IMAGE.get_height())
    speed = random.randint(1, 4)
    enemy = Enemy(ENEMY_IMAGE, x, y, speed)
    enemies.append(enemy)
game_over = False

while True:
    # 事件
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                player.fire_1()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_2:
                player.fire_2()
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_3:
                pygame.time.set_timer(CUSTOMEVENT, 50, 3)
                            
        if event.type == CUSTOMEVENT:
            player.fire_3()

    # 生成敵機
    if not enemies:
        x = random.randint(0, WINDOW_WIDTH - ENEMY_IMAGE.get_width())
        y = random.randint(-WINDOW_HEIGHT, -2*ENEMY_IMAGE.get_height())
        speed = random.randint(1, 4)
        enemy = Enemy(ENEMY_IMAGE, x, y, speed)
        enemies.append(enemy)

    # 移動玩家和子彈
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and 0 <= player.rect.x-5 and player.rect.x-5 <= WINDOW_WIDTH:
        player.rect.x -= 3
    if keys[pygame.K_RIGHT] and 0 <= player.rect.x+5 and player.rect.x+5 <= WINDOW_WIDTH:
        player.rect.x += 3
    if keys[pygame.K_UP] and 0 <= player.rect.y-5 and player.rect.y-5 <= WINDOW_HEIGHT:
        player.rect.y -=3
    if keys[pygame.K_DOWN] and 0 <= player.rect.y+5 and player.rect.y+5 <= WINDOW_HEIGHT:
        player.rect.y +=3
        
    player.move_bullets()

    # 敵機移動
    for enemy in enemies:
        enemy.move()
        if enemy.rect.top > WINDOW_HEIGHT:
            x = random.randint(0, WINDOW_WIDTH - ENEMY_IMAGE.get_width())
            y = random.randint(-2*ENEMY_IMAGE.get_height(), -ENEMY_IMAGE.get_height())
            speed = random.randint(1, 4)
            enemy.rect.x = x
            enemy.rect.y = y

    # 生成新的敵機
    if len(enemies) < 10:
        x = random.randint(0, WINDOW_WIDTH - ENEMY_IMAGE.get_width())
        y = random.randint(-WINDOW_HEIGHT, -2*ENEMY_IMAGE.get_height())
        speed = random.randint(1, 6)
        enemy = Enemy(ENEMY_IMAGE, x, y, speed)
        enemies.append(enemy)

    # 碰撞檢測
    for b in player.bullets:
        for e in enemies:
            if b.rect.colliderect(e.rect):
                try:  
                    player.bullets.remove(b)
                    enemies.remove(e)
                    update_score(10)
                except:
                    update_score(10)
                    continue
    for e in enemies:
        if e.rect.colliderect(player.rect):
            enemies.remove(e)
		    # Start the GUI
            cmd = "python 2_question.py"
            output = subprocess.check_output(cmd, shell = True)
            output_str = output.decode("utf-8")
            return_value = output_str.strip()
            if return_value == 'True':
                time.sleep(1)
            else:
                game_over = True

            
    if not game_over:
        if score>=2000:
            game_over = True
            
    if not game_over:
        # 繪製遊戲元素
        WINDOW.blit(BACKGROUND_IMAGE, (0, 0))
        player.draw()
        player.draw_bullets()
        for enemy in enemies:
            enemy.draw()
    else:
        game_over_text = font.render("Game Over!", True, red)
        score_text = font.render("Final Score: {} ".format(score), True, red)
        WINDOW.blit(game_over_text, (200, 200))
        WINDOW.blit(score_text, (200, 250))
        show_score()
        pygame.display.update()
        time.sleep(3)
        break
        
    # 刷新遊戲頁面
    show_score()
    pygame.display.update()

    # 控制游戲頻率
    CLOCK.tick(100)