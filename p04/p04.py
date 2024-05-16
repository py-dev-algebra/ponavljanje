import os
from typing import List, Dict


class FileManager:
    def __init__(self, file_path: str = 'data') -> None:
        # if os.path.exists(file_path):            
        #     self.file_path = file_path
        # else:
        #     os.makedirs(file_path)
        #     self.file_path = file_path
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        self.file_path = file_path


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