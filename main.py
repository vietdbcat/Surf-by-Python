import pygame, sys, time
from source import *
from player import *

pygame.init()

#create game window
SCREEN_WIDTH = 1000 #pixel
SCREEN_HEIGHT = 700 #pixel

# screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Surf")

#create character
player = Character(characters,0, 280, -100, van)
#set framerate
clock = pygame.time.Clock()
FPS = 300

#create score
score = 0

enemy_time = pygame.USEREVENT
pygame.time.set_timer(enemy_time, 150)

color_time = pygame.USEREVENT+1
pygame.time.set_timer(color_time, 30)
color = [GREEN, YELLOW, BLUE, PINK, RED]
color_i = 0

icon_time = pygame.USEREVENT+2
pygame.time.set_timer(icon_time, 4000)
icon_i = 0

choice = 1
def goto(choice):
	if choice >= 0:
		if choice == 0:
			sys.exit()
		if choice == 1:
			menu()
		if choice == 2:
			reset()
			gameplay()
		if choice == 3:
			howtoplay()
		if choice == 4:
			select_player()
		if choice == 5:
			gameover()

def gameplay():
	global score, player, choice, FPS, color_i, item
	m = Map()
	enemy = Enemy(260,-100)

	left = arrowKey(0, 730, 130)
	down = arrowKey(1, 800, 130)
	right = arrowKey(2, 870,130)
	up = arrowKey(3, 800, 60)

	

	#berore play
	run = True
	play = False
	while run:
		screen.fill((89, 193, 189))
		screen.blit(m.map,(m.x,m.y))
		clock.tick(FPS) #get the frame rate

		mouse_x, mouse_y = pygame.mouse.get_pos() #get mouse's position

		#event handler
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == enemy_time:
				enemy.update()
		if not play:
			player.y += 1
			if player.y == 200:
				play = True

		if play:
			enemy.y += 1
			if enemy.y == 40:
				run = False


		screen.blit(player.van[2] , (player.x,player.y+20))
		screen.blit(player.characters[2] , (player.x,player.y))
		screen.blit(enemy.enemy[enemy.index], (enemy.x, enemy.y))

		infor(screen, player, score)

		left.update(screen)
		down.update(screen)
		right.update(screen)
		up.update(screen)

		pygame.display.flip()

	#gameplay while loop
	win = False
	run = True
	while run:
		screen.fill((89, 193, 189))
		screen.blit(m.map,(m.x,m.y))
		clock.tick(FPS) #get the frame rate

		mouse_x, mouse_y = pygame.mouse.get_pos() #get mouse's position

		#event handler
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					choice = 5
					run = False
			if event.type == enemy_time:
				enemy.update()
			if event.type == color_time:
				if color_i < 4:
					color_i += 1
				else:
					color_i = 0
			if event.type == icon_time:
				x = random.randint(10, 550)
				y = random.randint(700,800)
				icon_i = random.randint(0,4)
				it = Item(x,y,icon_i)

		for x in items:
			x.update(screen,player)

		if not player.jumping and not player.boots:
			pygame.draw.circle(m.map, color[color_i], (player.x+19,player.y-m.y+50), 2)
			pygame.draw.circle(m.map, color[color_i], (player.x+28,player.y-m.y+50), 2)

		screen.blit(player.van[player.character_index] , (player.x,player.y+20))
		screen.blit(player.characters[player.character_index] , (player.x,player.y))

		player.update_animation(screen, True)

		m.update(player.speed)
		enemy.x = player.x-20
		screen.blit(enemy.enemy[enemy.index], (enemy.x, enemy.y))

		if m.y+10120 < player.y:
			win = True
			choice = 6
			run = False

		for o in obsrect:
			if o.colliderect(player.rect) and not player.jumping and not player.boots:
				if not player.collide:
					player.collide = True
					player.healthbar.value -= 1

		if player.death == True:
			choice = 5
			run = False
		
		score = (int)((player.y_collide - player.y)/100) + player.coin * 5
		
		infor(screen, player, score)

		
		left.update(screen)
		down.update(screen)
		right.update(screen)
		up.update(screen)

		pygame.display.flip()


	playagain = Button(120,300,100,40,'Play again!', 15, GREEN, screen)
	back = Button(320,300,100,40,'Menu', 15, GREEN, screen)

	#gameover while loop
	run = True
	while run:
		screen.fill((89, 193, 189))
		screen.blit(m.map,(m.x,m.y))
		clock.tick(FPS) #get the frame rate

		mouse_x, mouse_y = pygame.mouse.get_pos() #get mouse's position

		#event handler
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					choice = 1
					run = False
			if event.type == enemy_time:
				enemy.update()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if back.rect.collidepoint(mouse_x, mouse_y):
					choice = 1
					run = False
				if playagain.rect.collidepoint(mouse_x, mouse_y):
					choice = 2
					run = False

		if enemy.y < 110:
			enemy.y += 1

		screen.blit(player.van[4] , (player.x,player.y+20))
		screen.blit(player.characters[4] , (player.x,player.y))
		screen.blit(enemy.enemy[enemy.index], (enemy.x, enemy.y))

		infor(screen, player, score)
		
		left.update(screen)
		down.update(screen)
		right.update(screen)
		up.update(screen)

		if win:
			pygame.draw.rect(screen, BLUE, (100,100,400,500))
			screen.blit(pygame.font.SysFont('Comic Sans MS', 50).render("WIN GAME", False, BLACK), (100,250))

		playagain.update(screen)
		back.update(screen)

		pygame.display.flip()
	goto(choice)

