import os
import sys


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Директория не задана.')
    dir_to_check = os.getcwd() if sys.argv[1] == '.' else sys.argv[1]
    list_of_files = os.listdir(dir_to_check)
    import pdb; pdb.set_trace()
