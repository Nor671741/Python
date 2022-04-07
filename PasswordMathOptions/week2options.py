'''
Created on Aug 25, 2020
@author: nor67

An application with following menu options for users to
run at the command line:
a. Generate Secure Password
b. Calculate and Format a Percentage
c. How many days from today until July 4, 2025?
d. Use the Law of Cosines to calculate the leg of a triangle.
e. Calculate the volume of a Right Circular Cylinder
f. Exit program

'''
import string
import math
import secrets
from datetime import date
from math import pi

def options():
    '''presents user options and returns their choice.'''
    print('\na. Generate Secure Password \n\
b. Calculate and Format a Percentage \n\
c. How many days from today until July 4, 2025? \n\
d. Use the Law of Cosines to calculate the leg of a triangle. \n\
e. Calculate the volume of a Right Circular Cylinder \n\
f. Exit program \n')
    choice = str(input('Enter a letter from the menu options: '))

    #check valid entry
    while choice not in ('a', 'b', 'c', 'd', 'e', 'f'):
        print('Invalid Entry.')
        choice = str(input('Enter a, b, c, d, e, or f: '))
    return choice

def generate_pw():
    '''Prompt the user for the length of the password and complexity
    (i.e. Upper Case, Lower Case, Numbers, special characters). and
    generate a password of desired length and complexity.'''
    pw_length = int(input('Length of password? (8-20) '))
    #check valid entry
    while not 8 <= pw_length <= 20:
        print('Invalid Entry.')
        pw_length = int(input('Enter a length between 8-20: '))

    use_up_case = str(input('Use upper case letters? (yes/no) '))
    #check valid entry
    while use_up_case not in ('yes', 'no'):
        print('Invalid entry.\n Enter "yes" or "no". ')
        use_up_case = str(input('Use upper case letters? '))

    use_lo_case = str(input('Use lower case letters? (yes/no) '))
    #check valid entry
    while use_lo_case not in ('yes', 'no'):
        print('Invalid entry.\n Enter "yes" or "no". ')
        use_lo_case = str(input('Use lower case letters? '))

    use_number = str(input('Use numbers? (yes/no) '))
    #check valid entry
    while use_number not in ('yes', 'no'):
        print('Invalid entry.\n Enter "yes" or "no".')
        use_number = str(input('Use numbers? '))

    use_special = str(input('Use special characters? (yes/no) '))
    #check valid entry
    while use_special not in ('yes', 'no'):
        print('Invalid entry.\n Enter "yes" or "no". ')
        use_special = str(input('Use special characters? '))

    #if all options are no
    if use_up_case == 'no' and use_lo_case == 'no' and \
       use_number == 'no' and use_special == 'no':
        print('All options cannot be "no".\n')
        generate_pw()
    #if all options are yes
    if use_up_case == 'yes' and use_lo_case == 'yes' and \
       use_number == 'yes' and use_special == 'yes':
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for i in range(pw_length))
        print('\nCreated password: ' + password)
    #if all options are yes except upper case
    if use_up_case == 'no' and use_lo_case == 'yes' and \
       use_number == 'yes' and use_special == 'yes':
        alphabet = string.ascii_lowercase + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for i in range(pw_length))
        print('\nCreated password: ' + password)
    #if all options are yes except lower case
    if use_up_case == 'yes' and use_lo_case == 'no' and \
       use_number == 'yes' and use_special == 'yes':
        alphabet = string.ascii_uppercase + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for i in range(pw_length))
        print('\nCreated password: ' + password)
    #if all options are yes except numbers
    if use_up_case == 'yes' and use_lo_case == 'yes' and \
       use_number == 'no' and use_special == 'yes':
        alphabet = string.ascii_letters + string.punctuation
        password = ''.join(secrets.choice(alphabet) for i in range(pw_length))
        print('\nCreated password: ' + password)
    #if all options are yes except special characters
    if use_up_case == 'yes' and use_lo_case == 'yes' and \
       use_number == 'yes' and use_special == 'no':
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(pw_length))
        print('\nCreated password: ' + password)
    #if upper case and lowercase is no
    if use_up_case == 'no' and use_lo_case == 'no' and \
       use_number == 'yes' and use_special == 'yes':
        alphabet = string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for i in range(pw_length))
        print('\nCreated password: ' + password)
    #if upper case and numbers is no
    if use_up_case == 'no' and use_lo_case == 'yes' and \
       use_number == 'no' and use_special == 'yes':
        alphabet = string.ascii_lowercase + string.punctuation
        password = ''.join(secrets.choice(alphabet) for i in range(pw_length))
        print('\nCreated password: ' + password)
    #if upper case and special characters is no
    if use_up_case == 'no' and use_lo_case == 'yes' and \
       use_number == 'yes' and use_special == 'no':
        alphabet = string.ascii_lowercase + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(pw_length))
        print('\nCreated password: ' + password)
    #if upper case, lower case and number is no
    if use_up_case == 'no' and use_lo_case == 'no' and \
       use_number == 'no' and use_special == 'yes':
        alphabet = string.punctuation
        password = ''.join(secrets.choice(alphabet) for i in range(pw_length))
        print('\nCreated password: ' + password)
    #if lower case and numbers is no
    if use_up_case == 'yes' and use_lo_case == 'no' and \
       use_number == 'no' and use_special == 'yes':
        alphabet = string.ascii_uppercase + string.punctuation
        password = ''.join(secrets.choice(alphabet) for i in range(pw_length))
        print('\nCreated password: ' + password)
    #if lower case and special characters is no
    if use_up_case == 'yes' and use_lo_case == 'no' and \
       use_number == 'yes' and use_special == 'no':
        alphabet = string.ascii_uppercase + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(pw_length))
        print('\nCreated password: ' + password)
        #if lower case and special characters is no
    if use_up_case == 'yes' and use_lo_case == 'yes' and \
       use_number == 'no' and use_special == 'no':
        alphabet = string.ascii_uppercase + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(pw_length))
        print('\nCreated password: ' + password)
    #if only upper case is yes
    if use_up_case == 'yes' and use_lo_case == 'no' and \
       use_number == 'no' and use_special == 'no':
        alphabet = string.ascii_uppercase
        password = ''.join(secrets.choice(alphabet) for i in range(pw_length))
        print('\nCreated password: ' + password)
    #if only lower case is yes
    if use_up_case == 'no' and use_lo_case == 'yes' and \
       use_number == 'yes' and use_special == 'no':
        alphabet = string.ascii_lowercase
        password = ''.join(secrets.choice(alphabet) for i in range(pw_length))
        print('\nCreated password: ' + password)
    #if only numbers is yes
    if use_up_case == 'no' and use_lo_case == 'no' and \
       use_number == 'yes' and use_special == 'no':
        alphabet = string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(pw_length))
        print('\nCreated password: ' + password)
    #if only special characters is yes
    if use_up_case == 'no' and use_lo_case == 'no' and \
       use_number == 'no' and use_special == 'yes':
        alphabet = string.punctuation
        password = ''.join(secrets.choice(alphabet) for i in range(pw_length))
        print('\nCreated password: ' + password)
