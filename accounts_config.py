import yaml

def load_config():
    with open("accounts_config.yml", "rt") as f:
        return yaml.safe_load(f.read())


config = load_config()
