import pygame
from scripts.entities import PhysicsEntity
from scripts.tilemap import Tilemap
from scripts.utils import load_image, load_images
import sys

class Game:
  
    def __init__(self) -> None:

        pygame.init()
        pygame.display.set_caption('Ninja game')
        
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240)) #i am creating surface to render on this scale and than transform it to to
        #the screen scale so i get the pixel effect and images for example gets bigger
        self.clock = pygame.time.Clock()
        
        self.movement = [False, False]
        
        self.assets = {
            'decor' : load_images('tiles/decor'),
            'grass' : load_images('tiles/grass'),
            'large_decor' : load_images('tiles/large_decor'),
            'stone' : load_images('tiles/stone'),
            'player' : load_image('entities/player.png')
        }

        print(self.assets)

        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))

        self.tilemap = Tilemap(self, tile_size=16)
        

    def run(self):
        while True:
            self.display.fill((14, 219, 248))
            
            self.tilemap.render(self.display)

            self.player.update(self.tilemap, (self.movement[1]-self.movement[0], 0))
            self.player.render(self.display)
                                                      
   
                 
            
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_UP:
                        self.player.velocity[1] = -3

                          
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False 

                          
                   
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))#now i am bliting the display on the screen for to see it after this i have to 
            #transform it to screen size(inside this line)
            pygame.display.update()
            self.clock.tick(60)


Game().run()                