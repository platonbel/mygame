
import pygame
import runtime, scripts, assets, classes
import math, random

def main():

    #init the main vars and places
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 900

    FPS = 60
    TARGET_FPS = 60

    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Beliakov Platon")
    
    running = True  

    player_ = scripts.entity_create.entity_create("player", "src/assets/configs/entity/player_entity/juggernaut_player_entity.json")
    test_func_last_file_update = scripts.file_processing.file_get_update_time("src/command_file.json")

    while running:

        for event in pygame.event.get():
            keyValues = pygame.key.get_pressed() 
            mouseValues = pygame.mouse.get_pressed()
            mousePosition = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if keyValues[pygame.K_ESCAPE]:
                    paused = not paused

        clock.tick(FPS)
        dtime = 1/FPS  
        screen.fill((255, 255, 255))

        scripts.file_processing.test_func("src/command_file.json", test_func_last_file_update, player_.sprite_block_link)
        test_func_last_file_update = scripts.file_processing.file_get_update_time("src/command_file.json")

        runtime.objects.items['sprite_block'].update()
        runtime.objects.items['entity'].update(dtime, TARGET_FPS)
        runtime.objects.items['secondary_GUI'].update()
        runtime.objects.items['general_GUI'].update()

        tuple(map(lambda global_layer: global_layer.draw(screen), runtime.global_layers.items.values()))

        pygame.display.update()

    pygame.quit()

main()