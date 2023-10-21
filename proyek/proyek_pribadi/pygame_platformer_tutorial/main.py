import sys
import pygame as pg

from scripts.utils import load_image, load_images
from scripts.entities import PhysicsEntity
from scripts.tilemap import Tilemap

class Game:
    def __init__(self):
        pg.init()

        pg.display.set_caption('Ninja Game')
        self.screen = pg.display.set_mode((640, 480))
        self.display = pg.Surface((320, 240))

        self.clock = pg.time.Clock()
        
        self.movement = [False, False]
        
        self.assets = {
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'),
            'stone': load_images('tiles/stone'),
            'player': load_image('entities/player.png')
        }
        
        self.collision_area = pg.Rect((50, 50, 300, 50))
        
        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))
        
        self.tilemap = Tilemap(self, tile_size=16)
        
        self.scroll = [0, 0]

    def run(self):
        while True:
            self.display.fill((14, 219, 248))
            
            self.tilemap.render(self.display, offset = self.scroll)
            
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display, offset = self.scroll)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        self.movement[0] = True
                    elif event.key == pg.K_RIGHT:
                        self.movement[1] = True
                    elif event.key == pg.K_UP:
                        self.player.velocity[1] = -3
                if event.type == pg.KEYUP:
                    if event.key == pg.K_LEFT:
                        self.movement[0] = False
                    elif event.key == pg.K_RIGHT:
                        self.movement[1] = False
            
            self.screen.blit(pg.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pg.display.update()
            self.clock.tick(60)
   
Game().run()
         