import os

import scripts

def file_check_existence(file_path):
    return os.path.isfile(file_path)

def file_get_update_time(file_path):
    return os.path.getmtime(file_path)

def file_check_update(file_path, prev_file_update_time):
    if file_check_existence(file_path):
        try:
            current_file_update_time = file_get_update_time(file_path)
            if current_file_update_time != prev_file_update_time:
                return True
            else:
                return False
        except:
            return False
    else: 
        return False
    
def test_func(command_file_path, command_file_last_update_time, sprite_block):
    if file_check_update(command_file_path, command_file_last_update_time):
        command_file = scripts.config_unpack.config_unpack(command_file_path)
        if command_file["action"] == "position_edit":
            sprite_block.position_edit(command_file["position"], command_file["side"])
        if command_file["action"] == "position_update":
            sprite_block.position_update(command_file["position"], command_file["shift_distance"], command_file["shift_side"])
        

