import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for entity in updatable:
            entity.update(dt)

        screen.fill('black')

        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()
