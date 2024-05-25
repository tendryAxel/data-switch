from src.main import MultiConversion

if __name__ == '__main__':
    c = MultiConversion("test")
    c.convert()
    c.save(result_type="psql")
