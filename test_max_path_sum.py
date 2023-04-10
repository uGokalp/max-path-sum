from maxpath import MaxPathService
from models import TreeData


def test_1():
    data = {
        "tree": {
            "nodes": [
                {"id": "1", "left": "2", "right": "3", "value": 1},
                {"id": "3", "left": "6", "right": "7", "value": 3},
                {"id": "7", "left": None, "right": None, "value": 7},
                {"id": "6", "left": None, "right": None, "value": 6},
                {"id": "2", "left": "4", "right": "5", "value": 2},
                {"id": "5", "left": None, "right": None, "value": 5},
                {"id": "4", "left": None, "right": None, "value": 4},
            ],
            "root": "1",
        }
    }
    service = MaxPathService()
    tree_data = TreeData(**data)
    result = service.find_max_path_sum(tree_data)
    assert result == 18


def test_2():
    data = {
        "tree": {
            "nodes": [
                {"id": "1", "left": "2", "right": "3", "value": 1},
                {"id": "3", "left": None, "right": None, "value": 3},
                {"id": "2", "left": None, "right": None, "value": 2},
            ],
            "root": "1",
        }
    }
    service = MaxPathService()
    tree_data = TreeData(**data)
    result = service.find_max_path_sum(tree_data)
    assert result == 6


def test_3():
    data = {
        "tree": {
            "nodes": [
                {"id": "1", "left": "-10", "right": "-5", "value": 1},
                {"id": "-5", "left": "-20", "right": "-21", "value": -5},
                {"id": "-21", "left": "100-2", "right": "1-3", "value": -21},
                {"id": "1-3", "left": None, "right": None, "value": 1},
                {"id": "100-2", "left": None, "right": None, "value": 100},
                {"id": "-20", "left": "100", "right": "2", "value": -20},
                {"id": "2", "left": None, "right": None, "value": 2},
                {"id": "100", "left": None, "right": None, "value": 100},
                {"id": "-10", "left": "30", "right": "45", "value": -10},
                {"id": "45", "left": "3", "right": "-3", "value": 45},
                {"id": "-3", "left": None, "right": None, "value": -3},
                {"id": "3", "left": None, "right": None, "value": 3},
                {"id": "30", "left": "5", "right": "1-2", "value": 30},
                {"id": "1-2", "left": None, "right": None, "value": 1},
                {"id": "5", "left": None, "right": None, "value": 5},
            ],
            "root": "1",
        }
    }
    service = MaxPathService()
    tree_data = TreeData(**data)
    result = service.find_max_path_sum(tree_data)
    assert result == 154

