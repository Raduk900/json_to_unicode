import unittest
import json
import os
from json_reader import JsonReader

class TestJsonReader(unittest.TestCase):
    
    def setUp(self):
        self.file_paths = {
            'utf8': 'tests/test_utf8.json',
            'utf16': 'tests/test_utf16.json',
            'invalid': 'tests/test_invalid.json'
        }
        with open(self.file_paths['utf8'], 'w', encoding='utf-8') as f:
            json.dump({"name": "John"}, f)

        with open(self.file_paths['utf16'], 'w', encoding='utf-16') as f:
            json.dump({"name": "John"}, f)

        with open(self.file_paths['invalid'], 'w', encoding='utf-8') as f:
            f.write("invalid json")

    def tearDown(self):
        for file_path in self.file_paths.values():
            os.remove(file_path)

    def test_read_utf8(self):
        reader = JsonReader(self.file_paths['utf8'])
        self.assertEqual(reader.read(), {"name": "John"})

    def test_read_utf16(self):
        reader = JsonReader(self.file_paths['utf16'])
        self.assertEqual(reader.read(), {"name": "John"})

    def test_read_invalid(self):
        reader = JsonReader(self.file_paths['invalid'])
        self.assertIsNone(reader.read())

if __name__ == '__main__':
    unittest.main()
