import pygame
import random

#define colours

YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 255, 255)
PINK = (255, 153, 153)
RED = (255,0,0)


#image

how_bg = pygame.image.load('image\\bg.webp')

background = pygame.image.load('image\\bg2.webp')
background = pygame.transform.scale(background, (1268,720))
print(background.get_width())
print(background.get_height())

select_bg = pygame.image.load("image\\select_bg.png")

#set font
pygame.font.init()
comicsan = pygame.font.SysFont('Comic Sans MS', 20)
console = pygame.font.SysFont('lucidaconsole', 40)

class Button():
	def __init__(self, x, y, width, height, text, text_size, color,screen):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.width_highlight = width*2
		self.height_highlight = height*2

		self.text = pygame.font.SysFont('Comic Sans MS', text_size).render(text, False, BLACK)
		self.text_highlight = pygame.font.SysFont('Comic Sans MS', text_size*2).render(text, False, BLACK)
		self.color = color
		self.color_highlight = BLUE
		self.color_update = color

		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
		self.rect_highlight = pygame.Rect(self.x-self.width/2, self.y-self.height/2, self.width_highlight, self.height_highlight)

		self.txt_rect = self.text.get_rect(center = (self.x + self.width/2, self.y + self.height/2))
		self.txt_rect_highlight = self.text_highlight.get_rect(center = (self.x + self.width/2, self.y + self.height/2))
		
		
	def update(self,screen):
		mouse_x, mouse_y = pygame.mouse.get_pos()
		if self.rect.collidepoint(mouse_x, mouse_y):
			self.color_update = self.color_highlight
			pygame.draw.rect(screen, self.color_update, self.rect_highlight, 0, 5)
			screen.blit(self.text_highlight,self.txt_rect_highlight)

		else:
			self.color_update = self.color
			pygame.draw.rect(screen, self.color_update, self.rect, 0, 5)
			screen.blit(self.text,self.txt_rect)
		

obstacles = pygame.image.load('image\\objects2.png')
Tree = [obstacles.subsurface(390, 65, 55, 50),
		obstacles.subsurface(450, 65, 50, 50),
		obstacles.subsurface(515, 65, 55, 50),
		obstacles.subsurface(580, 65, 50, 50),
		obstacles.subsurface(640, 65, 55, 50),
		obstacles.subsurface(700, 65, 65, 60),
		obstacles.subsurface(780, 0, 40, 60),
		obstacles.subsurface(830, 10, 50, 50),
		obstacles.subsurface(900, 23, 55, 30),
		obstacles.subsurface(780, 65, 50, 50),
		obstacles.subsurface(830, 75, 65, 50),
		obstacles.subsurface(900, 65, 65, 60)]
Wood = [obstacles.subsurface(0, 60, 50, 60),
		obstacles.subsurface(75, 65, 60, 50),
		obstacles.subsurface(130, 95, 60, 33),
		obstacles.subsurface(200, 95, 60, 30),
		obstacles.subsurface(260, 65, 65, 60),
		obstacles.subsurface(320, 80, 65, 50)]
Obs = [obstacles.subsurface(390, 0, 55, 50),
		obstacles.subsurface(450, 0, 50, 50),
		obstacles.subsurface(515, 0, 55, 50),
		obstacles.subsurface(640, 20, 65, 50),
		obstacles.subsurface(700, 0, 65, 60),
		obstacles.subsurface(390, 300, 125, 70),
		obstacles.subsurface(515, 269, 125, 100),
		obstacles.subsurface(640, 300, 125, 70),
		obstacles.subsurface(770, 260, 60, 125),
		obstacles.subsurface(835, 260, 65, 125),
		obstacles.subsurface(900, 259, 70, 125),
		obstacles.subsurface(0, 126, 127, 120),
		obstacles.subsurface(390, 140, 180, 120),
		obstacles.subsurface(580, 126, 200, 120),
		obstacles.subsurface(770, 130, 180, 120)]
Glass = [obstacles.subsurface(1550, 0, 65, 65),
		obstacles.subsurface(1800, 0, 65, 65)]
Gate = obstacles.subsurface(0, 280, 388, 230)

