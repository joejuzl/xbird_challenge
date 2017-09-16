import yaml
from orator import DatabaseManager


def get_connection():
    with open('db/orator.yml', 'r') as config:
        db_config = yaml.load(config)

    return DatabaseManager(db_config['databases'])
