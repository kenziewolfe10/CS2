'''
Author: Mackenzie Wolfe
Due Date: 10/23/2025
Bugs: None
Sources: W3Schools
'''

def get_type(length, height, thickness):
    '''
    Description: Takes the length, height, and thickness and determinds the type of mailing shipping
    Args:
        length(float): The length of the package
        height(float): The height of the package
        thickness(float): The thickness of the package
    Return:
        returns the type of mailing shipping
    '''
    if 3.5 <= length <= 4.25 and 3.5 <= height <= 6 and .007 <= thickness <= .016:
        return 'regular post card'
    elif 4.25 <= length <= 6 and 6 <= height <= 11.5 and .007 <= thickness <= .015:
        return 'large post card'
    elif 3.5 <= length <= 6.125 and 5 <= height <= 11.5 and .016 <= thickness <= .25:
        return 'envelope'
    elif 6.125 <= length <= 24 and 11 <= height <= 18 and .25 <= thickness <= .5:
        return 'large envelope'
    elif length > 24 or height > 18 or thickness > .5 and length + 2*(height + thickness) <= 84:
        return 'package'
    elif length > 24 or height > 18 or thickness > .5 and 84 <= length + 2*(height + thickness) <= 130:
        return 'large package'
    else:
        return 'unmailable'

def get_zone(zipcode):
    '''
    Description: This takes the zipcode from the start and end place and determinds the start and end zone
    Args:
        zipcode(int): zipcode of start and end place
    Returns:
        Returns which zone the zipcode is apart of 
    
    '''
    if 1 <= zipcode <= 6999:
        return 1
    elif 7000 <= zipcode <= 19999:
        return 2 
    elif 20000 <= zipcode <= 35999:
        return 3
    elif 36000 <= zipcode <= 62999:
        return 4
    elif 63000 <= zipcode <= 84999:
        return 5
    elif 85000 <= zipcode <= 99999:
        return 6
    else:
        return -1
    
def get_distance(startzip, endzip):
    '''
    Description: This gets the zones from the start and end point and then subtracts them, finding how many zones it goes through
    Args:
        Startzip(int): start zipcode
        Endzip(int): end zipcode 
    Returns:
        Returns the number of zones the mail goes through
    '''
    startzone = get_zone(startzip)
    endzone = get_zone(endzip)

    if startzone == -1 or endzone == -1:
        return 'unmailable'
    return abs(endzone - startzone)

def get_cost(post_type, distance):
    '''
    Descrption: This determinds the cost depending on postcard type and distance
    Args:
        post_type(str): The type of postcard
        distance(int): The number of zones it goes through
    Returns:
        returns the cost 
    '''
    if post_type == 'unmailable' or distance == 'unmailable':
        return 'unmailable'
    elif post_type == 'regular post card':
        return .2 + .03*distance
    elif post_type == 'large post card':
        return .37 + .03*distance
    elif post_type == 'envelope':
        return .37 + .04*distance
    elif post_type == 'large envelope':
        return .6 + .05*distance
    elif post_type == 'package':
        return 2.95 + .25*distance
    elif post_type == 'large package':
        return 3.95 + .35*distance

def main():
    while True:
        data = input("Input your mailing data(length, height, thickness, startzip, endzip): ")
        data = data.split(",")
        length = float(data[0])
        height = float(data[1])
        thickness = float(data[2])
        startzip = int(data[3])
        endzip = int(data[4])
        
        post_type = get_type(length, height, thickness)
        distance = get_distance(startzip, endzip)
        cost = get_cost(post_type, distance)

        if cost == 'unmailable':
            print('unmailable')
        else:
            cost = f'{cost:.2f}'                              #this prints 2 decimal places in the output
            cost = cost.lstrip("0")                           #lstrip removes the 0 before the decimal in the output cost
            print(cost)
main()    
