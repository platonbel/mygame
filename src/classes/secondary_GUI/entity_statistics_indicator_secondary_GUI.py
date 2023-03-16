import scripts
import runtime

class Entity_Statistics_Indicator_Secondary_GUI():
    def __init__(self):
        runtime.objects.items['secondary_GUI'].add(self)

        self.sprite_block_link = None

        self.entity_link = None

        self.config_path = None
        self.config_path_last_update_time = None

        self.exist = True

    def update(self):
        self.setup_update()

        self.exist_check()
        self.movement()

    def setup_update(self):
        if scripts.file_processing.file_check_update(self.config_path, self.config_path_last_update_time):
            self.setup_edit(self.entity_link, self.config_path)

    def __del__(self):
        runtime.objects.items['secondary_GUI'].remove(self)
        self.sprite_block_link.__del__()
        self.exist = False

    def setup_edit(self, entity_link, config_path):
        self.config_path = config_path
        self.config_path_last_update_time = scripts.file_processing.file_get_update_time(self.config_path)
        config = scripts.config_unpack.config_unpack(self.config_path)
        self.entity_link = entity_link
        self.sprite_block_link = scripts.sprite_block_create.sprite_block_create(config["items"]["sprite_block_config_link"])

    def exist_check(self):
        if self.entity_link.exist == False:
            self.__del__()

    def movement(self):
        self.sprite_block_link.hitbox.position_update(
            position=self.entity_link.sprite_block_link.hitbox.get_position(side='center'),
            shift_distance=(0, -80),
            shift_side='center'
        )
    