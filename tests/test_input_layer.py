from src.input_layer import parse_plateau

def test_parse_plateau():
    assert parse_plateau("5 5") == {"max_x": 5, "max_y": 5}

def test_parse_plateau_with_large_plateau():
    assert parse_plateau("10 10") == {"max_x": 10, "max_y": 10}

def test_parse_plateau_with_non_square_plateau(): 
    assert parse_plateau("5 10") == {"max_x": 5, "max_y": 10}