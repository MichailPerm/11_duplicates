import sys, os

# TODO Сделать поиск по спискам файлов. Формировать словарь, где имя файла - ключ,
# а путь к файлу - это список директорий. И тогда выводить, какие именно файлы
# обнаружены в нескольких директориях

def walk_through_tree(directories_and_files_tree):
    files_index = 2
    directory_index = 1
    path_index = 0
    files_dict = {}
    for directory_info in directories_and_files_tree:
        full_path = '{}'.format(directory_info[path_index])
        for file_name in directory_info[files_index]:
            if file_name not in files_dict:
                files_dict[file_name] = [full_path]
            else:
                files_dict[file_name].append(full_path)
    return files_dict


def process_directories_info(directories_info):
    for key, value in directories_info:
        if len(value) < 2:
            continue
        print("File {} founded in next directories: ".format(key))
        for value_element in value:
            print('\t{}'.format(value_element))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Initial directory is not specified')
    if not os.path.isdir(sys.argv[1]):
        sys.exit('Specified argument is not a directory')
    directories_info = walk_through_tree(os.walk(sys.argv[1]))
    process_directories_info(directories_info)
    print('Duplicated files checking was successfully finished.')
