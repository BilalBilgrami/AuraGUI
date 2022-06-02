import csv

header = ['m', 'x', 'y']
data = [
    ['l', 0, 0],
    ['l', 6, 20],
    ['l', 10, 20],
    ['l', 10, 0],
    ['l', 8, 0],
    ['l', 8, 5],
    ['l', 4, 5],
    ['l', 0, 0],
    [],
    ['l', 5, 8],
    ['l', 8, 16],
    ['l', 8, 8],
    ['l', 5, 8]
]

with open('A.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)
