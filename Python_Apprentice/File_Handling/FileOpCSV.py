import csv

file = open('python_aprentice/File_handling/record.csv', 'r')

with file:
    read = csv.reader(file, delimiter = '|')

    for row in read:
        print(row)

file.close()

file = open('python_aprentice/File_handling/record_no_deli.csv', 'r')
with file: 
    read = csv.DictReader(file)

    for row in read:
        print(dict(row))
file.close()

names = [['FirstName', 'LastName'],
        ['Sofia', 'Reyes'],
        ['Jerome', 'Jackson'],
        ['Jia', 'Zhong']] 

file = open('python_aprentice/File_handling/names.csv', 'w' )

with file: 
    file_writer = csv.writer(file)
    for row in names:
        file_writer.writerow(row)

file.close()