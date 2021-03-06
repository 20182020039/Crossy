import pygame
from pygame.sprite import Sprite
from pygame import *
import util

class Pollo(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.imagenes = [util.cargar_imagen('Imagenes/pollo de regreso.png'),util.cargar_imagen('Imagenes/pollo de lado.png'),util.cargar_imagen('Imagenes/pollo de lado derecho.png'),util.cargar_imagen('Imagenes/pollo espalda.png')]
		self.image = self.imagenes[0]
                self.rect = self.image.get_rect()
		self.rect.move_ip(200, 10)
		self.puntaje = 0
		self.dir = "ab"

	def update(self):
		teclas = pygame.key.get_pressed()
		if teclas[K_LEFT] and self.rect.x>=10:
			self.rect.x -= 10
			self.imagenes[0] = self.imagenes[1]
		elif teclas[K_RIGHT] and self.rect.x<=640-self.rect.width:
			self.rect.x += 10
			self.imagenes[0] = self.imagenes[2]
		if teclas[K_UP] and self.rect.y>=10:
			self.rect.y -= 10
			self.imagenes[0] = self.imagenes[3]
		elif teclas[K_DOWN] and self.rect.y<=480-self.rect.height:
			self.rect.y += 10
			

