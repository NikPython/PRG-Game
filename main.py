import pygame,random,sys

"""Настройки окна"""
window = pygame.display.set_mode((900,650),0,32)
pygame.display.set_caption('The Last Mage')
screen = pygame.Surface((900,500))
tabdown = pygame.Surface((900,150))
tabdown_frame = pygame.Surface((900,5))
tabup = pygame.Surface((900,30))
tabup_frame = pygame.Surface((900,5))

"""Настройки классов"""
class Sprite:
	def __init__(self,xpos,ypos,filename):
		self.x = xpos
		self.y = ypos
		self.bitmap = pygame.image.load(filename)
		self.bitmap.set_colorkey((255,255,255))
	def render(self):
		screen.blit(self.bitmap,(self.x,self.y))

def Intersect(x1,x2,y1,y2,db1,db2): # Функция взаимодейвия объектов
	if (x1>x2-db1) and (x1<x2+db2) and (y1>y2-db1) and (y1<y2+db2):
		return 1
	else:
		return 0

"""Создание объектов и переменных"""
player = Sprite(420,50, 'images/book.png')
bomb = Sprite(300,100,'images/bomb.png')

hp = 10

""" Основной игровой цикл (геймплей) """
done = True
pygame.key.set_repeat(1,1)
while done:
	"""Обработка событий"""
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			done = False
		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_ESCAPE:
				done = False
			if e.key == pygame.K_LEFT:
				if player.x > 1:
					player.x -= 1
			if e.key == pygame.K_RIGHT:
				if player.x < 834:
					player.x += 1
			if e.key == pygame.K_UP:
				if player.y > 1:
					player.y -= 1
			if e.key == pygame.K_DOWN:
				if player.y < 401:
					player.y += 1

	if Intersect(player.x, bomb.x, player.y, bomb.y, 64, 64):
		hp -= 1
		if hp == 0:
			done = False
		else:
			pass
	"""Закрашивание элементов"""
	screen.fill((0,255,20))
	tabdown.fill((0,149,182))
	tabdown_frame.fill((0,0,0))
	tabup.fill((0,149,182))
	tabup_frame.fill((0,0,0))

	"""Рендер элементов"""
	player.render()
	bomb.render()
	window.blit(screen,(0,35))
	window.blit(tabdown,(0,500))
	window.blit(tabdown_frame,(0,495))
	window.blit(tabup,(0,0))
	window.blit(tabup_frame,(0,30))
	pygame.display.flip()
