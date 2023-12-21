import yaml

with open("accounts_config.yml", "rt") as f:
    config = yaml.safe_load(f.read())
