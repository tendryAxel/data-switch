from src.main import _Conversion

if __name__ == '__main__':
    c = _Conversion(".\\in\\test.csv", ".\\out\\test.json")
    c.convert()
    c.save()
