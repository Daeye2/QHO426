import csv

records = []
headings = []

def load_data(file_path):
    global records, headings
    print("Loading data...")

    with open(file_path, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        headings = next(csv_reader)

        for row in csv_reader:
            records.append(row)

def run():
    global records
    file_path = "titanic.csv"
    load_data(file_path)

    print(f"Successfully loaded {len(records)}")
    print("Done")

run()
