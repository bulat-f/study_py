import pygame
import random

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (215, 40, 40)
GREEN = (22, 184, 78)

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("race")
clock = pygame.time.Clock()
num_enemyCar = 10
# enemyCar_Y = random.randint(-400, 400)
# enemyCar_X = random.randint(0, 400)
# enemyCarSpawn = enemyCar_X, enemyCar_Y
# myCar_y = 400
# myCar_x = 200
# car_wedth = 50
# car_height = 75
# myCarSpawn = 200, 400
enemyCars = []
myCars = []
# myCar = pygame.draw.rect(screen, (WHITE), (myCar_x, myCar_y car_wedth, car_height))
# finish = pygame.draw.line(screen, (GREEN), (0, -400), (400, -400), 10)

pygame.display.update()
game_over = False

# for enemies in range(num_enemyCar):
#     enemyCar_Y = random.randint(-400, 400)
#     enemyCar_X = random.randint(0, 400)
#     enemyCarSpawn = enemyCar_X, enemyCar_Y
#     car_wedth = 50
#     car_height = 75
#     enemyCar = pygame.draw.rect(screen, (RED), (enemyCarSpawn, car_wedth, car_height))
#     enemyCars.append(enemyCar)
    

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        screen.fill((BLACK))
        for enemies in range(num_enemyCar):
            enemyCar_Y = random.randint(-400, 400)
            enemyCar_X = random.randint(0, 400)
            enemyCarSpawn = enemyCar_X, enemyCar_Y
            car_wedth = 50
            car_height = 75
            enemyCar = pygame.draw.rect(screen, (RED), (enemyCar_X, enemyCar_Y, car_wedth, car_height))
            enemyCars.append(enemyCar)
        for mine in range(1):
            myCar_y = 400
            myCar_x = 200
            car_wedth = 50
            car_height = 75
            myCarSpawn = 200, 400
            myCar = pygame.draw.rect(screen, (WHITE), (myCar_x, myCar_y, car_wedth, car_height))
            myCars.append(myCar)
        finish = pygame.draw.line(screen, (GREEN), (0, -400), (400, -400), 10)
        screen.fill((BLACK))
        if pygame.key.get_pressed()[pygame.K_a]:
            myCar_x -= 5
        elif pygame.key.get_pressed()[pygame.K_d]:
            myCar_x += 5
        if pygame.key.get_pressed()[pygame.K_w]:
            myCar_y += 10
        if myCar_x == enemyCar_X or myCar_y == enemyCar_Y:
            print('you lose')
            game_over = True
        elif myCar_y == finish:
            print('you won')
            game_over = True
    pygame.display.flip()
    clock.tick(30)
    pygame.quit()
if __name__ == "__main__":
    main()
            



