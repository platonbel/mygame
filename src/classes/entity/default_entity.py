import math
import scripts
import runtime

class Entity():
    
    def __init__(self):
        runtime.objects.items["entity"].add(self)

        self.object_name = None
        self.health_point_value = None
        self.max_health_point_value = None
        self.stamina_point_value = None
        self.max_stamina_point_value = None
        self.constant_velocity_value = None
        self.dynamic_velocity_value = None

        self.sprite_block_link = None

        self.inventory_link = None #inventory

        self.config_path = None
        self.config_path_last_update_time = None

        self.exist = True

    def update(self, dtime, TARGET_FPS):
        self.setup_update()

        self.exist_check()
        self.characteristics_update()
        self.movement()

    def setup_update(self):
        if scripts.file_processing.file_check_update(self.config_path, self.config_path_last_update_time):
            self.setup_edit(self.config_path)

    def __del__(self):
        runtime.objects.items['entity'].remove(self)
        self.sprite_block_link.__del__()
        #self.inventory.dropitems
        self.exist = False

    def setup_edit(self, config_path):
        self.config_path = config_path if scripts.file_processing.file_check_existence(config_path) else "src/assets/configs/entity/default_entity.json"
        self.config_path_last_update_time = scripts.file_processing.file_get_update_time(self.config_path)
        config = scripts.config_unpack.config_unpack(self.config_path)
        self.object_name = config["items"]["object_name"]
        self.health_point_value = config["items"]["max_health_point_value"]
        self.max_health_point_value = config["items"]["max_health_point_value"]
        self.stamina_point_value = config["items"]["max_stamina_point_value"]
        self.max_stamina_point_value = config["items"]["max_stamina_point_value"]
        self.constant_velocity_value = config["items"]["constant_velocity_value"]
        self.dynamic_velocity_value = config["items"]["constant_velocity_value"]
        self.sprite_block_link = scripts.sprite_block_create.sprite_block_create(config["items"]["sprite_block_config_link"])

    def exist_check(self):
        if self.health_point_value <= 0:
            self.__del__()

    def movement(self):
        None

    def characteristics_update(self):
        if self.health_point_value > self.max_health_point_value:
            self.health_point_value = self.max_health_point_value

        if self.stamina_point_value <= 0:
            self.stamina_point_value = 0
        elif self.stamina_point_value > self.max_stamina_point_value:
            self.stamina_point_value = self.max_stamina_point_value

