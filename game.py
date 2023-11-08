import pygame
import random
import sys

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (215, 40, 40)
GREEN = (22, 184, 78)

screen = pygame.display.set_mode((500, 800))
pygame.display.set_caption("race")
num_enemyCar = 10
enemyCar_Y = random.randint(-50, 700)
enemyCar_X = random.randint(10, 490)
enemyCarSpeed = 1
myCar_y = 750
myCar_x = 250
car_wedth = 45
car_height = 60
myCarSpeed = 2
enemyCars = []
enemiesXY = []
myCar = pygame.draw.rect(screen, (WHITE), (myCar_x, myCar_y, car_wedth, car_height))

pygame.display.update()

def drawEnemy():
    screen.fill((BLACK))
    enemyCar_Y = random.randint(-100, 600)
    enemyCar_X = random.randint(10, 490)
    enemyCar = pygame.draw.rect(screen, (RED), (enemyCar_X, enemyCar_Y, car_wedth, car_height))
    myCar = pygame.draw.rect(screen, (WHITE), (myCar_x, myCar_y, car_wedth, car_height))
    finish = pygame.draw.line(screen, (GREEN), (0, 0), (500, 0), 10)

class enemies:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 45
        self.height = 60
        self.speed = 1
    def draw(self):
        enemyCar = pygame.draw.rect(screen, (RED), (self.x, self.y, self.width, self.height))
        enemyCars.append(enemyCar)

    def move(self):
        self.y += self.speed


enemy = enemies(random.randint(10, 490), random.randint(-200, 0))
enemy1 = enemies(random.randint(10, 490), random.randint(-200, 0))
enemy2 = enemies(random.randint(10, 490), random.randint(-400, -200))
enemy3 = enemies(random.randint(10, 490), random.randint(-400, -200))
enemy4 = enemies(random.randint(10, 490), random.randint(-600, -400))
enemy5 = enemies(random.randint(10, 490), random.randint(-600, -400))
enemy6 = enemies(random.randint(10, 490), random.randint(-800, -600))
enemy7 = enemies(random.randint(10, 490), random.randint(-800, -600))
enemy8 = enemies(random.randint(10, 490), random.randint(-1000, -800))
enemy9 = enemies(random.randint(10, 490), random.randint(-1000, -800))

    

running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        myCar_x -= myCarSpeed
    if keys[pygame.K_d]:
        myCar_x += enemyCarSpeed
    if keys[pygame.K_w]:
        myCar_y -= myCarSpeed

    enemy.draw()
    enemy1.draw()
    enemy2.draw()
    enemy3.draw()
    enemy4.draw()
    enemy5.draw()
    enemy6.draw()
    enemy7.draw()
    enemy8.draw()
    enemy9.draw()

    myCar = pygame.draw.rect(screen, (WHITE), (myCar_x, myCar_y, car_wedth, car_height))
    finish = pygame.draw.line(screen, (GREEN), (0, 0), (500, 0), 10)
    enemy.move()
    enemy1.move()
    enemy2.move()
    enemy3.move()
    enemy4.move()
    enemy5.move()
    enemy6.move()
    enemy7.move()
    enemy8.move()
    enemy9.move()

    for enemyCar in enemyCars:
        if myCar.colliderect(enemyCar):
            print('you lose')
            running = False
    if myCar_y <= 0:
            print('you won')
            running = False
   
    pygame.display.update()

pygame.quit()



            



