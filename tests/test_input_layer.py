from src.input_layer import parse_plateau, parse_position

def test_parse_plateau():
    assert parse_plateau("5 5") == {"max_x": 5, "max_y": 5}

def test_parse_plateau_with_large_plateau():
    assert parse_plateau("10 10") == {"max_x": 10, "max_y": 10}

def test_parse_plateau_with_non_square_plateau(): 
    assert parse_plateau("5 10") == {"max_x": 5, "max_y": 10}

def test_parse_position():
    assert parse_position("1 2 N") == {"x": 1, "y": 2, "direction": "N"}

def test_parse_position_with_east_heading_and_different_coordinates():
    assert parse_position("4 8 E") == {"x": 4, "y": 8, "direction": "E"}

def test_parse_position_with_south_heading_and_different_coordinates():
    assert parse_position("3 7 S") == {"x": 3, "y": 7, "direction": "S"}


def test_parse_position_with_west_heading_and_different_coordinates():
    assert parse_position("2 6 W") == {"x": 2, "y": 6, "direction": "W"}