
#        Demonstrate the use of the re class in python

####   1. Create String variables and search a character and/or pattern of characters and position within the string
import re

str1 = "canada is very beautiful country and capital of canada is ottawa"   # String Variable created on which all the operations will be performed

# search pattern of characters
chars = re.findall('[a-c]',str1)     # Searching the characters between 'a' and 'c' in the main string
print("printing all the characters between a and c in the given string : ", chars)   # printing all the characters between 'a' and 'c' in the main string

searched_txt1 = re.search('b',str1)    ## searching a character in the string
print(searched_txt1)                   ## printing the statement whether char is present or not
pos1 = searched_txt1.start()           ## finding the position of the matched character in the string
print("The first string is located in the position : ", pos1)   ## printing the location of the matched character

# search a substring in the string and print its position
searched_txt2 = re.search('canada',str1)    ## searching a a substring in the string
print(searched_txt2)                        ## printing the statement whether substring is present or not in the main string

pos2 = searched_txt2.start()               ## finding the position of the matched substring in the string
print("The first string is located in the position : ", pos2)   ## printing the location of the matched substring

#### 2. Output out of the position of character to a variable as an integer

str1 = "canada is very beautiful country and canada capital is ottawa"
pos = str1.index('b')                                                   ## find the index of a character to divide the string
print("Position of the given character in the main string",pos)       # print the position of the character b in the string

print("String divided on the basis of above character")
print(str1[0:pos-1])           # Divide or split the string which is starting from 0 index to position which is found above i.e till 'b' character's location
print(str1[pos:len(str1)])     # Divide or split the string which is starting position which is found above i.e till 'b' character's location to end of the string's index


#Utilize the sub function to replace spaces and/or characters

print("Replacing all the whitespaces with underscore in the main string :")
modified_str1 = re.sub("\s","_", str1)   ## replace all the white space with underscore in the main string with Sub method
print(modified_str1)                     ## printing the modified string after adding the underscore in place of space.

print("Replacing lower c with capital C  in the main string :")
modified_str2 = re.sub('c','c'.upper(), str1)    ## Replacing lower 'c' with capital 'C'  in the main string with sub method
print(modified_str2)                             ## printing the modified string after replacing the small 'c' letter with capital 'C' letter

print("Replacing canada with Ontario in the main string :")
modified_str3 = re.sub('canada','Ontario', str1)    ## Replacing 'canada' word with 'ontario' in the main string with sub method
print(modified_str3)                               ## printing the modified string after replacing the 'canada' word with 'ontario'

#Find all characters of the same value within the string
print("print list of characters 'ca' in the main string")
sub_char = re.findall("ca", str1)        ##finding and storing in the list, all the occurrence of 'ca' characters in the main string
print(sub_char)                          ## printing the list of the characters which has all the occurrence of the 'ca' characters



#Split the string into array values and output the various array values into various variables
print("Breakdown the main string in to array of substrings and split on the basis of whitespace")
arr = re.split('\s',str1)         # split the string wherever whitespace comes in to it and store into string array
print(arr)                       # print the string array
for i in range(0, len(arr)):     # for loop to traverse the string array to store and print the array values
    print('substring at index : ',i," is : ",arr[i])    ## print the string array values and positions.

print("Breakdown the main string in to array of substrings and split on the basis of coma ',' ")
str2 = "This is canada,It is a country"     ### new string defined for the split operation
arr = re.split(',',str2)        ## split the string whenever coma ',' comes in the string and store in to array
print(arr)                 ## print the string array
for i in range(0, len(arr)):     # for loop to traverse the string array to store and print the array values
    print('substring at index : ',i," is : ",arr[i])    ## print the string array values and positions.

print("Breakdown the main string in to character array and split and store values character wise  and split with pipe '|' ")
char_arr = re.split('|',str1)   ## split the string with pipe '|' to generate character array of the string
print(char_arr)                # Print character array values


#Sub values in a string.
str2 = "this is canada,it is a country"          ### new string defined for the substitute or replace operation
modified_str3 = re.sub("i","8", str2)            ## replace or substitute the character 'i' in string with integer 8 with sub method in the string
print(modified_str3)                           # print the modified string after replacing i character with integer 8

####################   Utilize the Try except else commands to catch errors.  Show with an error and a success.
#################      (try to use a loop function in the success portion of the code) - Bonus

arr1 = [1,2,'hero',4,9,'team']      ## Array1 defined with different integer and string values
arr2 = [3, 'canada',5,7,3,18,'snow']  ## Array2 defined with different integer and string values

if len(arr1)>=len(arr2):        # if condition to check which array has less length than other and then assign that length to a variable
    count = len(arr2)        # variable to assign lesser length of array
else:
    count  = len(arr1)      # variable to assign lesser length of array

final_list = []                    # Empty list defined to store the addition operation's values which will do on arrays defined above.
                                   # I took the list here because it's size will be dynamic in nature.

for i in range(0, count):          # for loop to traverse the both arrays
    try:                           # try statement
        val = arr1[i] + arr2[i]    # Store addition operation value in a variable

    except:                        # except statement to capture exception
        print("Values ",arr1[i]," and ",arr2[i], " of both arrays can not be added because one of the value's type is mismatching")    ## print the exception position and message
    else:                  # else statement for the successful execution of the addition operation
        print("Array values at : ", i, "position is : ",final_list.append(val))    ## print the the position and value of successful operation.

    finally:     # final statement which always runs
        print("Elements in the array currently are : ", final_list)   # print the list values after every iteration of the operation's loop

print("Final list after addition operation on both arrays : ")
print(final_list)               # printing the final list after operation and now its length is 3
