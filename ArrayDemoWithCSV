import csv

# defining array with different type of data types and printing its values and types
arr = [1,'a',3.2,4,"prabhjeet",True]    # array contains integer, string, float and boolean type values
count = len(arr)   # finding length of the array
## printing the values of array with loop
for i in range(0, count):   # for loop to traverse the array values and printing its type, values and position of the array
    print(f"Value at  {i}th position of given array is {arr[i]} and its type is {type(arr[i])}")


## Entering array values from keyboard or user
arr1 = [0]*5              # Defining an empty array of length 5
for i in range(0, 5):     # for loop for the entering names in an array from keyboard on the go
    arr1[i] = input("name : ")
count1 = len(arr1)         # finding length of the array
for i in range(0, count1):   # for loop to traverse the array values and printing its values entered by user and position of the array
    print(f"Name at  {i}th position of entered array is {arr1[i]}")


# Calculation on array
arr2 = [0,1,2,3,4,5,6,7,8,9]    # defining an integer array with simple values
arr3 = [0]*10     # defining an empty array of length 10 to store even values
arr4 = [0]*10      # defining an empty array of length 10 to store odd values
for i in range(0, len(arr2)):
    arr3[i] = int(arr2[i]*2)        # calculation on array value - multplying the values by 2
    arr4[i] = int(arr2[i]*2) +1     # calculation on array value - multplying the values by 2 and adding 1

print("Print Even numbers")
for i in range(0, len(arr2)):
    print(arr3[i])                  # printing the even values
#
print("Print Odd numbers")
for i in range(0, len(arr2)):
    print(arr4[i])                  # printing the odd values


# Array integer values converting to string and printing them
arr5 = [0]*5                  # empty array of length 5
arr6 = [90,91,100,88,75]      # intger array containing marks of a student name Jack
for i in range(0, len(arr5)):
    arr5[i] = input("Subject : ")   # entering subject values from keyboard and storing in an array
count1 = len(arr6)                  # finding length of the array
print("Jack got below marks in his high school")
for i in range(0, count1):
    print("In Subject: "+arr5[i]+" received: "+str(arr6[i])+" marks")  # print the subjects values and converted integers values(matks) to string.



# Creating a csv file and storing the data into that and then reading from it

row_list = [["ID", "Name", "Company"],            #storing header row in the list.
             [1001, "Prabhjeet", "Google"],        #storing Data row 1 in the list.
             [1002, "Rahul", "Yahoo"],             #storing Data row 2 in the list.
             [1003,"Ram", "Adobe"],                #storing Data row 3 in the list.
            [1003,"Shyam", "Microsoft"]]           #storing Data row 4 in the list.

with open('C:\data\output.csv', 'w',newline='') as file:    # creating and opening a file to write into a csv file at given location and 'w' parameter write.
    writer = csv.writer(file)                               #Begin to write in the csv file
    writer.writerows((row_list))                           #Writing the list to the csv file row wise

print (row_list [3])                              #Output array element 3 to console

with open("C:\data\output.csv", "r") as csvfile:         # opening a csv file at given location and 'r' parameter is for reading.
    reader_var = csv.reader(csvfile, delimiter=",")      # storing the rows of a csv file into a list variable
    for row in reader_var:                       # for loop to traverse the list
        print(row)                              # printing the rows one by one


