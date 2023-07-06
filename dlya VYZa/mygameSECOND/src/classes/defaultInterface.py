from classes import entity

class Interface():
    def __init__(self):
        self.player: entity.player_entity.Player_Entity = None
        
    def update(self, keyValues, mouseValues, mousePosition):
        None