import os
from json_converter import JsonConverter
from json_reader import JsonReader
from json_writer import JsonWriter

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def process_files(mode):
    output_folder = "result"
    ensure_directory_exists(output_folder)

    if mode == "encode":
        source_folder = "to_encode"
        for filename in os.listdir(source_folder):
            if filename.endswith('.json'):
                file_path = os.path.join(source_folder, filename)
                reader = JsonReader(file_path)
                data = reader.read()
                if data is not None:
                    encoded_data = JsonConverter.encode_to_utf16(data)
                    output_path = os.path.join(output_folder, filename)
                    writer = JsonWriter(output_path)
                    writer.write(encoded_data)
                    print(f"Encoded and saved: {output_path}")

        JsonConverter.generate_hex_map(data)
        hex_map_output_path = os.path.join(output_folder, "hex_string_map.txt")
        JsonConverter.save_hex_map(hex_map_output_path)
        print(f"Hex string map saved: {hex_map_output_path}")

    elif mode == "decode":
        source_folder = "to_decode"
        for filename in os.listdir(source_folder):
            if filename.endswith('.json'):
                file_path = os.path.join(source_folder, filename)
                reader = JsonReader(file_path)
                data = reader.read()
                if data is not None:
                    decoded_data = JsonConverter.decode_from_utf16(data)
                    output_path = os.path.join(output_folder, filename)
                    writer = JsonWriter(output_path)
                    writer.write(decoded_data)
                    print(f"Decoded and saved: {output_path}")

if __name__ == "__main__":
    mode = input("Choose mode (encode/decode): ").strip().lower()
    if mode in ["encode", "decode"]:
        process_files(mode)
    else:
        print("Invalid mode selected.")
