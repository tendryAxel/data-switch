from src.main import Conversion

if __name__ == '__main__':
    c = Conversion("test")
    c.convert()
    c.save(result_type="psql")