def howtoplay():

	back = Button(450,570,100,40,'Menu', 15, GREEN, screen)

	run = True
	while run:

		screen.fill(PINK) #fill screen by color
		screen.blit(how_bg, (0,0))
		clock.tick(FPS) #get the frame rate

		pygame.draw.rect(screen, YELLOW, (100,100,800,500), 0, 10)
		screen.blit(pygame.font.SysFont('Times new roman', 30).render("1. Sử dụng các phím mũi tên để di chuyển.", False, BLACK), (200,200))
		screen.blit(pygame.font.SysFont('Times new roman', 30).render("2. Tránh các chướng ngại vật.", False, BLACK), (200,250))
		screen.blit(pygame.font.SysFont('Times new roman', 30).render("3. Giúp nhân vật đến đích trước khi bị bắt.", False, BLACK), (200,300))
		screen.blit(pygame.font.SysFont('Times new roman', 30).render("4. Sử dụng các vật phẩm để hỗ trợ trong quá trình chơi.", False, BLACK), (200,350))


		back.update(screen)

		# back.update(screen)
		mouse_x, mouse_y = pygame.mouse.get_pos() #get mouse's position

		#event handler
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					choice = 1
					run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if back.rect.collidepoint(mouse_x, mouse_y):
					choice = 1
					run = False

		pygame.display.flip()
	goto(choice)

def select_player():
	global player, choice

	back = Button(450,570,100,40,'Menu', 15, GREEN, screen)

	run = True
	while run:

		screen.fill((204, 255, 153)) #fill screen by color
		screen.blit(select_bg, (0,0))
		clock.tick(FPS) #get the frame rate

		back.update(screen)

		mouse_x, mouse_y = pygame.mouse.get_pos() #get mouse's position
		
		# pygame.draw.rect(screen, YELLOW, (200,200,600,300), 0, 20)
		pygame.draw.rect(screen, PINK, (250,100,500,100), 0, 20)

		screen.blit(pygame.font.SysFont('Times new roman', 50).render("CHỌN NHÂN VẬT", False, BLACK), (280,120))

		c1 = pygame.transform.scale(characters[0][0], (70,110)).get_rect(center = (300,300))
		c2 = pygame.transform.scale(characters[1][0], (70,110)).get_rect(center = (400,300))
		c3 = pygame.transform.scale(characters[2][0], (70,110)).get_rect(center = (500,300))
		c4 = pygame.transform.scale(characters[3][0], (70,110)).get_rect(center = (600,300))
		c5 = pygame.transform.scale(characters[4][0], (70,110)).get_rect(center = (700,300))

		screen.blit(pygame.transform.scale(characters[0][0], (70,110)), c1)
		screen.blit(pygame.transform.scale(characters[1][0], (70,110)), c2)
		screen.blit(pygame.transform.scale(characters[2][0], (70,110)), c3)
		screen.blit(pygame.transform.scale(characters[3][0], (70,110)), c4)
		screen.blit(pygame.transform.scale(characters[4][0], (70,110)), c5)


		#event handler
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					choice = 1
					run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if c1.collidepoint(mouse_x,mouse_y):
					choice = 1
					player.index = 0
					player.characters = characters[player.index]
					run = False
				if c2.collidepoint(mouse_x,mouse_y):
					choice = 1
					player.index = 1
					player.characters = characters[player.index]
					run = False
				if c3.collidepoint(mouse_x,mouse_y):
					choice = 1
					player.index = 2
					player.characters = characters[player.index]
					run = False
				if c4.collidepoint(mouse_x,mouse_y):
					choice = 1
					player.index = 3
					player.characters = characters[player.index]
					run = False
				if c5.collidepoint(mouse_x,mouse_y):
					choice = 1
					player.index = 4
					player.characters = characters[player.index]
					run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if back.rect.collidepoint(mouse_x, mouse_y):
					choice = 1
					run = False
				

		pygame.display.flip()
	goto(choice)

def reset():
	global score, obsrect, player, FPS, items
	items.clear()
	obsrect.clear()
	player.x = 280
	player.y = -100
	player.y_collide = 200
	player.healthbar.value = 3
	player.bootbar.value = 3
	player.death = False
	player.coin = 0
	score = 0
	# FPS = 250

def menu():
	global choice

	start = Button(100,100,150,50,'Start', 20, GREEN, screen)
	how = Button(100,220,150,50,'How to play', 20, YELLOW, screen)
	select = Button(100,340,150,50,'Select player', 20, PINK, screen)
	exit = Button(100,460,150,50,'Exit', 20, RED, screen)

	run = True
	while run:
		screen.fill(BLUE) #fill screen by color
		clock.tick(FPS) #get the frame rate

		screen.blit(background, (0,0))

		mouse_x, mouse_y = pygame.mouse.get_pos()

		start.update(screen)
		how.update(screen)
		select.update(screen)
		exit.update(screen)

		

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if start.rect.collidepoint(mouse_x, mouse_y):
					choice = 2
					run = False
				if how.rect.collidepoint(mouse_x, mouse_y):
					choice = 3
					run = False
				if select.rect.collidepoint(mouse_x,mouse_y):
					choice = 4
					run = False
				if exit.rect.collidepoint(mouse_x, mouse_y):
					choice = 0
					run = False

		pygame.display.flip()
	goto(choice)

goto(choice)
#exit pygame
pygame.quit()