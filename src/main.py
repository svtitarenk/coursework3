from functions import (get_json_file,
                       filtered_lines,
                       sorted_datetime_toprows,
                       result_transactions)
import os
from config import ROOT_DIR

file_path = os.path.join(ROOT_DIR, 'data', 'operations.json')


def main():
    content_to_filter = get_json_file(file_path)
    filtered_array = filtered_lines(content_to_filter)
    filtered_top5rows = sorted_datetime_toprows(filtered_array, 5)
    row_ = result_transactions(filtered_top5rows)
    print(row_)


main()
