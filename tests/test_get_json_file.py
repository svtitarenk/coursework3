from src.functions import get_json_file
import os
from config import ROOT_DIR

file_path = os.path.join(ROOT_DIR, 'data', 'operations.json')


def test_is_file_exists():
    assert os.path.exists(file_path) is True


def test_is_date_filtered_lines():
    assert isinstance(get_json_file(file_path), list)
