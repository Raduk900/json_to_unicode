import os
import queue
from threading import Thread
from json_reader import JsonReader
from json_converter import JsonConverter
from json_writer import JsonWriter

class JsonFileProcessor(Thread):
    def __init__(self, file_queue, mode):
        super().__init__()
        self.file_queue = file_queue
        self.mode = mode

    def run(self):
        while not self.file_queue.empty():
            input_file = self.file_queue.get()
            output_file = f"{self.mode}_{os.path.basename(input_file)}"

            reader = JsonReader(input_file)
            data = reader.read()

            if data is not None:
                converter = JsonConverter()
                if self.mode == 'encode':
                    converted_data = converter.encode_to_utf16(data)
                elif self.mode == 'decode':
                    converted_data = converter.decode_from_utf16(data)

                writer = JsonWriter(output_file)
                writer.write(converted_data)

            self.file_queue.task_done()
