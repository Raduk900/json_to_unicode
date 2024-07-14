import unittest
import os
import json
from json_writer import JsonWriter

class TestJsonWriter(unittest.TestCase):

    def test_write(self):
        file_path = 'tests/test_output.json'
        data = {"name": "John"}

        writer = JsonWriter(file_path)
        writer.write(data)

        with open(file_path, 'r', encoding='utf-8') as f:
            self.assertEqual(json.load(f), data)

        os.remove(file_path)

if __name__ == '__main__':
    unittest.main()
