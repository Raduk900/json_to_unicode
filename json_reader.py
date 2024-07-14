import json

class JsonReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        encodings = ['utf-8', 'utf-16']
        for encoding in encodings:
            try:
                with open(self.file_path, 'r', encoding=encoding) as file:
                    return json.load(file)
            except FileNotFoundError:
                print(f"File not found: {self.file_path}")
                return None
            except json.JSONDecodeError:
                print(f"Error decoding JSON from file with encoding '{encoding}': {self.file_path}")
            except UnicodeError as e:
                print(f"Unicode decoding error with encoding '{encoding}': {e}")
        print("Failed to read the file with all attempted encodings.")
        return None
