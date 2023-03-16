import scripts
from classes import secondary_GUI
#create entity from .json entity configs
def secondary_GUI_create(entity_link, config_path):
    secondary_GUI_link = secondary_GUI.entity_statistics_indicator_secondary_GUI.Entity_Statistics_Indicator_Secondary_GUI()
    secondary_GUI_link.setup_edit(entity_link, config_path)
    return secondary_GUI_link