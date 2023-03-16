from classes import entity

class Player_Entity(entity.default_entity.Entity):

    def __init__(self):
        super().__init__()

        self.key_values = {'K_LSHIFT': False, 'K_0': False, 'K_1': False, 'K_2': False, 'K_3': False, 'K_w': False, 'K_a': False, 'K_s': False, 'K_d': False}

