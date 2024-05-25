import csv
import json

from src.utils import printer


class _Conversion:
    def __init__(self, in_file_name, out_file_name):
        self.in_file_name = in_file_name
        self.out_file_name = out_file_name

        self.result = []
        self.content = list(csv.reader(open(self.in_file_name, 'r')))

    @printer
    def save(self):
        json.dump(self.result, open(self.out_file_name, 'w'))

    @printer
    def convert(self):
        self.clear_results()
        row_name = self.content[0]
        for line in range(1, len(self.content)):
            tmp = {}
            for name_id in range(len(row_name)):
                tmp[row_name[name_id]] = self.content[line][name_id]
            self.result.append(tmp)

    def clear_results(self):
        self.result = []
