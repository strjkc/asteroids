import sys
from asteroidfield import AsteroidField
from player import Player
from asteroid import Asteroid
from shot import Shot
import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    loaded = pygame.init()
    print(f"Loaded {loaded[0]} modules")
    print(f"Failed to load {loaded[1]} modules")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0,0,0))
        for item in updatable:
            item.update(dt)
        for asteroid in asteroids:
            if player.check_collisions(asteroid):
                print("Game Over!")
                sys.exit()
            for bullet in shots:
                if bullet.check_collisions(asteroid):
                    asteroid.split()
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        rt_val = clock.tick(60)
        dt = rt_val / 1000

if __name__ == "__main__":
    main()
