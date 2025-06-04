import pygame
pygame.init()

pygame.display.set_caption("ceci est un test")
pygame.display.set_mode((960,600))

running = True
eventCounter = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print('fermeture du jeu!!!!')
        else:
            print('some event occured ' + str(eventCounter))
        eventCounter += 1
