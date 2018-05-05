import sys, os


def walk_through_tree(directories_and_files_tree):
    files_index = 2
    path_index = 0
    files = {}
    for full_path, _, names_of_files in directories_and_files_tree:

        # full_path = directory[path_index]
        # for file_name in directory[files_index]:

            # if file_name not in files:
            #     files[file_name] = [full_path]
            # else:
            #     files[file_name].append(full_path)
    return files


def process_directories_info(files):
    for key, value in files.items():
        if len(value) < 2:
            continue
        print('File {} founded in next directories: '.format(key))
        for value_element in value:
            print('\t{}'.format(value_element))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Initial directory is not specified')
    if not os.path.isdir(sys.argv[1]):
        sys.exit('Specified argument is not a directory')
    files = walk_through_tree(os.walk(sys.argv[1]))
    process_directories_info(files)
    print('Duplicated files checking was successfully finished.')
