# sample.py
import yaml

# Function to read YAML file
def read_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Function to print greeting message
def print_greeting(yaml_data):
    message = yaml_data['greeting']['message']
    language = yaml_data['greeting']['language']
    print(f"{message} (Language: {language})")

if __name__ == "__main__":
    yaml_file = 'hello-world.yaml'
    yaml_data = read_yaml(yaml_file)
    print_greeting(yaml_data)

