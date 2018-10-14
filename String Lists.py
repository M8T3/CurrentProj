# Note: This program does not work if characters of "string" are not all entered in the same case (i.e. all lowercase or all uppercase)

string = input("Give me a phrase: ")

back = ""

backwards = ""

n = len(string) - 1

string_back = string[len(string)::-1] # 1st Version of Program 
                                      # this treats len(string) as element outside of the list and excludes
                                      # it because of the -1 increment size; used " " instead of "0" for end index
                                      #  to include all elements in "string"

while n >= 0:                         # 2nd Version of Program 
    back = back + string[n]
    n -= 1

for letter in string:                 # 3rd Version of Program
    if n >= 0:
        backwards = backwards + string[n]
        n -= 1
    else:
        break

p = 1
for letter in string:
    print("Letter " + str(p) + ": " + letter)
    p += 1

if backwards == string:
    print(string + " is a palindrome.")
else:
    print(string + " is not a palindrome.")

