import csv

user = "user1"

with open("1.csv", 'r') as inf, open('2.csv', 'w', newline="") as outf:
    csvreader = csv.DictReader(inf)
    # add column name to beginning
    source = "source"
    user = "user1"
    fieldnames = [source] + csvreader.fieldnames
    csvwriter = csv.DictWriter(outf, fieldnames)
    csvwriter.writeheader()

    for (source, row) in enumerate(csvreader, 1):
        csvwriter.writerow(dict(row, source=user))
