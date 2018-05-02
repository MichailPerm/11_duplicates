import sys, os


def walk_through_files_in_dirs(dirs_and_files_list):
    first_list_element_index = 0
    files_list_index = 2
    dir_index = 0
    if not dirs_and_files_list:
        return
    files_in_dir = dirs_and_files_list.pop(
        first_list_element_index)[files_list_index]
    for dir in dirs_and_files_list:
        files = list(set(files_in_dir) & set(dir[files_list_index]))
        if not files:
            continue
        print("Duplicated files {} founded in {} directory".format(files, dir[dir_index]))
    walk_through_files_in_dirs(dirs_and_files_list)


if __name__ == '__main__':
    if sys.argv.__len__() < 2:
        sys.exit("Initial directory is not specified")
    if not os.path.exists(sys.argv[1]):
        sys.exit("Specified directory is not exists")
    directories_info = os.walk(sys.argv[1])
    dirs_and_files_list = []
    for directory_info in directories_info:
        dirs_and_files_list.append(directory_info)
    walk_through_files_in_dirs(dirs_and_files_list)
    print("Duplicated files checkind was succesfully finished.")


