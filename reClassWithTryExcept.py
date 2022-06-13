###  Create String variables and search a character and/or pattern of characters and position within the string

import re

txt = "loyalist college is in belleville, canada"

char1 = re.search('a', txt)
print(char1)
print("The searched character's first location is at : ", char1.start())

char2 = re.search('le', txt)
print(char2)
print("The searched pattern of characters' first location is at : ", char2.start())

# Utilize the sub function to replace spaces and/or characters

print("Replace all spaces with '#' in the string :")
str1 = re.sub("\s", "#", txt)
print(str1)

print("Replace all character 'e' with character 'Z' in the string :")
str2 = re.sub("e", "Z", txt)
print(str2)

# Find all characters of the same value within the string
print("Find all characters of 'le' in the string and print them in list")
str3 = re.findall("le", txt)
print(str3)

# Split the string into array values and output the various array values into various variables
print("Split the string and store into array")
arr1 = re.split('\s', txt)
print(arr1)
for i in range(0, len(arr1)):
    print('Array value at :', i, "th position is :", arr1[i])

# Sub values in a string.
var = txt.index(',')
print(var)
print(txt[0:var-1])
print(txt[var:len(txt)])

###########     Utilize the Try except else commands to catch errors.  Show with an error and a success.
############    (try to use a loop function in the success portion of the code) - Bonus

arr2 = [100, 'loyalist', 50, 10, 'belleville', 3]
val = 2

arr3 = [0] * 6
for i in range(0, len(arr2)):
    try:
        output = arr2[i] / val
        print(output)
    except:
        print("String value can not be divided by an integer")
    else:
        print("Value after divide operation is :", output)
        arr3[i] = output
    finally:
        print('try except block completed. This block always executed in try, except else case')

print(arr3)

