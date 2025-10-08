import pygame

from constants import REFRESH_RATE, SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta_time = 0
    running = True

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    Player.containers = (updatables, drawables)  # type: ignore

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while running:
        screen.fill("black")

        updatables.update(delta_time)

        for drawable in drawables:
            drawable.draw(screen)

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
