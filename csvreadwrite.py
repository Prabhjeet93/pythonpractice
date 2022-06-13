import csv

# with open("C:\data\output4.csv", 'w', newline='') as csvfile :
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     write = csv.DictWriter()
#
#     writer.writeheader()
#     writer.writerow({'first_name':'Baked','last_name':'Beans'})
#     writer.writerow({'first_name': 'ram', 'last_name': 'joshi'})
#     writer.writerow({'first_name': 'tim', 'last_name': 'cook'})

# with open('names.csv', 'w', newline='') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
from csv import reader
from csv import writer

with open('input.csv', 'w', newline='') as csvfile:
    fieldnames = ['Student_ID', 'First']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    count = input("Enter no. of rows : ")
    name = [0] * int(count)
    for i in range(0, int(count)):
        name[0] = input("Input student ID : ")
        name[1] = input("Input First name : ")
        fieldnames = ['Student_ID', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'Student_ID': str(name[0]), 'last_name': name[1]})
with open('names6.csv', 'a', newline='') as csvfile:
    fieldnames = ['last_name', 'Marks']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

count_rows = input("Enter no. of rows : ")
last_name = [0]*int(count_rows)
for i in range(0, int(count_rows)):
    last_name[0] = input("Input last name : ")
    last_name[1] = input("Input marks of students : ")
    with open('names5.csv', 'a', newline='') as csvfile:
        fieldnames = ['last_name', 'Marks']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'last_name': str(last_name[0]), 'Marks': last_name[1]})
default_text = 'Some Text'
# Open the input_file in read mode and output_file in write mode
with open('input.csv', 'r') as read_obj, \
        open('output_1.csv', 'w', newline='') as write_obj:
    # Create a csv.reader object from the input file object
    csv_reader = reader(read_obj)
    # Create a csv.writer object from the output file object
    csv_writer = writer(write_obj)
    # Read each row of the input csv file as list
    for row in csv_reader:
        # Append the default text in the row / list
        row.append(default_text)
        # Add the updated row / list to the output file
        csv_writer.writerow(row)



