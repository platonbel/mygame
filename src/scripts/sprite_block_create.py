from classes import sprite

#create sprite_contaiuner from sprite configs
def sprite_block_create(config_path):
    sprite_block_link = sprite.default_sprite_block.Sprite_Block()
    sprite_block_link.setup_edit(config_path)
    return sprite_block_link