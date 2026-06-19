def parse_plateau(plateau_size):
    max_x = plateau_size.split(' ')[0]
    max_y = plateau_size.split(' ')[1]
    return {"max_x": int(max_x), "max_y": int(max_y)}

def parse_position(position_string):
    x_position = position_string.split(' ')[0]
    y_position = position_string.split(' ')[1]
    direction = position_string.split(' ')[2]
    return {"x": int(x_position), "y": int(y_position), "direction": direction}

def parse_instructions(instruction_string):
    return list(instruction_string)