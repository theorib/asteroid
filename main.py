import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import REFRESH_RATE, SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta_time = 0
    running = True

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)  # type: ignore
    Player.containers = (updatable, drawable)  # type: ignore
    AsteroidField.containers = (updatable,)  # type: ignore

    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    while running:
        screen.fill("black")

        updatable.update(delta_time)

        for item in drawable:
            item.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.flip()

        last_call = clock.tick(REFRESH_RATE)
        delta_time = last_call / 1000
    # print("Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.quit()


if __name__ == "__main__":
    main()
