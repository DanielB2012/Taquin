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


class Eleve:
    def __init__(self, name : str, age0 : int):
        self.nom = name
        self.age = age0

    def travaille(self):
        print("l'eleve {} travail".format(self.nom))

    def dort(self):
        print("l'eleve {} dort".format(self.nom))

    def presenteToi(self):
        print("Bonjour je m'appelle {} et j'ai {} ans".format(self.nom, str(self.age)))



eleve1 = Eleve ('Alban', 13)
eleve1.travaille()
eleve2 = Eleve ('Daniel', 12)
eleve2.dort()

eleve2.presenteToi()
