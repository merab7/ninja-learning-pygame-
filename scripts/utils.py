import pygame

BASE_IMAGE_PATH = 'data/images/'

def load_images(path):
    img = pygame.image.load(BASE_IMAGE_PATH + path).convert()#convert is the internal modification in 
    #pygame it makes the image more efficient for render it is very important to do that
    img.set_colorkey((0, 0, 0))
    return img 