#generate_pw()
def calc_percentage():
    ''' the user has to enter the numerator and
    denominator and the number of decimal points for formatting.
    For example, 22, 57, 3 would yield 38.596 percent.'''
    numerator = (input('Enter the numerator: '))
    #check valid entry by trying to make input a float for calculations.
    try:
        numerator = float(numerator)
    except ValueError:
        print('Invalid entry.')
    while type(numerator) != float:
        numerator = (input('Enter the numerator (ex. 5.2): '))
        try:
            numerator = float(numerator)
        except ValueError:
            print('Invalid entry.')
#while not numerator.isnumeric():
#print('Invalid Entry.\n')
#numerator = (input('\nEnter an integer for the numerator (ex: 5): '))
#numerator = float(numerator)
    denominator = (input('Enter the denominator:'))
    #check valid entry by trying to make input a float for calculations.
    try:
        denominator = float(denominator)
    except ValueError:
        print('Invalid entry.')
    while type(denominator) != float:
        denominator = (input('Enter the denominator (ex. 5.2): '))
        try:
            denominator = float(denominator)
        except ValueError:
            print('Invalid entry.')
#while not denominator.isnumeric() or denominator == 0:
#print('Invalid Entry.\n')
#denominator = (input('Enter an integer for the denominator (ex: 10): '))
#denominator = float(denominator)
    decimals = (input('Enter the number of decimal points: '))
    #check valid entry by trying to make input an int for calculations.
    try:
        decimals = int(decimals)
    except ValueError:
        print('Invalid entry.')
    while type(decimals) != int:
        decimals = (input('Enter the decimals (ex. 5): '))
        try:
            decimals = int(decimals)
        except ValueError:
            print('Invalid entry.')
#while not decimals.isnumeric():
#print('Invalid Entry.\n')
#decimals = (input('Enter an integer for the denominator (ex: 10): '))
#decimals = int(decimals)

    #calculation
    percent = float(numerator/denominator)
    #round to decimal place as specified by user
    decimals += 2   #add 2 decimal places b/c it will change once formatted to percent.
    percent_deci_place = (round((percent), decimals)) * 100
    #print percentage and format final answer as a percent
    print('\nPercentage is ' + str(percent_deci_place) + '%')
#'{:.2%}'.format(percent_deci_place))
#I tried to use the formatting, but could not figure out how to specify from user.
#calc_percentage()

