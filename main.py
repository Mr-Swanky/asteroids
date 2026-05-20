import pygame
import sys
from logger import log_event
from player import Player
from constants import *
from logger import log_state
from asteroidfield import *
from asteroids import Asteroid
from shot import Shot

def main():
    print("Creating groups...")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    print ("Groups created")

    print("Creating containers...")
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable,drawable)
    Shot.containers = (shots, updatable, drawable)
    print("Containers created")

    print("Initializing Asteroid Field...")
    field = AsteroidField()
    print("Asteroid Field Initialized")


    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    VERSION = pygame.version.ver
    clock = pygame.time.Clock()
    dt = 0
    print(f"Starting Asteroids with pygame version: {VERSION}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    while True:
        log_state()
        screen.fill("black")
        updatable.update(dt)
        player.cooldown -= dt
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
        for thing in drawable:
            thing.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        print(dt)
        pygame.display.flip()
if __name__ == "__main__":
    main()
