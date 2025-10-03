'''
Author: Kenzie Wolfe
Due Date: 10/3/2025
Bugs: limited number of titles in list
Bonus: Returns boolean if name contains a title and contains a menu
Sources: Ms. Marciano and Mr. Cambell
Log: 1.0 initial release
'''


import random

def reverse_string(string):
    '''
    Description: takes a word and prints it reversed
    Args:
        string(string): word or phrase
    returns:
        str: string reversed
    '''
    return string[::-1]

def vowel_count(name):
    '''
    Description: Checks the name with the list of vowels and check if each letter is a vowel. If a letter is a vowel it adds ot the vowel count.
    args:
        string(name): word/phrase that vowels are being counted 
    returns:
        return: number of vowels in name
    '''
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vcount = 0
    #for each letter (character) in the name it checks if it is a vowel from the list above. If it is it adds 1 to the vowel count to then print later 
    for letter in name:
        if letter in vowels:
            vcount += 1

    return vcount

def consonant_count(name):
    '''
    Description: Checks the name with list belows and checks each letter to see if it is consonant. If it is a consonant it will add to constant count
    args: 
        string(name): word/phrase that consonants are being counted
    returns:
        return: number of consonants in name 
    '''
    consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    ccount = 0
    #for each letter (character) it will check if it in a consonant from list above, if it is it will be added to consonant count
    for letter in name:
        if letter in consonant:
            ccount += 1
    return ccount

def get_names(fullname):
    '''
    Description: Makes a split function, so it splits the first, middle, and last name into seperate arrays
    Args:
        String (fullname): word or phrase
    Returns:
        string: seperate arrays of names
    '''
    names = []
    name = ''
    # it goes through each character and sees if it is a space. If it is a space it will split the names and return the name as arrays. 
    for letter in fullname:           #for each character in fullname
        if letter == " ":             #if the character is a space
            names.append(name)        #split the first, middle, and last name
            name = ''                 #sets variable as empty
        else:                       
            name += letter            #adds the letters to the string(name)
    names.append(name)                #adds string to list of names
    return names
def first_name(fullname):
    '''
    Description: It takes the first array in fullname from the split function. It then checks if it contains a title and if it does it adds it to names_list so it doesnt print as a first name. 
    args:
        string(fullname): word/phrase 
    return:
        return: first name
    '''
    fullname = remove_title(fullname)    #this calls the function remove_title to remove the title from the name
    names_list = get_names(fullname)     #takes the arrays from get_titles
    return names_list[0]                 #returns first item in the list(0)

   

def last_name(fullname):
    '''
    Description: Uses get_names to print the last name, once it finds a space the code will stop and print the last name
    args:
        String(name): word/phrase that each character is counted from last charcter to the space. Then the stirng gets reversed.
    returns:
        returns last name
    '''
    fullname = remove_title(fullname)  #this calls the function remove_title to remove the title from the name
    names = get_names(fullname)
    return names[-1]                   #goes through each character from the end to the begining (reversed)

def lower_case(name):
    '''
    This takes the letter given and sees if it is capital. It then convets it to the number sequences and converts it from uppercase to lowercase.
    args:
        string(name): word/phrase that computer goes through each letter to change to lower case 
    returns:
        Name in all lower case
    '''
    name_out = ""
    for letter in name:
        if ord(letter)>64 and ord(letter)<91:        #Takes from the ascii table and checks to see if the letters are uppercase from the set of numbers given
            num = ord(letter)                        #converts letter into number to do the math
            num = num + 32                           #turns into lower case
            letter = chr(num)                        #connvert number to letter
            name_out = name_out + letter             #joins the letters together
        else:
            name_out = name_out + letter
    return name_out

