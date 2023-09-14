import sys
import pygame as pg

class Game:
    def __init__(self):
        pg.init()

        pg.display.set_caption("Ninja Game")
        self.screen = pg.display.set_mode((640, 480)) # resolusi window

        self.clock = pg.time.Clock() # setting frame per detik
        
        self.img = pg.image.load("D:\Codes\Python\dasar_pemrograman_python\proyek_pribadi\pygame_platformer_tutorial\data\images\clouds\cloud_1.png")

    def run(self):
        # perulangan tak terhingga untuk mengupdate tampilan window
        while True:
            
            # menutup window
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            
            pg.display.update()
            self.clock.tick(60) # frame per detik
   
Game().run()
         