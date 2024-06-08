import pygame

# Making this Bunny a pygame sprite has some benefits... using sprite groups
class Bunny(pygame.sprite.Sprite):
	def __init__(self, filename="bunny.png", scale_x=1, scale_y=1, x=0, y=0, speed_x=1, speed_y=0, opacity=200, tolerance=5):
		
		pygame.sprite.Sprite.__init__(self)
		
		self.image = pygame.image.load(filename)
		self.image.set_alpha(opacity)            #change the opacity
		w = self.image.get_width()*scale_x
		h = self.image.get_height()*scale_y
		self.image = pygame.transform.scale(self.image, (w, h))
		#self.image = pygame.transform.flip(self.image, True, True)
		self.rect = self.image.get_rect()

		self.x = x
		self.y = y
		
		self.rect.x = self.x
		self.rect.y = self.y
		
		self.speed_x = speed_x
		self.speed_y = speed_y

		self.tolerance = tolerance
		
	def blit(self, screen):
		screen.blit(self.image, self.rect)
	
	def move(self, speed):
		self.rect = self.rect.move(speed) 
	
	def update(self):
		# check for keys pressed
		keys_pressed = pygame.key.get_pressed()
		
		if keys_pressed[pygame.K_LEFT]:
			self.move([-self.speed_x, 0])
			
		if keys_pressed[pygame.K_RIGHT]:
			self.move([self.speed_x, 0])
		
		if keys_pressed[pygame.K_UP]:
			self.move([0, -self.speed_y])

		if keys_pressed[pygame.K_DOWN]:
			self.move([0, self.speed_y])

	def onPlatform(self, platform):
		# Check if this sprite sprite is on top of the platform
		if (self.rect.bottom >= platform.rect.top and
			self.rect.bottom <= platform.rect.top + self.tolerance and  # small tolerance for float inaccuracies
			self.rect.right > platform.rect.left and
			self.rect.left < platform.rect.right):
			print("Sprite is on the platform!")

			return True

		return False
			
