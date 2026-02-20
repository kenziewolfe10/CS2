import operator
import csv

def open_csv(word_dictionary, csv_file):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Key', 'Value'])
            
        for key, value in word_dictionary.items():
            writer.writerow([key, value])

    print(f"Dictionary saved to {csv_file}")

def count_words(filename, output):
    word_dictionary = {}
    excluded_words = ["and", "or", "i", "but", "the", "of", "a", "to", "that", "is", "my", "it"]    #a list of words that should not be included in the dictionary

    try:
        with open(filename, 'r') as file:                        
            for line in file:                                         
                row = line.strip().split()                            #splits the words into seperate indexs by seperating from each space
                
                for w in row:                                         #for each index in a row
                    w = w.lower()                                     #converts the index to all lower case 
                    
                    if w in word_dictionary:                          #if the index is in the dictionary created 
                        word_dictionary[w] += 1                       #add a count of 1 to the index
                    elif w in excluded_words:                         #else if the word is an excluded value
                        continue                                      #continue and do not add to list
                    else:                                             #if the word is not already in the dictionary
                        word_dictionary[w] = 1                        #add the index to the dictionary and set it equal to 1

            extra_words = []                                          #makes a list of words that are the words above a count of 5
            
            for key,value in word_dictionary.items():                 #for each key with a vlaue in the dictionary
                if value <= 5:                                       #if the word is below a count of 5
                    extra_words.append(key)                           #add to the list of extra_words

            for word in extra_words:                                  #for the words in the list of extra words
                word_dictionary.pop(word)                             #remove them from the dictionary

            sorted_dict = dict(sorted(word_dictionary.items(), key=lambda item: item[1], reverse=True)) #sort dictionary by value, items with the greatest value to the least
            print(sorted_dict)                                        #prints the dictonary 

            open_csv(sorted_dict, output)


    except FileNotFoundError:
        print(f"Error: {filename} file not found.")
count_words('Macbeth.txt', 'Macbeth.csv')
count_words('Romeo and Juliet.txt', 'Romeo and Juliet.csv')