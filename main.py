import pygame
import sys
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill("#000000")

		for object in updatable:
			object.update(dt)

		for object in asteroids:
			if object.collisions(player):
				print("Game over!")
				sys.exit()

		for object in drawable:
			object.draw(screen)
		
		pygame.display.flip()

		dt = clock.tick(60)/1000




if __name__ == "__main__":
	main()
