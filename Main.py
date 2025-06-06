# import pygame
# pygame.init()
#
# pygame.display.set_caption("ceci est un test")
# pygame.display.set_mode((960,600))
#
# running = True
# eventCounter = 0
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#             pygame.quit()
#             print('fermeture du jeu!!!!')
#         else:
#             print('some event occured ' + str(eventCounter))
#         eventCounter += 1

def additionDeDeuxNombres(a: int, b: int) -> (int, int):
    print('je suis dans la fonction additionDeDeuxNombres et le nombre a est ' + str(a))
    return (a*b, a+b)


def additionDeTroisNombres(a: int, b: int, c: int) -> int:
    return a + b + c



def maFonctgionDetoutenfaut() -> None:
    aa = 8
    bb = 5
    (c, d) = additionDeDeuxNombres(aa, bb)
    print(c)
    print(d)
    variable = additionDeTroisNombres(1,2,3)
    print(variable)

maFonctgionDetoutenfaut()