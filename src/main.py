
import pygame
import modules

def main():

    #init the main vars and places
    WIDTH = 1080
    HEIGHT = 720
    FPS = 60
    TARGET_FPS = 60

    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    cursor = modules.gameentity.cursorentity.Cursor()
    interface = modules.classmodules.Interface(screen)
    pygame.display.set_caption("Beliakov Platon")
    
    running = True
    paused = False

    player = modules.gameentity.playerentity.Player(name='Player')
    zombie = modules.gameentity.zombieentity.Zombie(name='Zombie')

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

        interface.update(screen, paused, player)
        modules.gameentity.entitygroup.cursorgroup.update(mouse)

        if not paused:
            modules.gameentity.entitygroup.playergroup.update(mouse, mousestate, keystate, screen, dtime, TARGET_FPS)
            modules.gameentity.entitygroup.zombiegroup.update(player, screen, dtime, TARGET_FPS)
            modules.gameentity.entitygroup.bulletgroup.update(dtime, TARGET_FPS)
        
        modules.gameshape.shapegroup.defaultgroup.update()
        modules.gametext.textgroup.defaultgroup.update()

        modules.gameentity.entitylayer.defaultlayer.draw(screen)
        modules.gameshape.shapelayer.defaultlayer.draw(screen)
        modules.gametext.textlayer.defaultlayer.draw(screen)
        modules.gameentity.entitylayer.cursorlayer.draw(screen)

        modules.privategameobject.privateobjectlayer.interfacelayer.draw(screen)

        pygame.display.update()

    pygame.quit()

main()