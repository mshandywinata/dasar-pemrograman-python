import os 
import pygame as pg

BASE_IMG_PATH = 'D:/Codes/Python/dasar-pemrograman-python/proyek/proyek_pribadi/pygame_platformer_tutorial/data/images/'

def load_image(path):
    img = pg.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img

def load_images(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(load_image(path + '/'+ img_name))
    return images