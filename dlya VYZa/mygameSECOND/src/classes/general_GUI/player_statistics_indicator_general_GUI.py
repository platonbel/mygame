import scripts
import runtime

class Player_Statistics_Indicator():
    def __init__(self, player_link, screen_link):
        runtime.objects.items['general_GUI'].add(self)

        self.sprite_link = scripts.sprite_block_create.sprite_create("src/configs/sprites/player_statistics_indicator_general_GUI.json")

        self.player_link = player_link
        self.screen_link = screen_link

        self.exist = True

    def update(self):
        self.movement()
        self.sprite_update()

    def __del__(self):
        runtime.objects.items['general_GUI'].remove(self)
        self.sprite_link.__del__()
        self.exist = False

    def check_exist(self):
        if self.player_link.exist == False:
            self.__del__()

    def movement(self):
        self.sprite_link.hitBox.position_update(
            position=self.screen_link.get_size(),
            distance=(-30, -30),
            side='bottomright'
        )
    
    def sprite_update(self):
        self.sprite_link.shape_group['health_point_bar'].size_edit((int(272*self.player_link.health_point_value/self.player_link.max_health_point_value), 24))
        self.sprite_link.shape_group['stamina_point_bar'].size_edit((int(272*self.player_link.stamina_point_value/self.player_link.max_stamina_point_value), 24))
        self.sprite_link.title_group['health_point_ratio'].text_edit(f'{str(int(self.player_link.health_point_value/self.player_link.max_health_point_value)*100)}%')
        self.sprite_link.title_group['stamina_point_ratio'].text_edit(f'{str(int(self.player_link.stamina_point_value/self.player_link.max_stamina_point_value)*100)}%')
    