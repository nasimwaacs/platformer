import pygame, sys
from pygame.locals import QUIT
import bunny, myplatform

WHITE = (255, 255, 255)
SKY = (135, 206, 235)
FPS = 30
WIDTH = 600
HEIGHT = 400

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bunny Run')

player = bunny.Bunny(x=80, y=200, scale_x=.2, scale_y=.2, speed_x=3, speed_y=3)

platform = myplatform.Platform()

clock = pygame.time.Clock()
while True:
	screen.fill(SKY)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			
	player.update()
	player.blit(screen)
	platform.blit(screen)

	if (player.onPlatform(platform)):
		player.speed_y = 0
	else:
		player.speed_y = 3

	pygame.display.update()
	clock.tick(FPS)


