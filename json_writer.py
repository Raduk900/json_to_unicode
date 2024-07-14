import json

class JsonWriter:
    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, data):
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error writing to file {self.file_path}: {e}")
