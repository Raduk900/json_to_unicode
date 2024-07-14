class JsonConverter:
    hex_string_map = {}

    @staticmethod
    def encode_to_utf16(data):
        if isinstance(data, dict):
            return {JsonConverter.encode_string(key): JsonConverter.encode_to_utf16(value) for key, value in data.items()}
        elif isinstance(data, list):
            return [JsonConverter.encode_to_utf16(item) for item in data]
        elif isinstance(data, str):
            encoded_string = JsonConverter.encode_string(data)
            JsonConverter.hex_string_map[data] = JsonConverter.encode_to_hex(data)
            return encoded_string
        else:
            return data

    @staticmethod
    def encode_string(value):
        """Stringas į Unikodą. Čia jeigu mes pridedame vieną '\' ir saugojame kaip json formatą, automatiškai yra pridedamas dar vienas '\' nes '\' jsone reiškia nauja eilutė"""
        return ''.join(fr"\u{ord(char):04x}" for char in value)

    @staticmethod
    def save_hex_map(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            for original, encoded in JsonConverter.hex_string_map.items():
                file.write(f"{original} -> {encoded}\n")

    @staticmethod
    def generate_hex_map(data):
        JsonConverter._generate_hex_map_recursive(data)

    @staticmethod
    def _generate_hex_map_recursive(data):
        if isinstance(data, dict):
            for key, value in data.items():
                JsonConverter._add_to_hex_map(key)
                JsonConverter._generate_hex_map_recursive(value)
        elif isinstance(data, list):
            for item in data:
                JsonConverter._generate_hex_map_recursive(item)

    @staticmethod
    def _add_to_hex_map(value):
        if isinstance(value, str):
            JsonConverter.hex_string_map[value] = JsonConverter.encode_to_hex(value)

    @staticmethod
    def encode_to_hex(value):
        return ''.join(fr"\x{ord(char):02x}" for char in value)

    @staticmethod
    def decode_from_utf16(data):
        if isinstance(data, dict):
            return {JsonConverter.decode_from_utf16(key): JsonConverter.decode_from_utf16(value) for key, value in data.items()}
        elif isinstance(data, list):
            return [JsonConverter.decode_from_utf16(item) for item in data]
        elif isinstance(data, str):
            decoded_string = ''
            parts = data.split('\\u')
            for part in parts:
                if part:
                    decoded_string += chr(int(part, 16))
            return decoded_string
        else:
            return data