def days_to_7425():
    '''For days until July 4, 2025 the output should just be the number of days.
    There would be no input other than the selection from the menu.'''
    today = date.today()
    date_7425 = date(2025, 7, 4)
    #calculate the number of days
    time_to_7425 = abs(date_7425 - today)
    print('\nThe number of days to July 4th 2025 from today is: ' + str(time_to_7425.days))

def calc_tri_leg():
    '''Uses the Law of Cosines to calculate the leg of a triangle
    The Law of Cosines says:    c^2 = a^2 + b^2 - 2ab cos(C)'''
    side_1 = (input('\nEnter length of one side of the triangle: '))
    #check valid entry by trying to make input a float for calculations.
    try:
        side_1 = float(side_1)
    except ValueError:
        print('Invalid entry.')
    while type(side_1) != float:
        side_1 = (input('Enter the length of one side (ex. 5.2): '))
        try:
            side_1 = float(side_1)
        except ValueError:
            print('Invalid entry.')
#while not side_1.isnumeric():
#print ('Invalid Entry')
#side_1 = (input('Enter length of one side of the triangle: '))
#side_1 = float(side_1)
    side_2 = (input('Enter the length of the other side of the triangle: '))
    #check valid entry by trying to make input a float for calculations.
    try:
        side_2 = float(side_2)
    except ValueError:
        print('Invalid entry.')
    while type(side_2) != float:
        side_2 = (input('Enter the length of the other side (ex. 5.2): '))
        try:
            side_2 = float(side_2)
        except ValueError:
            print('Invalid entry.')
#while not side_2.isnumeric():
#print('Invalid Entry')
#side_2 = (input('Enter the length of \
#the other side of the triangle: (ex. 4 or 4.12): '))
#side_2 = float(side_2)
    angle = (input('Enter the angle between the sides in degrees: '))
    #check valid entry by trying to make input a float for calculations.
    try:
        angle = float(angle)
    except ValueError:
        print('Invalid entry.')
    while type(angle) != float or not 0 < angle < 180:
        angle = (input('Enter the angle between sides in degrees (ex. 5.2): '))
        try:
            angle = float(angle)
        except ValueError:
            print('Invalid entry.')
#while not 0 < angle < 180:
#print('Invalid Entry')
#angle = float(input('Enter the angle in degrees (0-180): '))
    #converts angle from degrees to radians for the cos function.
    angle = math.radians(angle)
    #calculate 3rd side. Each part broken to smaller parts and then rounded to 3 decimal places.
    a_squared = side_1**2
    b_squared = side_2**2
    ab2_cos_angle = (2 * side_1 * side_2 * math.cos(angle))
    c_result = math.sqrt(a_squared + b_squared - ab2_cos_angle)
    c_result = round(c_result, 3)
    print('\nThe length of the 3rd side of the triangle is: ' + str(c_result))

def calc_cylinder_vol():
    '''Volume of Circular Cylinder = (πr^2) × Height'''
    radius = (input('Enter the radius: '))
    #check valid entry by trying to make input a float for calculations.
    try:
        radius = float(radius)
    except ValueError:
        print('Invalid entry.')
    while type(radius) != float:
        radius = (input('Enter the radius (ex. 5.2): '))
        try:
            radius = float(radius)
        except ValueError:
            print('Invalid entry.')
#while not radius.isnumeric():
#print('Invalid entry.')
#radius = (input('Enter the radius. ex: 5 or 5.12'))
#radius = float(radius)
    height = (input('Enter the height: '))
    #check valid entry by trying to make input a float for calculations.
    try:
        height = float(height)
    except ValueError:
        print('Invalid entry.')
    while type(height) != float:
        height = (input('Enter the height (ex. 5.2): '))
        try:
            height = float(height)
        except ValueError:
            print('Invalid entry.')
#while not height.isnumeric():
#print('Invalid entry.')
#height = (input('Enter the height. ex: 5 or 5.12'))
#height = float(height)
    #calculation of volume
    result_cyl_vol = (pi * radius**2) * height
    result_cyl_vol = round(result_cyl_vol, 3)
    print('\nThe volume of the cylinder is ' +str(result_cyl_vol))
#calc_cylinder_vol()

def exit_options():
    '''exit message'''
    print('\nThank you for visiting. Good day.')

#recalls options() until user chooses 'f' to exit
CHOICE = options()
while CHOICE != ('f'):
    if CHOICE == 'a':
        generate_pw()
        #print('a')
        #CHOICE = options()
    elif CHOICE == 'b':
        calc_percentage()
        #print('b')
        #CHOICE = options()
    elif CHOICE == 'c':
        days_to_7425()
        #print('c')
        #CHOICE = options()
    elif CHOICE == 'd':
        calc_tri_leg()
        #print('d')
        #CHOICE = options()
    elif CHOICE == 'e':
        calc_cylinder_vol()
        #print('e')
    #recursive call for custom function options()
    CHOICE = options()

if CHOICE == 'f':
    exit_options()
