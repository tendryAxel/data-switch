from src.main import _Conversion, create_insert_psql

if __name__ == '__main__':
    c = _Conversion(".\\in\\test.csv", ".\\out\\test.json")
    c.convert()
    c.save()
    print(create_insert_psql("user", [
        {"name": "axel", "age": "2", "test": "bien"},
        {"age": "2", "name": "axel"},
    ]))
