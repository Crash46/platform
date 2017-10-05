# Main fail 
import pygame
import random
from settings import *
from sprites import *

# Initialize game winodow etc
class Game:
	def __init__(self):
		#initializes pygame
		pygame.init()
		#add sound
		pygame.mixer.init()
		#window
		self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
		#title
		pygame.display.set_caption(TITLE)
		#FPS check
		self.clock = pygame.time.Clock()
		self.running = True
# Start for new game 
	def new(self):
		self.all_sprites = pygame.sprite.Group()
		self.platforms = pygame.sprite.Group()
		self.player = Player(self) 
		self.all_sprites.add(self.player)
		#above: self for inner 'reference' to game loop learn all variables and functions

		#manual spown of platform 
		p1 = Platform (0, HEIGTH - 40 , WIDTH , 40)
		self.all_sprites.add(self.player)	
		self.all_sprites.add(p1)
		self.platforms.add(p1)

		p2 = Platform(WIDTH /2 -50, HEIGTH*3/4, 100, 20)
		self.all_sprites.add(p2)
		self.platforms.add(p2)

		self.run()

# Initialize game loop ticks the clock checks for events update and draw on screen
	def run(self):
		
		self.playing = True
		while self.playing:
			self.clock.tick(FPS)
			self.events()
			self.update()
			self.draw()

# Game loop update
	def update(self):
		self.all_sprites.update()
		#only if falling
		if self.player.vel.y > 0:

			#colision check btw player and platforms; don;t deleat upon collision
			hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
			if hits:
				self.player.pos.y = hits[0].rect.top or hits[0].rect.midbottom
				self.player.vel.y = 0
# Game loops events
	def events(self):
		for event in pygame.event.get():
			#check for closing window
			if event.type == pygame.QUIT:
				if self.playing:
					self.playing = False
				self.running = False

			#jumping
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					self.player.jump()
# Game loop draw
	def draw(self):
		self.screen.fill(BLACK)
		self.all_sprites.draw(self.screen)
		pygame.display.flip()
# Start screen
	def show_start_screen(self):
		pass
# Game over screen
	def show_GO_screen(self):
		pass

# Variable and settings for game 'running'
g = Game()
g.show_start_screen()
while g.running:
	g.new()

	g.show_GO_screen()

pygame.quit()
