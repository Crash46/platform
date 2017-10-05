#sprite classes
import pygame
from settings import *
#create 2dimentional vector variable
vec = pygame.math.Vector2
#player
class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((30, 40))
		self.image.fill(YELLOW)
		self.rect = self.image.get_rect()
		#position in the center of the screen
		self.rect.center = (WIDTH / 2 , HEIGTH / 2)
		#acceleration / vector...
		self.pos = vec(WIDTH/2 , HEIGTH/2)
		self.vel = vec(0, 0)
		self.acc = vec(0, 0)


	def update(self):
		self.acc = vec(0, 0.5)
		self.vx = 0 
		# check for key action -> add velocity and acceleration
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			self.acc.x = -PLAYER_ACC
		if keys[pygame.K_RIGHT]:
			self.acc.x = PLAYER_ACC
			#add acceleration and velocity - phisics  to draw
		#Apply FRICTION only horizontaly
		self.acc.x += self.vel.x * PLAYER_FRICTION

		#equations of motion
		self.vel += self.acc
		self.pos+=self.vel + 0.3 * self.acc
		#wrap around the sides of the screen
		if self.pos.x > WIDTH:
			self.pos.x = 0
		if self.pos.x<0:
			self.pos.x = WIDTH

		#self position = self bottom
		self.rect.midbottom = self.pos

class Platform(pygame.sprite.Sprite):
	def __init__(self, x , y, w , h):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((w, h ))
		self.image.fill(GREEN)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y