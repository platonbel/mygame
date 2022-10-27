import pygame
import math
import random
    
class Entity(pygame.sprite.Sprite): # class
    _instances = set()
    def __init__(self, color, resolution, keys): # init
        Entity._instances.add(self)
        super().__init__()
        self.resolution = resolution
        self.image = pygame.Surface((40, 40))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.resolution[0] / 2 + random.randint(1, 256), self.resolution[1] / 2 + random.randint(1, 256))
        self.health = 100
        self.maxhealth = 100
    
    def healthbar(self, screen): #healthbar (problem here)
        if self.maxhealth == math.inf: #if health is infinit -> healthration(1 = 100%) = 1
            healthratio = 1
        else: # else: take a proportion of health and maxhealth
            healthratio = self.health / self.maxhealth 
        bar_lenght = 100 
        bar_height = 10

        bar_image = pygame.Surface((bar_lenght*healthratio, bar_height)) #creating image of healthbar
        bar_image.fill((75, 255, 75))
        bar_image_rect = bar_image.get_rect()
        bar_image_rect.center = (self.rect.center[0], self.rect.center[1]+30)

        screen.blit(bar_image, bar_image_rect)

    def update(self, screen): #update func
        self.healthbar(screen)
    
def main():
    WIDTH = 1080
    HEIGHT = 720
    FPS = 60
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("sss")
    all_entity = pygame.sprite.Group()
    player1 = Entity((0, 200, 255), (WIDTH, HEIGHT), [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d])
    all_entity.add(Entity._instances)
    clock = pygame.time.Clock()
    running = True


    while running: #main loop
        clock.tick(FPS)
        dtime = 1/FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        all_entity.update(screen)
        screen.fill((255, 255, 255))
        bar_image = pygame.Surface((100, 100)) #creating image of healthbar
        bar_image.fill((0, 0, 255))
        bar_image_rect = bar_image.get_rect()
        bar_image_rect.center = player1.rect.center
        screen.blit(bar_image, bar_image_rect)
        all_entity.draw(screen)
        pygame.display.update()
    pygame.quit()
main()