obsrect = []

def insert_map(Map, arr, obsrect, begin, end, step, num1,num2, b):
	for y in range(begin,end,step):
		n = random.randint(num1,num2)
		for m in range(n):
			i = random.randint(0, len(arr)-1)
			x = random.randint(0, 550)

			r = pygame.Rect(5,5,5,5).inflate(arr[i].get_width()*5/7,arr[i].get_height()*5/7)
			r.center = (x,y)
			r2 = arr[i].get_rect(center = (x,y))

			Map.map.blit(arr[i], r2)
			if b:
				# pygame.draw.rect(Map.map, (YELLOW), r,5)
				obsrect.append(r)
map_piece = pygame.transform.scale(pygame.image.load('image\\bg.png'), (400,400))
class Map():
	def __init__(self):
		self.map = pygame.Surface((600,10700))
		self.map.fill((214, 228, 229))
		# self.map.fill((247, 247, 247))
		# self.map.fill((207, 245, 231))
		self.x = 0
		self.y = 0

		for x in range(0,600,400):
			for y in range(0,10000,400):
				self.map.blit(map_piece,(x,y))

		#create glass
		insert_map(self, Glass, obsrect, 900, 9800, 100, 1, 2, False)

		#create tree
		insert_map(self, Tree, obsrect, 700, 9800, 300, 1, 1, True)

		#create wood
		insert_map(self, Wood, obsrect, 700, 9800, 300, 2, 4, True)
		
		#create obs
		insert_map(self, Obs, obsrect, 900, 9800, 300, 1, 3, True)

		#create gate
		# r = Gate.get_rect(center = (300,19900))
		# self.map.blit(Gate, r)
		pygame.draw.rect(self.map,WHITE,(0,9980,1000,20))
		for i in range(0,1000,60):
			pygame.draw.rect(self.map,BLACK,(i,9980,30,10))
			pygame.draw.rect(self.map,BLACK,(i+30,9990,30,10))

	def update(self,speed):
		self.y -= speed


class Enemy():
	def __init__(self, x , y):
		self.enemy = [obstacles.subsurface(1177, 280, 82, 100),#0
					obstacles.subsurface(1305, 280, 82, 100),#1
					obstacles.subsurface(1433, 280, 82, 100),#2
					obstacles.subsurface(1561, 280, 82, 100),#3
					obstacles.subsurface(1689, 280, 82, 100),#4
					obstacles.subsurface(1817, 280, 82, 100),#5
					obstacles.subsurface(1175, 390, 82, 122),#6
					obstacles.subsurface(1303, 390, 82, 122),#7
					obstacles.subsurface(1431, 390, 82, 122),#8
					obstacles.subsurface(1559, 390, 82, 122),#9
					obstacles.subsurface(1687, 390, 82, 122),#10
					obstacles.subsurface(1815, 390, 82, 122)]#11
		self.index = 0
		self.x = x
		self.y = y
	def update(self):
		if self.y < 110:
			if self.index < 5:
				self.index += 1
			else:
				self.index = 0
		else:
			if self.index < 11:
				self.index += 1
			else:
				self.index = 6

key = pygame.transform.scale(pygame.image.load('image\\key.png'), (225,156))
keys = [key.subsurface(6,85,66,65),
		key.subsurface(80,85,66,65),
		key.subsurface(154,85,66,65),
		key.subsurface(80,11,66,65)]
class arrowKey():
	def __init__(self, key, x, y):
		self.x = x
		self.y = y
		self.key_index = key
		self.key = keys[key]
		self.nohighlight = (100,100,100)#(89, 193, 189)
		self.highlight = (255,255,255)
		self.color = self.nohighlight
		self.rect = keys[key].get_rect(center = (x,y))

	def update(self, screen):
		mouse_x, mouse_y = pygame.mouse.get_pos()

		k = pygame.key.get_pressed()
		i = -1
		if k[pygame.K_LEFT]:
			i = 0
		if k[pygame.K_DOWN]:
			i = 1
		if k[pygame.K_RIGHT]:
			i = 2
		if k[pygame.K_UP]:
			i = 3
		if i == self.key_index:
			self.color = self.highlight
		else:
			self.color = self.nohighlight

		pygame.draw.rect(screen, self.color, self.rect, 0, 10)
		screen.blit(self.key, self.rect)

