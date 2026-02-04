## Manages everything world related
## World switching and themes
import json
import pygame
from worlds.residential_world import ResidentialWorld
from worlds.city_world import CityWorld
from worlds.nature_world import NatureWorld

class WorldManager:
    def __init__(self):
        self.worlds ==[]
        self.current_world_index = 0
        self.transition_progress = 0.0
        self.transitioning = False
        self.transition_speed = 2.0 #Transition speed

        self.load_world_themes()
        self.initialie_worlds()

    def load_world_theme(self):
        """Load the world themes from the configuration file"""
        try:
            with open('config/world_themes.json', 'r') as f:
                self.world_config = json.load(f)
        except FileNotFoundError:
            #Be able to create a config if file does not exist
            self.create_default_world_config()

    def create_default_world_config(self):
        """Create a default world configuration"""
        default_config = {
            "worlds": [
                {
                    "name": "The Residential Town",
                    "type": "residential",
                    "background": "assets/images/worlds/residential_bg.png",
                    "theme_color": [144, 238, 144],
                    "buildable_plots": 12,
                    "plot_positions": [
                        [300,300], [100,300],[500,300],
                        [300,300], [700,300], [100,300],
                        [100,300], [100,300], [700,300],
                        [500,300], [300,300], [500,300]
                    ]
                },
                {
                    "name": "My City Scape",
                    "type": "city",
                    "background": "assets/images/worlds/city_scape_bg.png",
                    "theme_color": [169,169,169],
                    "buildings": ["My Public School", "My University", "My General Hospital", "My Grocery Store", "My Shopping Center"]
                },
                {
                    "name": "My Nature Park",
                    "type": "nature",
                    "background": 
                }
            ]
        }