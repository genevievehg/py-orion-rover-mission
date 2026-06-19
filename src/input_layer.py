def parse_plateau(plateau_size):
    max_x = plateau_size.split(' ')[0]
    max_y = plateau_size.split(' ')[1]
    return {"max_x": int(max_x), "max_y": int(max_y)}