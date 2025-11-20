import csv
from utils.Monolog import Monolog

def read_in_monolog_csv(filepath: str) -> list[Monolog]:
    results: list[Monolog] = []
    with open(filepath, mode="r") as file:
        csv_file = csv.DictReader(file)
        for line in csv_file:
            monolog = Monolog(no=int(line["no"]), lesson_number=line["lesson_number"], type=line["type"], text=line["text"], speaker_gender=line["speaker_gender"])
            results.append(monolog)
    return results