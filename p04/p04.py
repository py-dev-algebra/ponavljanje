import os
from typing import List, Dict
from dotenv import load_dotenv


class FileManager:
    def __init__(self, file_path: str = '') -> None:
        # if os.path.exists(file_path):            
        #     self.file_path = file_path
        # else:
        #     os.makedirs(file_path)
        #     self.file_path = file_path

        if not os.path.exists(file_path):
            os.makedirs(self.file_path)
            self.file_path = file_path
        else:
            self.set_file_path()

    def set_file_path(self):
        load_dotenv()
        self.file_path = os.getenv('FILE_PATH')


    def write(self, data: str, file_name: str, mode: str='a'):
        try:
            with open(f'{self.file_path}/{file_name}.txt', mode) as file_writer:
                file_writer.write(str(data) + '\n')

        except Exception as ex:
            print(f'Dogodila se greska: {ex}')

    def read(self, file_name: str, mode: str='r'):
        try:
            with open(f'{self.file_path}/{file_name}.txt', mode) as file_reader:
                return file_reader.read()

        except Exception as ex:
            print(f'Dogodila se greska: {ex}')