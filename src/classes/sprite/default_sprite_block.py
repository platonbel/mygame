from classes import sprite
import scripts
import runtime

class Sprite_Block():

    def __init__(self):
        runtime.objects.items['sprite_block'].add(self)

        self.hitbox = None
        self.bitmap_image_group = dict()
        self.title_group = dict()

        self.config_path = None
        self.config_path_last_update_time = None

        self.exist = True

    def update(self):

        self.setup_update()

        self.hitbox.update()

        tuple(map(lambda object_: object_.update(
            position=self.hitbox.get_position(side=object_.shift_side),
            shift_distance=object_.shift_distance,
            shift_side=object_.shift_side
            ), self.bitmap_image_group.values()))
        
        tuple(map(lambda object_: object_.update(
            position=self.hitbox.get_position(side=object_.shift_side),
            shift_distance=object_.shift_distance,
            shift_side=object_.shift_side
            ), self.title_group.values()))

    def setup_update(self):
        if scripts.file_processing.file_check_update(self.config_path, self.config_path_last_update_time):
            self.sprite_block_clear()
            self.setup_edit(self.config_path)

    def __del__(self):
        runtime.objects.items['sprite_block'].remove(self)
        self.hitbox.__del__()
        tuple(map(lambda object_: object_.__del__(), self.bitmap_image_group))
        tuple(map(lambda object_: object_.__del__(), self.title_group))
        self.exist = False

    def setup_edit(self, config_path):
        self.config_path = config_path if scripts.file_processing.file_check_existence(config_path) else "src/assets/configs/sprite_block/error.json"
        self.config_path_last_update_time = scripts.file_processing.file_get_update_time(self.config_path)
        config = scripts.config_unpack.config_unpack(self.config_path)
        for key0, value0 in config.items():
            if key0 == "hitBox":
                self.hitbox_create(*value0.values())
            if key0 == "bitmap_image_group":
                for key1, value1 in value0.items():
                    self.bitmap_image_create(str(key1), value1.values())
            if key0 == "title_group":
                for key1, value1 in value0.items():
                    self.title_create(str(key1), value1.values())

    def hitbox_create(self, *args):
        self.hitbox = sprite.default_hitbox.Hitbox(*args)
    
    def bitmap_image_create(self, key, values):
        self.bitmap_image_group[key] = sprite.default_bitmap_image.Bitmap_Image(*values)

    def title_create(self, key, values):
        self.title_group[key] = sprite.default_title.Title(*values)

    def sprite_block_clear(self):
        self.hitbox.__del__()
        tuple(map(lambda key: self.bitmap_image_group[key].__del__(), self.bitmap_image_group.keys()))
        tuple(map(lambda key: self.title_group[key].__del__(), self.title_group.keys()))
        self.hitbox = None
        self.bitmap_image_group = dict()
        self.title_group = dict()

    def position_edit(self, position:list[int], side:str):
        self.hitbox.position_edit(position, side)

    def position_update(self, position:list[int], shift_distance:list[int], shift_side:str):
        self.position_edit((position[0]+shift_distance[0], position[1]+shift_distance[1]), shift_side) 