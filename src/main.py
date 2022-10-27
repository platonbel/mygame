
import pygame
import modules


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
    entitygroup_mob = pygame.sprite.Group()
    textentitygroup = pygame.sprite.Group()

    player1 = modules.mysprites.Player((0, 200, 255), (WIDTH, HEIGHT), [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d], name='Player', entitygroup=entitygroup, selfentitygroup=entitygroup_player)
    zombie1 = modules.mysprites.Zombie(name='Zombie', target=player1, entitygroup=entitygroup, selfentitygroup=entitygroup_zombie)
    pause = modules.mysprites.Text('PAUSE', 72, alone = True, position=(WIDTH/2, HEIGHT/2))
    
    entitygroup.add(modules.mysprites.Entity._instances)
    entitygroup_zombie.add(modules.mysprites.Zombie._instances)
    entitygroup_player.add(modules.mysprites.Player._instances)
    textentitygroup.add(modules.mysprites.Text._instances)

    clock = pygame.time.Clock()

    running = True
    paused = True
    while running:
        clock.tick(FPS)
        dtime = 1/FPS
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                mouse = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousestat = pygame.mouse.get_pressed()
                if mousestat[0]:
                    entitygroup.add(modules.mysprites.Bullet(vector=mouse, player=player1, entitygroup=entitygroup, selfentitygroup=entitygroup))
            if event.type == pygame.KEYDOWN:
                keystate = pygame.key.get_pressed()
                if keystate[pygame.K_ESCAPE]:
                    paused = not paused

        if entitygroup_zombie.sprites() == []:
            newzombie = modules.mymodules.zombieSpawn(entitygroup_zombie, entitygroup_player, textentitygroup, entitygroup)

        entitygroup.update(entitygroup_zombie, screen, mouse, dtime, TARGET_FPS)
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
