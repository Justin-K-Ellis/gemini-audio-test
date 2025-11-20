from dotenv import load_dotenv

from lib.getmonolog import get_monolog
from lib.read_monolog_csv import read_in_monolog_csv

load_dotenv()

def main():
    monologs_path = "./input/monologs.csv"
    monologs = read_in_monolog_csv(filepath=monologs_path)
    for monolog in monologs:
        get_monolog(monolog=monolog)


if __name__ == "__main__":
    main()
