import json
import os

def load_json_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Target file not found at: {file_path}")
    with open(file_path, 'r') as file:
        return json.load(file)
      
