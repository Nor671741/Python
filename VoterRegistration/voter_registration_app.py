'''
Professor Cohen,
I'd appreciate any feedback on how to reuse code, instead of typing over
and over, and if there are any ways to write the code better.
Thank you.

Created on Aug 20, 2020

@author: nor67

A voter registration application asking the user a few simple questions
followed by a confirmation of registration, provided the user is eligible.
'''
# welcome statement to application
print('WELCOME TO THE PYTHON VOTER REGISTRATION APPLICATION\n')
#declare value for variable CITIZEN and AGE
CITIZEN = str('null')
AGE = int(-1)

# obtain information from user and store
TO_VOTE = str(input('Do you want to continue with Voter Registration? '))

# check answer is valid: either yes or no.
while TO_VOTE not in ('yes', 'no'):
    print('Invalid entry.\n Enter "yes" or "no".')
    TO_VOTE = str(input('Do you want to continue with Voter Registration? '))

# if the user continues to register, obtain all information.
#first name
if TO_VOTE == 'yes':
    FIRST_NAME = str(input('What is your first name? '))
    while not FIRST_NAME.isalpha(): #check FIRST_NAME is letters
        print('Invalid entry.')
        FIRST_NAME = str(input('What is your first name? '))
    TO_VOTE = str(input('Continue with Voter Registration? '))
    # check answer is valid: either yes or no.
    while TO_VOTE not in ('yes', 'no'):
        print('Invalid entry.\n Enter "yes" or "no".')
        TO_VOTE = str(input('Do you want to continue with Voter Registration? '))

# last name
if TO_VOTE == 'yes':
    LAST_NAME = str(input('What is your last name? '))
    while not LAST_NAME.isalpha(): #check last name is letters
        print("Invalid entry.")
        LAST_NAME = str(input('What is your last name? '))
    TO_VOTE = str(input('Continue with Voter Registration? '))

    # check answer is valid: either yes or no.
    while TO_VOTE not in ('yes', 'no'):
        print('Invalid entry.\n Enter "yes" or "no".')
        TO_VOTE = str(input('Do you want to continue with Voter Registration? '))

#AGE
if TO_VOTE == 'yes':
    AGE = int(input('What is your age? '))

while not 0 < AGE < 120: #check if AGE is a valid AGE
    print('Invalid Entry.')
    AGE = int(input('What is your age? '))
if AGE < 18:
    print('Thank you for trying the Voter Registration Application.\n\
Unfortunately, you are not eligible to vote at this time.\nGood day.')
else:
    O_VOTE = str(input('Continue with Voter Registration? '))

    # check answer is valid: either yes or no.
    while TO_VOTE not in ('yes', 'no'):
        print('Invalid entry.\n Enter "yes" or "no".')
        TO_VOTE = str(input('Do you want to continue with Voter Registration? '))

#CITIZEN
if AGE >= 18 and TO_VOTE == 'yes':
    CITIZEN = str(input('Are you a U.S. citizen? '))
    while CITIZEN not in ('yes', 'no'):  #check answer is yes or no
        print('Invalid entry.\n Enter "yes" or "no".')
        CITIZEN = str(input('Are you a U.S. citizen? '))
    if CITIZEN == 'no':
        print('Thank you for trying the Voter Registration Application.\n\
Unfortunately, you are not eligible to vote at this time.\nGood day.')
    else:
        TO_VOTE = str(input('Continue with Voter Registration? '))
        # check answer is valid: either yes or no.
        while TO_VOTE not in ('yes', 'no'):
            print('Invalid entry.\n Enter "yes" or "no".')
            TO_VOTE = str(input('Do you want to continue with Voter Registration? '))

#residence state
if AGE >= 18 and TO_VOTE == 'yes' and CITIZEN == 'yes':
    RESIDENCE_STATE = str(input('What state do you live? '))
    while RESIDENCE_STATE not in('AK', 'AL', 'AR', 'AS', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL',
                                 'GA', 'GU', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA',
                                 'MD', 'ME', 'MI', 'MN', 'MO', 'MP', 'MS', 'MT', 'NA', 'NC', 'ND',
                                 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR',
                                 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VI', 'VT', 'WA', 'WI',
                                 'WV', 'WI'):
        print('Invalid entry.')
        RESIDENCE_STATE = str(input('What state do you live in? (ex: AK) '))
    TO_VOTE = str(input('Continue with Voter Registration? '))

    # check answer is valid: either yes or no.
    while TO_VOTE not in ('yes', 'no'):
        print('Invalid entry.\n Enter "yes" or "no".')
        TO_VOTE = str(input('Do you want to continue with Voter Registration? '))

#ZIPCODE
if AGE >= 18 and TO_VOTE == 'yes' and CITIZEN == 'yes':
    ZIPCODE = str(input('What is your zipcode? '))

    print('\nThanks for registering to vote.\n\
     Information received:\n\
     Name: ' + FIRST_NAME, LAST_NAME + '\n\
     AGE: ' + str(AGE) + '\n\
     U.S. citizen: ' + CITIZEN + '\n\
     State: ' + RESIDENCE_STATE + '\n\
     Zipcode: ' + str(ZIPCODE))

# if-else logic for voter registration
if AGE >= 18 and TO_VOTE == 'yes' and CITIZEN == 'yes':
    print('\nYour voting registration is complete.\n\
Your voter registration card should be shipped within 3 weeks.')

# while the user does not what to continue to register
if TO_VOTE == 'no':
    print('Thank you for trying the Voter Registration Application.\n\
You are not registered to vote.\nGood day.')
