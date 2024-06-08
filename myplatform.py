import pygame

# A rectangular platform
class Platform(pygame.sprite.Sprite):
	def __init__(self, position=(150, 200), width=200, height=20, color=(125, 199, 52), opacity=255, tolerance=5):
		
		pygame.sprite.Sprite.__init__(self)

		# rectangular surface
		self.surface = pygame.Surface((width, height))
		self.surface.fill(color)
		self.surface.set_alpha(opacity)          #set the opacity level 0-255
		self.rect = self.surface.get_rect()

		self.rect.topleft = position
		self.position = position

		self.tolerance = tolerance

	# Returns true if the given sprite is on top of this platform
	def onPlatform(self, sprite):
		# Check if the sprite is on top of the platform
		if (sprite.rect.bottom >= self.rect.top and
			sprite.rect.bottom <= self.rect.top + self.tolerance and  # small tolerance for float inaccuracies
			sprite.rect.right > self.rect.left and
			sprite.rect.left < self.rect.right):
			print("Sprite is on the platform!")

	def blit(self, screen):
		screen.blit(self.surface, self.rect)
	
	def update(self):
		# in case we decide to move it aroudn later on
		pass
			
