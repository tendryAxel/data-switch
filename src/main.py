import csv
import glob
import json
from typing import TextIO

from src.utils import printer


class _Conversion:
    def __init__(self, in_file_name, out_file_name):
        self.in_file_name = in_file_name
        self.out_file_name = out_file_name

        self.result = []
        self.content = list(csv.reader(open(self.in_file_name, 'r')))

    @printer
    def save(self, result_type="json", file: TextIO = None):
        save_types = {
            "json": lambda: json.dump(self.result, (open(self.out_file_name + ".json", 'w') if file is None else file),),
            "psql": lambda: (open(self.out_file_name + ".sql", 'w') if file is None else file).write(create_insert_psql(self.in_file_name.split('.')[-1], self.result))
        }
        if result_type in save_types.keys():
            save_types[result_type]()
            return True
        raise RuntimeError(f"the type:<{result_type}> is not supported")

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


def create_insert_psql(table: str, column_value: list[dict[str, str]], if_empty_case: str = "") -> str:
    keys = column_value[0].keys()
    values = [f'({", ".join([lines.get(k) if k in lines.keys() else if_empty_case for k in keys])})' for lines in column_value]
    values = ", ".join(values)
    return f'INSERT INTO "{table}"({", ".join(keys)}) VALUES {values};'


class Conversion(_Conversion):
    def __init__(self, relative_file_name):
        in_file_name = f".\\in\\{relative_file_name}.csv"
        super().__init__(in_file_name, Conversion.in_path_to_out(in_file_name))

    @staticmethod
    def in_path_to_out(path: str) -> str:
        split = path.split("\\")
        split[1] = "out"
        result = "\\".join(split)
        result = result.split(".")[:-1]
        return ".".join(result)


class MultiConversion:
    def __init__(self, relative_folder):
        self.list_file = glob.glob(f".\\in\\{relative_folder}\\*.csv")
        self.list_conversion = [_Conversion(file, "\\".join(Conversion.in_path_to_out(file).split("\\")[:-1])) for file in self.list_file]

    def convert(self):
        [c.convert() for c in self.list_conversion]

    def save(self, result_type="json"):
        file = open(".\\out\\test.sql", 'w')
        [c.save(result_type=result_type, file=file) for c in self.list_conversion]
