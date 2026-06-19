from src.input_layer import parse_plateau

def test_parse_plateau():
    result = parse_plateau("5 5")
    assert result == {"max_x": 5, "max_y": 5}

def test_parse_plateau_with_large_plateau():
    result = parse_plateau("10 10")
    assert result == {"max_x": 10, "max_y": 10}

def test_parse_plateau_with_non_square_plateau():
    result = parse_plateau("5 10")
    assert result == {"max_x": 5, "max_y": 10}