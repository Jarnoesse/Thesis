#this simple function convert from exadecimal/binary to decimal.
#the numbers are ordered to reflect the "i+n" order from the documentation, so for example i will come before i+1
def number_converter(list):

    space = False
    is_binary = True

    for digit in list:

        #early checks for format
        if digit == ' ':
            space = True
        #checks if the number is in binary
        if digit != '1' and digit != '0':
            is_binary = False

    #removes some spaces that may have been retained with the string format from the txt document
    if space:
        list = list[1:len(list)]

    if is_binary:

        second = int("".join(list[4:16]),2)
        first = int("".join(list[20:len(list)]),2)

    else:
        #it assumes a exadecimal data format where the word is 8 characters long
        #it join the list as a string again then it converts the string into a decimal number
        second = int("".join(list[1:4]),16)
        first = int("".join(list[5:len(list)]),16)

    return first, second