member = pygame.image.load("image\\member.png")
def infor(screen, player, score):
	screen.blit(pygame.font.SysFont('Comic Sans MS', 20).render(str(score), False, BLACK), (620,300))
	screen.blit(pygame.font.SysFont('Comic Sans MS', 20).render("Score", False, BLACK), (930,300))
	pygame.draw.line(screen, BLACK, (610,350),(980,350))

	player.bootbar.update(screen)
	screen.blit(pygame.transform.scale(booticon[0], (23,30)), (615,270))
	screen.blit(pygame.font.SysFont('Comic Sans MS', 20).render("Boots", False, BLACK), (930,270))

	player.healthbar.update(screen)
	screen.blit(pygame.transform.scale(hearticon[0], (23,30)), (615, 240))
	screen.blit(pygame.font.SysFont('Comic Sans MS', 20).render("Health", False, BLACK), (930,240))

	screen.blit(pygame.transform.scale(coinicon[0], (23,30)), (615, 210))
	screen.blit(pygame.font.SysFont('Comic Sans MS', 20).render("    x " + str(player.coin), False, BLACK), (630,210))
	screen.blit(pygame.font.SysFont('Comic Sans MS', 20).render("Coin", False, BLACK), (930,210))

	# screen.blit(pygame.transform.scale(member,(330,300)), (620,360))


booticon = [obstacles.subsurface(1036, 5, 46, 60),
		obstacles.subsurface(1036, 69, 46, 60),
		obstacles.subsurface(1036, 133, 46, 60),
		obstacles.subsurface(1036, 197, 46, 60)]

hearticon = [obstacles.subsurface(1096, 5, 49, 58),
		obstacles.subsurface(1096, 69, 49, 58),
		obstacles.subsurface(1096, 133, 49, 58),
		obstacles.subsurface(1096, 197, 49, 58),]

coinicon = [obstacles.subsurface(972, 265, 44, 54),
		obstacles.subsurface(972, 329, 44, 54),
		obstacles.subsurface(972, 393, 44, 54),
		obstacles.subsurface(972, 457, 44, 54)]

item = [hearticon[0], booticon[0], coinicon[0], coinicon[0], coinicon[0]]
items = []
class Item():
	def __init__(self, x, y, icon_i):
		self.x = x
		self.y = y
		self.item = item[icon_i]
		self.icon_i = icon_i
		items.append(self)

	def update(self,screen,player):
		self.y -= player.speed

		item_rect = self.item.get_rect(center = (self.x,self.y))
		player_rect = pygame.Rect(player.x+15,player.y+50,20,10)

		screen.blit(self.item, item_rect)
		if self.y < 0 or item_rect.colliderect(player_rect):
			if self.icon_i == 0 and player.healthbar.value < 3:
				player.healthbar.value += 1
			else:
				if self.icon_i == 1 and player.bootbar.value < 3:
					player.bootbar.value += 1
				else:
					if self.icon_i == 2 or self.icon_i == 3 or self.icon_i == 4:
						player.coin += 1
			items.remove(self)
		



print(booticon[0].get_width())
print(booticon[0].get_height())

# pygame.init()

# #create game window
# SCREEN_WIDTH = 600 #pixel
# SCREEN_HEIGHT = 700 #pixel

# screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) 
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Intro")
# clock = pygame.time.Clock()
# FPS = 250

# i = 0

# run = True
# while run:
# 		screen.fill(PINK)
# 		clock.tick(FPS)
		
# 		screen.blit(booticon[i], (200,200))
# 		screen.blit(hearticon[i], (200,300))
# 		screen.blit(coinicon[i], (200,400))

# 		mouse_x, mouse_y = pygame.mouse.get_pos()
# 		#event handler
# 		for event in pygame.event.get():
# 			if event.type == pygame.QUIT:
# 				choice = 0
# 				run = False

# 		pygame.display.flip()