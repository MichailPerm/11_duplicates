import sys, os
from collections import defaultdict


def get_file_size(file_name, full_path):
    full_name = full_path + '/' + file_name
    return os.stat(full_name).st_size


def get_files_locations(root_dir):
    names_of_files = defaultdict(list)
    for dir_name, _, file_names in os.walk(root_dir):
        full_path = dir_name
        for file_name in file_names:
            file_size = get_file_size(file_name, full_path)
            names_of_files[(file_name, file_size, )].append(full_path)
    return names_of_files


def print_duplicated_files_paths(names_of_files):
    for file_name, file_paths in names_of_files.items():
        if len(file_paths) >= 2:
            print('File {} founded in next directories: '.format(file_name))
            for file_path in file_paths:
                print('\t{}'.format(file_path))


def get_root_path(root_path_index=1):
    return sys.argv[root_path_index]


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Initial directory is not specified')
    root_path = get_root_path()
    if not os.path.isdir(root_path):
        sys.exit('Specified argument is not a directory')
    names_of_files = get_files_locations(root_path)
    print_duplicated_files_paths(names_of_files)
    print('Duplicated files checking was successfully finished.')
