import pygame
pygame.init()
screen=pygame.display.set_mode((400,400))

while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            exit()
    screen.fill('light blue')
    pygame.display.update()
