from json import loads, dumps
from os.path import exists


class File:
    def __init__(self, filename) -> None:
        self.filename = filename

    def append_item(self, item: list):
        data = self.read_file()
        data += item
        self.write_file(data)

    def read_file(self) -> list:
        json = ""
        if exists(self.filename):
            with open(self.filename, 'r') as f:
                json = f.readline()
        return self._load_data(json)

    def _load_data(self, json: str) -> list:
        try:
            data = loads(json)
            if type(data) != list:
                return []
            return data
        except Exception:
            print('deu merda na hora de ler')
            return []

    def write_file(self, data: list[dict]):
        with open(self.filename, 'w+') as f:
            f.write(dumps(data))
