from abc import ABC, abstractmethod


class Cloud(ABC):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def upload_dir(self, path):
        pass

    @abstractmethod
    def upload_file(self, path, cloud_dir_path):
        pass

    @abstractmethod
    def find_dir(self, path):
        pass

    @abstractmethod
    def find_file(self, path):
        pass

    @abstractmethod
    def compare_files(self, path, cloud_file_path):
        pass

    @abstractmethod
    def delete_file(self, path):
        pass

    @abstractmethod
    def delete_dir(self, path):
        pass
