import pygame

character = pygame.image.load('image\\player.png')


# cha1 = [character.subsurface(14, 0, 30, 55),
cha1 = [character.subsurface(1, 703, 50, 60),
		character.subsurface(75, 697, 47, 60),
		character.subsurface(199, 697, 48, 60),
		character.subsurface(326, 697, 47, 60),
		character.subsurface(385, 709, 62, 60),  
		character.subsurface(578, 697, 52, 60)]

cha2 = [character.subsurface(2, 448, 52, 62),
		character.subsurface(75, 441, 47, 60), 
		character.subsurface(200, 441, 47, 60), 
		character.subsurface(325, 441, 47, 60), 
		character.subsurface(385, 452, 62, 60), 
		character.subsurface(580, 441, 50, 60)]

cha3 = [character.subsurface(2, 640, 52, 62),
		character.subsurface(75, 633, 47, 60), 
		character.subsurface(200, 633, 47, 60),
		character.subsurface(324, 633, 47, 60),
		character.subsurface(385, 646, 62, 60),  
		character.subsurface(578, 633, 52, 60)]  

cha4 = [character.subsurface(0, 769, 48, 62),
		character.subsurface(78, 762, 47, 60),
		character.subsurface(200, 762, 48, 60),
		character.subsurface(324, 762, 47, 60),
		character.subsurface(385, 772, 62, 60), 
		character.subsurface(581, 765, 52, 60)]

cha5 = [character.subsurface(1, 512, 52, 62),
		character.subsurface(75, 505, 47, 60),
		character.subsurface(199, 505, 48, 60),  
		character.subsurface(326, 505, 47, 60),
		character.subsurface(385, 518, 62, 60),   
		character.subsurface(578, 505, 52, 60)]

van = [character.subsurface(73, 10, 51, 60),
		character.subsurface(73, 10, 51, 60),
		character.subsurface(199, 10, 48, 60),
		character.subsurface(324, 10, 51, 60),
		character.subsurface(385, 0, 62, 50),
		character.subsurface(576, 10, 64, 60)]

characters = [cha1,cha2,cha3,cha4,cha5]

class Character():
	def __init__(self, characters, index, x, y, van):
		self.index = index
		self.characters = characters[self.index]
		self.character_index = 0
		self.van = van
		self.x = x
		self.y = y
		self.y_collide = y
		self.y_jump = 160
		self.rect = pygame.Rect(self.x+10,self.y_collide+40,20,10)
		self.jumping = False
		self.jumping_countdown = 0
		self.speed_default = 1.5
		self.speed = self.speed_default
		self.boots = False
		self.boots_countdown = 200
		self.collide = False
		self.collide_countdown = 70
		self.death = False
		self.coin = 0

		self.healthbar = Bar(650,245,150,15,3,(255,0,0),(50,50,50))
		self.bootbar = Bar(650,275,150,15,3,(0,255,255),(50,50,50))

	def update_animation(self, screen, status): # update character's animation when changing mouse's position
		
		pressKey = False
		key = pygame.key.get_pressed()

		if key[pygame.K_DOWN] and not self.boots and self.bootbar.value == 3:
			pressKey = True
			self.boots = True
			self.boots_countdown = 200
			self.y = self.y_jump
			self.speed = self.speed_default*2
			self.bootbar.value -= 3

		else:
			if key[pygame.K_UP] and not self.jumping and not self.boots and self.bootbar.value >= 1:
				pressKey = True
				self.y = self.y_jump
				self.jumping = True
				self.jumping_countdown = 150
				self.bootbar.value -= 1

			else:
				if key[pygame.K_LEFT] and self.x > 0 and not self.boots:
					pressKey = True
					self.x -= 1
					if not self.jumping:
						self.character_index = 1

				else:
					if key[pygame.K_RIGHT] and self.x < 570 and not self.boots:
						pressKey = True
						self.x += 1
						if not self.jumping:
							self.character_index = 3
		
		if self.jumping:
			self.jumping_countdown -= 1
			if self.jumping_countdown == 0:
				self.y = self.y_jump + 40
				self.jumping = False
			self.character_index = 5
			pygame.draw.ellipse(screen,(102,102,102),(self.x+10,self.y+90,25,15))

		if self.boots:
			self.boots_countdown -= 1
			if self.boots_countdown == 0:
				self.boots = False
				self.y = self.y_jump + 40
			self.character_index = 5
			pygame.draw.ellipse(screen,(102,102,102),(self.x+10,self.y+90,25,15))

		if not self.jumping and not self.boots:
			if not pressKey:
				self.character_index = 2
			self.speed = self.speed_default

		if status:
			self.y_collide += self.speed
		self.rect = pygame.Rect(self.x+15,self.y_collide+50,20,10)
		# pygame.draw.rect(screen, (0,0,0), (self.x+15,self.y+50,20,10), 1)
		# pygame.draw.rect(screen, (0,0,0), self.rect, 1)

		self.bootbar.update(screen)
		self.healthbar.update(screen)

		if self.collide:
			self.collide_countdown -= 1
			if self.collide_countdown == 0:
				self.collide = False
				self.collide_countdown = 70

		if self.healthbar.value == 0:
			self.death = True

class Bar():
	def __init__(self, x,y, width,height, value,color_value, color_bg):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.rect = pygame.Rect(self.x,self.y,self.width,self.height)

		self.value = value
		self.color_value = color_value
		self.color_bg = color_bg

	def update(self, screen):
		pygame.draw.rect(screen, self.color_bg, self.rect, 0, 5)
		value_rect = pygame.Rect(self.x,self.y,self.width*self.value/3,self.height)
		pygame.draw.rect(screen, self.color_value, value_rect, 0, 5)

class Obstacle():
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.rect = pygame.Rect((self.x,self.y,self.width,self.height))

