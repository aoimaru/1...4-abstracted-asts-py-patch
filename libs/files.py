import glob
from abc import ABCMeta, abstractmethod

class File(object):
    @staticmethod
    def get_file_ids(root_file_path: str):
        return glob.glob(root_file_path, recursive=True)



def main():
    ROOT_FILE_PATH = "../fluentd/**"
    file_paths = File.get_file_ids(ROOT_FILE_PATH)
    for file_path in file_paths:
        print(file_path)


if __name__ == "__main__":
    main()


