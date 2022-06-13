import csv

## creating and writing into a  csv file
with open('name.csv', 'w', newline='') as csvfile:               # create and open a csv file, w parameter is for the write
    fieldnames = ['Student_ID', 'Name']                        # Enter 2 column names in the csv file
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)    ## Start writing into csv file
    writer.writeheader()     # Write the headers in the csv file
    count = input("Enter no. of rows to write in csv file : ")   # Enter no. of rows for csv file
    name = [0] * int(count)                                      # Define and initialize array for the input values from keyboard
    for i in range(0, int(count)):                               # for loop to traverse
        name[0] = input("Enter First name : ")                   # Enter name from keyboard
        name[1] = input("Enter Marks : ")                        # Enter marks  from keyboard
        fieldnames = ['Name', 'Marks']                         # defining column names
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  ## Start writing the data from keyboard
        writer.writerow({'Name': str(name[0]), 'Marks': name[1]})   ##  Write the name and marks from keyboard into csv file

with open("name.csv", "r") as csvfile:         # Open a csv file at given location and 'r' parameter is for reading.
    reader_var = csv.reader(csvfile, delimiter=",")      # Store the rows of a csv file into a list variable
    for row in reader_var:                       # for loop to traverse the csv data list
        print(row)                              # Print the csv file data


### Append the data entered from keyboard into the existing csv file
count_new = input("Enter no. of rows to be added in csv file: ")                 # enter no. of rows to append in the csv file
name1 = [0]*int(count_new)                                # Define a new array for entering values from keyboard , for appending the data
for i in range(0, int(count_new)):                        # for loop to traverse
    name1[0] = input("Enter First name : ")               # Enter name from keyboard
    name1[1] = input("Enter Marks : ")                     # Enter marks  from keyboard
    with open('name.csv', 'a', newline='') as csvfile:     # Open an existing csv file, 'a' parameter is for the append in the file
        fieldnames = ['Student_ID', 'Name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)           ## Start writing the values from keyboard.
        writer.writerow({'Student_ID': str(name1[0]), 'Name': name1[1]})  ##  Write the values entered from keyboard into csv file

with open("name.csv", "r") as csvfile:                         # Open a csv file at given location and 'r' parameter is for reading.
    reader_var = csv.reader(csvfile, delimiter=",")            # Store the rows of a csv file into a list variable
    for row in reader_var:                                     # for loop to traverse the csv data list
        print(row)                                             # Print the csv file data







