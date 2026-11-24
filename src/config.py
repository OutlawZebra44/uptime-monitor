import yaml 


def load_config(path: str = "config.yaml") -> dict:
    """Loads the configuration from a YAML file."""
    with open(path, "r") as file:
        return yaml.safe_load(file)