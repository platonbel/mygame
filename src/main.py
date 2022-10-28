
import pygame
import modules
from modules.mymodules import bulletSpawn


def main():

    WIDTH = 1080
    HEIGHT = 720
    FPS = 60
    TARGET_FPS = 60
    
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()

    mouse = (0, 0)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Beliakov Platon")

    entitygroup = pygame.sprite.Group()
    entitygroup_zombie = pygame.sprite.Group()
    entitygroup_player = pygame.sprite.Group()
    textentitygroup = pygame.sprite.Group()

    player1 = modules.myentity.Player((0, 200, 255), (WIDTH, HEIGHT), name='Player', entitygroup=entitygroup, selfentitygroup=entitygroup_player, selfenemygroup=entitygroup_zombie)
    pause = modules.myentity.Text('PAUSE', 72, alone = True, position=(WIDTH/2, HEIGHT/2))
    
    entitygroup.add(modules.myentity.Entity._instances)
    entitygroup_zombie.add(modules.myentity.Zombie._instances)
    entitygroup_player.add(modules.myentity.Player._instances)
    textentitygroup.add(modules.myentity.Text._instances)

    clock = pygame.time.Clock()

    running = True
    paused = True
    while running:
        clock.tick(FPS)
        dtime = 1/FPS
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            keystate = pygame.key.get_pressed()
            mousestate = pygame.mouse.get_pressed()
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                mouse = event.pos  
            if event.type == pygame.KEYDOWN:
                if keystate[pygame.K_ESCAPE]:
                    paused = not paused

        if entitygroup_zombie.sprites() == []:
            modules.mymodules.zombieSpawn(entitygroup_zombie, entitygroup_player, textentitygroup, entitygroup)


        entitygroup.update(screen, mouse, mousestate, keystate, entitygroup, dtime, TARGET_FPS)
        textentitygroup.update()

        entitygroup.draw(screen)
        textentitygroup.draw(screen)
        modules.mymodules.cursor(screen, mouse)

        while paused:
            screen.blit(pause.image, pause.rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    paused = False
                if event.type == pygame.KEYDOWN:
                    keystate = pygame.key.get_pressed()
                    if keystate[pygame.K_ESCAPE]:
                        paused = not paused
            pygame.display.flip()
        
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