def upper_case(name):
    '''
    Description: This takes the letter given and sees if it is lowercase. It then convets it to the number sequences and converts it from lowercase to uppercase.
    args:
        string(name): word/phrase that looks at the chart with each corresponding letter and number. If the letter is lower case it will then convert it to upper case.
    returns:
        The name in all upper case.
    '''
    name_out = ""
    for letter in name:
        if ord(letter) > 96 and ord(letter) < 123:   #Takes from the ascii table and checks to see if the letters are lowercase from the set of numbers given
            num = ord(letter)                        #converts letter into number to do the math
            num = num - 32                           #turns into upper case
            letter = chr(num)                        #converts number back to letter
            name_out = name_out + letter             #joins the letters together
        else:                                        #if character is upper case
            name_out = name_out + letter             #joins the letters together
    return name_out                                  #returns name in upper case

def hyphen_check(name):
    '''
    Description: Checks if hyphen is in last name
    args:  
        string(name): word/phrase that is being checked for "-"
    returns:
        true or false depending on if it contains "-"
    '''
    if "-" in name:
        return True
    else:
        return False

def is_palidrone(name):
    '''
    Description: Checks if the name given is the same as the reverse name from reverse function
    args:
        string(name): word/phrase that is being checked if its the same as reversed one
    returns:
        reutrns true or false
    '''
    if name == reverse_string(name):
        return True
    else:
        return False

def get_initials(name):
    '''
    Description: Takes the initials from the full name
    args:
        string(name): word/phrase that is split to get initials
    returns:
        returns the initials for the name previously selected 
    '''

    name = remove_title(name)
    name_list = get_names(name)    #goes to function get_names that creates a split so the names are split into arrays
    initials = ''
    #this finds the first character in the word, the name is already put into seperate arrays so it can get the intials
    for name in name_list:
        initials += name[0]
    return initials

def get_title(name):
    '''
    Description: From the list of titles it sees if they are in name
    args:
        string(name): word/phrase that is checked for titles
    returns:
        return: boolean depending if it contains title
    '''
    titles = ['Dr.', 'Sir', 'Esp', 'Ph.d']
    names = get_names(name)
    #if the titles from list are in the name it will return true, if not it will return false.
    for title in titles:
        if title in names:
            return True 
    return False
     
def remove_title(name):
    '''
    Description: This removes the title of a name
    Args:
        string(name): word/phrase
    returns:
        returns name without the title
    '''
    titles = ['Dr.', 'Sir', 'Esp', 'Ph.d']
    names = get_names(name)
    #if the titles from list are in the name it will remove the title and then return the name without the title
    for title in titles:
        if title in names:
            names.remove(title)
    return ' '.join(names)

def random_name(name):
    '''
    Description: Shuffles your name into new random name
    args:
        string(name): word/phrase that is convtered into a list which it then suffled
    returns:
        return: joins characters back together and returns a new shuffled name
    '''
    name = list(name)
    random.shuffle(name)     #shuffles characters
    return ''.join(name)     #joins back characters to make new name

def middle_name(fullname):
    '''
    takes middle name from finding the spaces
    args:
        string(fullname): word/phrase that is checked for spaces to determind middlename
    returns:
        return: middle name 
    '''
    fullname = remove_title(fullname)  #this calls the function remove_title to remove the title from the name 
    names = get_names(fullname)
    return ' '.join(names[1:-1])       #goes through each character from start and from end


def main():
    name = input("Enter your full name: ")


    while True:
        choice = input("Which function do you want to run? \n1. Reverses the name \n2. Counts vowels in name \n3. Counts consonant \n4. Returns first name \n5. Returns last name \n6. Returns name in lower case \n7. Returns name in upper case \n8. Checks for hyphen in last name \n9. Checks if name is palidrone \n10. Returns initials \n11. Checks if name contins title \n12. Mixes letters \n13. Returns middle name\nChoose a function: ")

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
        elif choice == '9':
            output = is_palidrone(name)
            print(output)
        elif choice == '10':
            output = get_initials(name)
            print(output)
        elif choice == '11':
            output = get_title(name)
            print(output)
        elif choice == '12':
            output = random_name(name)
            print(output)
        elif choice == '13':
            output = middle_name(name)
            print(output)
main()