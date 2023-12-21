from loguru import logger
from accounts_config import config
from enties.mega_cloud import MegaCloud


def main():
    mega = MegaCloud(config["Mega"]["username"], config["Mega"]["password"])
    try:
        mega.login()
    except Exception as e:
        logger.error(e)


if __name__ == "__main__":
    main()
