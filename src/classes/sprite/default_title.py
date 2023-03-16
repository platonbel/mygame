import pygame
import runtime

class Title(pygame.sprite.Sprite):
    
    def __init__(self, text=None, font_link='neo sans pro', font_size=36, color=(0, 0, 0), alpha=255, visible=True, shift_distance=(0, 0), shift_side=None, global_layer=0, layer=0):
        super().__init__()
        self.setup_edit(text, font_link, font_size, color, alpha, visible, shift_distance, shift_side, global_layer, layer)

    def update(self, position:list[int], shift_distance:list[int], shift_side:str):
        self.position_update(position, shift_distance, shift_side)

    def position_update(self, position:list[int], shift_distance:list[int], shift_side:str):
        if position and shift_distance:
            self.position_edit((position[0]+shift_distance[0], position[1]+shift_distance[1]), shift_side)

    def __del__(self):
        runtime.global_layers.items[self.global_layer].remove(self)
        self.exist = False

    def setup_edit(self, text:str, font_link:str, font_size:int, color:list[int], alpha:int, visible:bool, shift_distance:list[int], shift_side:str, global_layer:int, layer:int):
        self.image_edit(text, font_link, font_size, color)
        self.visible_edit(alpha, visible)
        self.shift_distance = shift_distance
        self.shift_side = shift_side
        self.layer_edit(global_layer, layer)
        self.exist = True

    def image_edit(self, text:str, font_link:str, font_size:int,color:list[int]):
        try:
            position = self.get_position()
        except:
            position = (0, 0)
        self.text = text
        self.font_link = font_link
        self.font_size = font_size
        self.color = color
        self.font = pygame.font.SysFont(self.font_link, self.font_size)
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()
        self.position_edit(position)

    def visible_edit(self, alpha:int, visible:bool):
        self.alpha = alpha
        self.visible = visible
        self.image.set_alpha(0 if not self.visible else self.alpha)

    def layer_edit(self, global_layer: int, layer: int):
        try:
            if runtime.global_layers.items[self.global_layer].has(self):
                runtime.global_layers.items[self.global_layer].remove(self)
        except:
            pass
        self.global_layer = global_layer
        self.layer = layer
        runtime.global_layers.items[self.global_layer].add(self, layer=self.layer)

    def position_edit(self, position:list[int]=None, side:str=None):
        if position:
            match side:
                case 'topleft':
                    self.rect.topleft = position
                case 'midtop':
                    self.rect.midtop = position
                case 'topright':
                    self.rect.topright = position
                case 'midright':
                    self.rect.midright = position
                case 'bottomright':
                    self.rect.bottomright = position
                case 'midbottom':
                    self.rect.midbottom = position
                case 'bottomleft':
                    self.rect.bottomleft = position
                case 'midleft':
                    self.rect.midleft = position
                case 'center':
                    self.rect.center = position
                case _:
                    self.rect.topleft = position

    def get_position(self, side:str=None):
        match side:
            case 'topleft':
                return self.rect.topleft
            case 'midtop':
                return self.rect.midtop
            case 'topright':
                return self.rect.topright
            case 'midright':
                return self.rect.midright
            case 'bottomright':
                return self.rect.bottomright
            case 'midbottom':
                return self.rect.midbottom
            case 'bottomleft':
                return self.rect.bottomleft
            case 'midleft':
                return self.rect.midleft
            case 'center':
                return self.rect.center
            case _:
                return self.rect.topleft