import sys, pygame, util
from pygame.locals import *
from Pollo import *
from carro import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
ICON_SIZE = 32

def game(): 
    pygame.init()
    pygame.mixer.init()
    jugando = True
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption('Juego del pollo')
    fuente = pygame.font.Font(None, 30)
    background_image = util.cargar_imagen('Imagenes/Fondo.png');
    pygame.mouse.set_visible( False )
    temporizador = pygame.time.Clock()
    pollo = Pollo()
    carro = [Carro((100,100),7)]
    while jugando:
        pollo.update()
        texto_vida = fuente.render("Puntaje: " + str(pollo.vida), 1, (250, 250, 250))
        for n in carro:
              n.update()
        pollo.image = pollo.imagenes[0]
        if pollo.rect.y == 430 and pollo.dir == "ab":
            pollo.vida += 1
            pollo.dir = "a"
        if pollo.rect.y == 0 and pollo.dir == "a":
            pollo.vida += 1
            pollo.dir = "ab"
        for n in carro:
              if pollo.rect.colliderect(n.rect):
                  jugando = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(background_image, (0,0))
        screen.blit(pollo.image, pollo.rect)
        for n in carro:
            screen.blit(n.image, n.rect)
        screen.blit(texto_vida, (20, 10))
        pygame.display.update()
        pygame.time.delay(10)


if __name__ == '__main__':
      game()


