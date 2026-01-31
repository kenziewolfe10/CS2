def display():
    '''
    Loads file and displays the first 10 rows
    args: none
    returns:
        return: the first 10 lines of the titanic CSV file
    '''

    try:
        with open('titanic.csv', 'r') as file:
            count = 0
            for line in file:
                row = line.strip().split(',')
                print(row)
                count += 1
                if count == 10:
                    break
    except FileNotFoundError:
        print("Error: 'titanic.csv' file not found.")
        

def survival_rate():  
    '''
    Calculates and prints overall survival rate
    Args:
        none
    returns:
        prints the total number of people and total survival rate
    '''
    with open('titanic.csv', 'r', newline = '') as file:
        next(file)
        survived = 0
        total = 0
        for line in file:
            row = line.strip().split(',')
            if row[1] == "1":
                survived += 1
                total += 1
            else:
                total += 1
        print(f'Survival rate: {survived/total*100:.2f}%')
        print(f'Total:{total}')

def gender_rate():
    '''
    Calculates the survival rate for males and females separately
    Args:
        none
    returns:
        Prints female and male survival rate as a percentage
    '''
    with open('titanic.csv', 'r', newline = '') as file:
        next(file)
        female = 0
        Ftotal= 0
        male = 0
        Mtotal = 0

        for line in file:
            row = line.strip().split(',')

            if row[5] == "female":
                if row[1] == "1":
                    female += 1
                Ftotal += 1
            elif row[5] == "male":
                if row[1] == "1":
                    male += 1
                Mtotal += 1
        print(f'Female survival rate: {female/Ftotal*100:.2f}%')
        print(f'Male survival rate: {male/Mtotal*100:.2f}%')



def age_survivor():
    '''
    Prints information based on age of passengers
    Args:
        none
    returns:
        Prints average age, average age of survivor and non-survivor
    '''
    with open('titanic.csv', 'r', newline = '') as file:
        next(file)
        SurvivorAge = []
        NonSurvivorAge = []
        ages = []

        for line in file:
            row = line.strip().split(',')
            if row[6] == "":
                continue
            if row[1] == "1":
                SurvivorAge.append(float(row[6]))
            else:
                NonSurvivorAge.append(float(row[6]))
            ages.append(float(row[6]))
        print(f'Average age: {sum(ages)/len(ages):.2f}')
        print(f'Average survivor age: {sum(SurvivorAge)/len(SurvivorAge):.2f}')
        print(f'Average non-survivor age: {sum(NonSurvivorAge)/len(NonSurvivorAge):.2f}')


def oldyoung_survivor():
    '''
    Gets the oldest and yougest survivor
    Args:
        none
    Returns:
        The oldest and youngest survivors name and age
    '''

    with open('titanic.csv', 'r', newline = '') as file:
        next(file)
        min_age = 200
        youngest = '' 
        oldest = ''
        max_age = -1

        for line in file:
            row = line.strip().split(',')
            if row[6] == '':
                continue
        

            if float(row[6]) > max_age:
                max_age = float(row[6])
                oldest = row[4] + row[3]
            elif float(row[6]) < min_age:
                min_age = float(row[6])
                youngest = row[4] + row[3]

        print(f"The youngest passenger was {youngest} at {min_age} years old")
        print(f"The oldest passenger was {oldest} at {max_age} years old")


def class_survivor():
    '''
    Gets the three classes average fair and survival rate
    Args:
        none
    Returns:
        Prints all three classes survival rates and average fairs
    '''
    with open('titanic.csv', 'r', newline = '') as file:
        next(file)
        class1 = 0
        class1survived = 0
        fair1 = 0
        class2= 0
        class2survived = 0
        fair2 = 0
        class3 = 0
        class3survived = 0
        fair3 = 0

        for line in file:
            row = line.strip().split(',')

            if row[2] == "1":
                if row[1] == "1":
                    class1 += 1
                class1survived += 1
                fair1 += float(row[10])
            elif row[2] == "2":
                if row[1] == "1":
                    class2 += 1
                class2survived += 1
                fair2 += float(row[10])
            elif row[2] == "3":
                if row[1] == "1":
                    class3 += 1
                class3survived += 1
                fair3 += float(row[10])

        print(f'First class survival rate: {class1/class1survived*100:.2f}%')
        print(f'Second class survival rate: {class2/class2survived*100:.2f}%')
        print(f'Third class survival rate: {class3/class3survived*100:.2f}%') 

        print(f'First class average fair: {fair1/class1:.2f}$')
        print(f'Second class average fair: {fair2/class2:.2f}$')
        print(f'Third class average fair: {fair3/class3:.2f}$')


def family_survivor():
    '''
    Calculates family size, how many people are in each family size, and the surivival rate of each family size.
    Args:
        none
    Returns:
        Prints how many people are in each family size and the surival rate of each family size
    '''
    with open('titanic.csv', 'r', newline = '') as file:
        next(file)

        family_sizes = {1: [0, 0]}

        for line in file:
            row = line.strip().split(',')
            family_size = int(row[7]) + int(row[8]) + 1
            
            if family_size == 1:
                family_sizes[1][0] += 1

                if row[1] == "1":
                    family_sizes[1][1] += 1
            elif family_size in list(family_sizes.keys()):
                family_sizes[family_size][0] += 1

                if row[1] == "1":
                    family_sizes[family_size][1] += 1
            else:
                if row[1] == "1":
                    family_sizes[family_size] = [1, 1]
                else:
                    family_sizes[family_size] = [1, 0]

    family_sizes = dict(sorted(family_sizes.items()))

    for family_size in family_sizes.keys():
        print(f'Family of {family_size}: Total - {family_sizes[family_size][0]}, Survival rate - {family_sizes[family_size][1]/family_sizes[family_size][0]*100:.2f}%')



def main():
    while True:
        choice = input("Which function would you like to run? \n1. Display the first 10 rows of the titanic file \n2. Get the survival rate and total passengers \n3. Get the survival rate based on gender \n4. Get the survival rate based on age \n5. Get the oldest and younger survivor \n6. Get survival rate based on class \n7. Analyze data based off family size \nEnter 1-7: ")

        if choice == '1':
            display()
        elif choice == '2':
            survival_rate()
        elif choice == '3':
            gender_rate()
        elif choice == '4':
            age_survivor()
        elif choice == '5':
            oldyoung_survivor()
        elif choice == '6':
            class_survivor()   
        elif choice == '7':
            family_survivor()     

main()
