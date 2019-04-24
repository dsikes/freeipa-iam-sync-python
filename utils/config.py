import yaml

def get_config():
    with open('config.yaml') as config:
        return yaml.load(config)
