import pygame
import sys

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from logger import log_event, log_state
from player import Player
from shot import Shot


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()



# GAME LOOP START

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

# Update GAME positions
        updatable.update(dt)

# Do collision detection for all asteroids
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")  # Log the event
                print("Game over!")      # Notify the console
                sys.exit()               # Terminate execution immediately


# Render Screen
        screen.fill ("black")
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

# Set framerate to cap at 60fps
        dt = clock.tick(60) / 1000.0



if __name__ == "__main__":
    main()
