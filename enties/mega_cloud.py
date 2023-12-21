from enties.cloud import Cloud
from loguru import logger
from mega import Mega

from utils.time_utils import creation_date


class MegaCloud(Cloud):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.mega = Mega()

    def login(self):
        try:
            self.mega.login(self.username, self.password)
            logger.success("Logged in Mega cloud")
        except Exception as e:
            raise e

    def upload_dir(self, path):
        try:
            self.mega.create_folder(path)
            logger.success(f"Created dir {path}")
        except Exception as e:
            raise e

    def upload_file(self, path, cloud_dir_path):
        try:
            dir = self.find_dir(cloud_dir_path)
            if dir is None:
                return

            self.mega.upload(path, dir[0])
            logger.success(f"Created file {path}")
        except Exception as e:
            raise e

    def find_dir(self, path):
        try:
            dir = self.mega.find(path)

            if dir is None:
                logger.error(f"Didn't find dir {path}")
            else:
                logger.success(f"Find dir {path}")

            return dir
        except Exception as e:
            raise e

    def find_file(self, path):
        try:
            file = self.mega.find(path)

            if file is None:
                logger.error(f"Didn't find file {path}")
            else:
                logger.success(f"Find file {path}")

            return file
        except Exception as e:
            raise e

    def compare_files(self, path, cloud_file_path):
        try:
            cloud_file = self.find_file(cloud_file_path)

            if cloud_file is None:
                logger.error(f"Can't compare file {path} with {cloud_file_path}")
                return True

            file_modify = creation_date(path)
            logger.success(f"Compare file {path}:{file_modify} with cloud file {cloud_file_path}:{cloud_file[1]['ts']}")
            return file_modify > cloud_file[1]["ts"]
        except Exception as e:
            raise e

    def delete_file(self, path):
        try:
            file = self.mega.find_file(path)

            if file is None:
                logger.error(f"Can't delete file {path}")
                return

            self.mega.delete(file[0])
            logger.success(f"Deleted file {path}")
        except Exception as e:
            raise e

    def delete_dir(self, path):
        try:
            dir = self.find_dir(path)

            if dir is None:
                logger.error(f"Can't delete dir {path}")
                return

            self.mega.delete(dir[0])
            logger.success(f"Deleted dir {path}")
        except Exception as e:
            raise e
