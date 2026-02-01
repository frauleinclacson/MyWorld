## Engine of the Main Game
import pygame
from core.scene_manager import SceneManager
from world.world_manager import WorldManager
from characters.character_manager import ChharacterManager
from ui.main_menu import MainMenu
from monetization.package_manager import PackageManager

class GameEngine:
    def __init__(self, config):
        self.config = config
        self.screen = pygame.display.set_mode((config. SCREEN_WIDTH, config.SCREEN_HEIGHT))
        pygame.display.set_caption("My World Game")

        #Managers Initialized
        self.scene_manager = SceneManager ()
        self.world_manager = WorldManager ()
        self.character_manager = CharacterManager ()
        self.package_manager = PackageManager ()

        #Setting initial scene
        self.scene_manager.set_scene("Main_Menu")

    def handle_event(self, event):
        self.scene_manager.handle_event(event)

        #Swipe gestures handling world switching orr navigation
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.world_manager.previous_world()
            elif event.key == pygame.K_RIGHT:
                self.world_manager.next_world()

    def update (self, dt):
        self.scene_manager.update(dt)
        self.world_manager.update(dt)
        self.character_manager.update(dt)

    def render (self):
        self.screen.fill((135, 206, 235)) #Gives a sky blue background
        self.scene_manager.render(self.screen)
        self.world_manager.render(self.screen)
