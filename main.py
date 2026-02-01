import pygame
import sys
import os
from core.game_engine import GameEngine
from config.game_config import GameConfig

def main():
    pygame.init()

    #Game initialization
    config = GameConfig()
    game = GameEngine(config)

    #Loop of the game
    clock = pygame.time.Clock()
    running = True

    while running:
        dt = clock.tick(config.FPS) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game.handle_event(event)

        game.update(dt)
        game.render()

        pygame.display.flip()

    pygame.quit ()
    sys.exit ()
if __name__ == "__My World Main__"
    main()
