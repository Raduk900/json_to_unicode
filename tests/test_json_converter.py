import unittest
from json_converter import JsonConverter

class TestJsonConverter(unittest.TestCase):
    
    def test_encode_to_utf16(self):
        input_data = {"name": "John", "age": 30, "is_employee": True}
        expected_output = {
            "\\u006e\\u0061\\u006d\\u0065": "\\u004a\\u006f\\u0068\\u006e",
            "\\u0061\\u0067\\u0065": 30,
            "\\u0069\\u0073\\u005f\\u0065\\u006d\\u0070\\u006c\\u006f\\u0079\\u0065\\u0065": True
        }
        self.assertEqual(JsonConverter.encode_to_utf16(input_data), expected_output)

    def test_decode_from_utf16(self):
        input_data = {
            "\\u006e\\u0061\\u006d\\u0065": "\\u004a\\u006f\\u0068\\u006e",
            "\\u0061\\u0067\\u0065": 30,
            "\\u0069\\u0073\\u005f\\u0065\\u006d\\u0070\\u006c\\u006f\\u0079\\u0065\\u0065": True
        }
        expected_output = {"name": "John", "age": 30, "is_employee": True}
        self.assertEqual(JsonConverter.decode_from_utf16(input_data), expected_output)

if __name__ == '__main__':
    unittest.main()
