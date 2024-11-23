import csv

with open("disneyland_reviews.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for column in csv_reader:
        print(column[1])