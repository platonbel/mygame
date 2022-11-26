
import pygame
import modules
import math, random

def main():

    #init the main vars and places
    SCREEN_WIDTH = 1920
    SCREEN_HEIGHT = 1080

    BORDERS_WIDTH = 3072
    BORDERS_HEIGHT = 3072

    FPS = 60
    TARGET_FPS = 60

    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    borders = (BORDERS_WIDTH, BORDERS_HEIGHT)
    clock = pygame.time.Clock()
    interface = modules.interfaceClass.defaultInterface.Interface(screen)
    background = modules.backgroundClass.defaultBackground.Background(screen)
    pygame.display.set_caption("Beliakov Platon")
    
    running = True  
    paused = False
    fpsrender = modules.textClass.defaultText.Text(position=(200, 200))
    player = modules.entityClass.playerEntity.Player(name='Player')
    zombie = modules.entityClass.zombieEntity.Zombie(name='Zombie')

    #for i in range(1000):
    #    modules.shapeClass.defaultShape.Shape(position=(random.randint(0, 1920), random.randint(0, 1080)),image="src/assets/textures/ak-47_icon.png")

    while running:

        for event in pygame.event.get():
            keystate = pygame.key.get_pressed()
            mousestate = pygame.mouse.get_pressed()
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if keystate[pygame.K_ESCAPE]:
                    paused = not paused

        clock.tick(FPS)
        dtime = 1/FPS  
        screen.fill((255, 255, 255))
        fpsrender.textedit(str(clock), (0, 0, 0))

        interface.update(screen, mouse, mousestate, keystate, paused, player)
        background.update(screen)
        if not paused:
            modules.entityClass.instances.entityGroup.playerGroup.update(mouse, mousestate, keystate, screen, dtime, TARGET_FPS)
            modules.entityClass.instances.entityGroup.zombieGroup.update(screen, dtime, TARGET_FPS)
            modules.entityClass.instances.entityGroup.bulletGroup.update(dtime, TARGET_FPS)

        fpsrender.moving(fpsrender.position)
        modules.backgroundClass.instances.backgroundLayer.defaultLayer.draw(screen)
        modules.entityClass.instances.entityLayer.defaultLayer.draw(screen)
        modules.shapeClass.instances.shapeLayer.defaultLayer.draw(screen)
        modules.textClass.instances.textLayer.defaultLayer.draw(screen)
        modules.interfaceClass.instances.interfaceLayer.defaultLayer.draw(screen)

        pygame.display.update()

    pygame.quit()

main()