import pygame
from pygame.sprite import Sprite
from pygame import *
import util

class Carro(Sprite):
	def __init__(self,coord,vel):
		Sprite.__init__(self)
		self.image = util.cargar_imagen('Imagenes/coche1.png')
		self.rect = self.image.get_rect()
		self.rect.move_ip(coord[0], coord[1])
		self.dir = "l"
		self.velocidad=vel
        
	def update(self):
		if self.dir == "l":
			self.rect.x -= self.velocidad
		if self.rect.x<=-400:
			self.rect.x = 680

