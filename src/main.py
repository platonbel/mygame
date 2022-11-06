
import pygame
import modules

def main():

    #init the main vars and places
    WIDTH = 1920
    HEIGHT = 1080
    FPS = 60
    TARGET_FPS = 60

    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    interface = modules.interfaceClass.defaultInterface.Interface(screen)
    pygame.display.set_caption("Beliakov Platon")
    
    running = True
    paused = False

    player = modules.entityClass.playerEntity.Player(name='Player')
    zombie = modules.entityClass.zombieEntity.Zombie(name='Zombie')

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

        interface.update(mouse, mousestate, keystate, paused, player)
        if not paused:
            modules.entityClass.instances.entityGroup.playerGroup.update(mouse, mousestate, keystate, screen, dtime, TARGET_FPS)
            modules.entityClass.instances.entityGroup.zombieGroup.update(player, screen, dtime, TARGET_FPS)
            modules.entityClass.instances.entityGroup.bulletGroup.update(dtime, TARGET_FPS)
        modules.shapeClass.instances.shapeGroup.defaultGroup.update()
        modules.textClass.instances.textGroup.defaultGroup.update()

        modules.entityClass.instances.entityLayer.defaultLayer.draw(screen)
        modules.shapeClass.instances.shapeLayer.defaultLayer.draw(screen)
        modules.textClass.instances.textLayer.defaultLayer.draw(screen)
        modules.interfaceClass.instances.interfaceLayer.defaultLayer.draw(screen)

        pygame.display.update()

    pygame.quit()

main()