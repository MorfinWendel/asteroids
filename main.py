import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    pygame.init()
    pygame.font.init()
    font = pygame.font.Font(None, 36)
    score = 0
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable) 
    Shot.containers = (updatable, drawable, shots)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for entity in updatable:
            entity.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                if player.lives > 1:
                    player.lives -= 1
                    print(f"Live lost! Remaining lives: {player.lives}")
                    player.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                else:
                    print("Game over!")
                    return
            for bullet in shots:
                if bullet.collision(asteroid):
                    asteroid.split()
                    bullet.kill()
                    score += SCORE_INCREMENT

        screen.fill('black')
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        lives_text = font.render(f'Lives: {player.lives}', True, (255, 255, 255))
        screen.blit(score_text, (10,10))
        screen.blit(lives_text, (1100,10))
        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()
