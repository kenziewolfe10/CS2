import random

def reverse_string(string):
    return string[::-1]

def vowel_count(name):
    '''
    Takes name and returns number of vowels
    args:
        name = word that vowels are being counted 
    returns:
        return: number of vowels in name
    '''
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vcount = 0
    for letter in name:
        if letter in vowels:
            vcount += 1

    return vcount

def consonant_count(name):
    consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    ccount = 0
    for letter in name:
        if letter in consonant:
            ccount += 1
    return ccount


def first_name(name):
    output = ""
    for letter in name:
        if letter == " ":
            break
        else:
            output = output + letter
    return output

def last_name(name):
    print("inside last name func")
    name_out = ""
    for i in range(len(name)-1,-1,-1):
        if name[i] == " ":
            break
        else:
            name_out = name_out + name[i]
    name_out = reverse_string(name_out)
    return name_out


def lower_case(name):
    '''
    This takes the letter given and sees if it is capital. It then convets it to the number sequences and converts it from uppercase to lowercase.
    args:
        name = word that computer goes through each letter to change to lower case 
    returns:
        name_out = 
    '''
    name_out = ""
    for letter in name:
        if ord(letter)>64 and ord(letter)<91:
            num = ord(letter)
            num = num + 32
            letter = chr(num)
            name_out = name_out + letter
        else:
            name_out = name_out + letter
    return name_out

def upper_case(name):
    '''
    This takes the letter given and sees if it is lowercase. It then convets it to the number sequences and converts it from lowercase to uppercase.
    '''
    name_out = ""
    for letter in name:
        if ord(letter) > 96 and ord(letter) < 123:
            num = ord(letter)
            num = num - 32
            letter = chr(num)
            name_out = name_out + letter
        else:
            name_out = name_out + letter
    return name_out

def hyphen_check(name):
    if "-" in name:
        return "True"
    else:
        return "False"

def main():
    name = input("Enter your full name: ")

    while True:
        choice = input("Which function do you want to run?")

        if choice == '1':
            output = reverse_string(name)
            print(output)
        elif choice =='2':
            output = vowel_count(name)
            print("TOTAL VOWELS:" + str(output))
        elif choice == '3':
            output = consonant_count(name)
            print("TOTAL CONSONANTS:" + str(output))
        elif choice == '4':
            output = first_name(name)
            print(output)
        elif choice == '5':
            output = last_name(name)
            print(output)
        elif choice == '6':
            output = lower_case(name)
            print(output)
        elif choice == '7':
            output = upper_case(name)
            print(output)
        elif choice == '8':
            output = hyphen_check(name)
            print(output)
main()