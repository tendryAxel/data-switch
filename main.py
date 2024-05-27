from src.main import MultiConversion

if __name__ == '__main__':
    print(f"{'-'*20}\nWelcome to this Python application\n{'-'*20}\n")
    print("Todo:")
    print("\t- Create the folder /in")
    print("\t- put all of your .csv file in the folder in /in")
    c = MultiConversion(input("The name of the folder in /in: "))
    c.convert()
    c.save(result_type=input("The type of result(json/psql): "))
