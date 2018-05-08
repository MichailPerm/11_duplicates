import sys, os
from collections import defaultdict


def process_files_and_paths(root_dir):
    names_of_files = defaultdict(list)
    for dir_name, _, file_names in os.walk(root_dir):
        full_path = dir_name
        for file_name in file_names:
            names_of_files[file_name].append(full_path)
    return names_of_files



def print_duplicated_files_paths(names_of_files):
    for file_name, file_paths in names_of_files.items():
        if len(file_paths) < 2:
            continue
        print('File {} founded in next directories: '.format(file_name))
        for file_path in file_paths:
            print('\t{}'.format(file_path))


if __name__ == '__main__':
    rootdir_path_indes = 1
    if len(sys.argv) < 2:
        sys.exit('Initial directory is not specified')
    if not os.path.isdir(sys.argv[rootdir_path_indes]):
        sys.exit('Specified argument is not a directory')
    names_of_files = process_files_and_paths(sys.argv[rootdir_path_indes])
    print_duplicated_files_paths(names_of_files)
    print('Duplicated files checking was successfully finished.')
