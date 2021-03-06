import os
import json
import argparse


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def pretty_print_json(dictionary):
    print(json.dumps(dictionary, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', type=str)
    arguments = parser.parse_args()

    if os.path.exists(arguments.filepath):
        json_data = load_data(arguments.filepath)
        pretty_print_json(json_data)
    else:
        print('No such file or directory: \'{}\''.format(arguments.filepath))
