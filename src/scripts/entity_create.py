import scripts
from classes import entity

#create entity from .json entity configs
def entity_create(entity_type, config_path):
    match entity_type:
        case "default":
            entity_link = entity.default_entity.Entity()
        case "player":
            entity_link = entity.player_entity.Player_Entity()
        case "zombie":
            entity_link = entity.zombie_entity.Zombie_Entity()
    entity_link.setup_edit(config_path)
    secondary_GUI_link = scripts.secondary_GUI_create.secondary_GUI_create(entity_link, "src/assets/configs/secondary_GUI/entity_statistics_indicator_secondary_GUI.json")
    return entity_link