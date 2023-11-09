import pygame
import random
import time

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (215, 40, 40)
GREEN = (22, 184, 78)

screen = pygame.display.set_mode((500, 800))
pygame.display.set_caption("race")
num_enemy_car = 10

myCar_y = 750
myCar_x = 250

enemy_cars = []

pygame.display.update()

class Car:
    def __init__(self, x, y, color = RED):
        self.x = x
        self.y = y
        self.width = 45
        self.height = 60
        self.speed = 10
        self.color = color

    def draw(self):
        self.car = pygame.draw.rect(screen, (self.color), (self.x, self.y, self.width, self.height))

    def move_y(self, direction = 1):
        self.y += self.speed * direction

    def move_x(self, direction = 1):
        self.x +=  self.speed * direction

    def colliderect(self, other_car):
        return self.car.colliderect(other_car.car)



for i in range(1, num_enemy_car):
    enemy_cars.append(Car(random.randint(10, 490), random.randint(-200 * i, -200 * i + 200)))

my_car = Car(myCar_x, myCar_y, WHITE)


running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        my_car.move_x(-1)
    if keys[pygame.K_d]:
        my_car.move_x(1)

    if keys[pygame.K_w]:
        my_car.move_y(-1)

    for enemy in enemy_cars:
        enemy.draw()

    my_car.draw()

    finish = pygame.draw.line(screen, (GREEN), (0, 0), (500, 0), 10)

    for enemy in enemy_cars:
        enemy.move_y()

    for enemy_car in enemy_cars:
        if my_car.colliderect(enemy_car):
            print('you lose')
            running = False

    if my_car.y <= 0:
        print('you won')
        running = False
   
    pygame.display.update()
    time.sleep(0.1)

pygame.quit()



            



