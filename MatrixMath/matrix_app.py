'''
Created on Sep 10, 2020
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: nor67
'''
#import pandas as pd
import re
import numpy as np

#FUNCTIONS
def menu():
    '''presents user options and returns their choice.'''
    choice = str(input('Do you want to play the Matrix game? (yes or no)\n'))

    #check valid entry
    while choice not in ('yes', 'no'):
        print('Invalid Entry.')
        choice = (input('Enter yes or no: '))
    return choice

def calculation(matrix_1, matrix_2, operation):
    '''receive three matrix inputs and calculates desired operation:  Addition, Subtraction
    Matrix Multiplication or Element by element multiplication and returns the resulting matrix.'''
    if operation == 'addition':
        result = np.add(matrix_1, matrix_2)
    if operation == 'subtraction':
        result = np.subtract(matrix_1, matrix_2)
    if operation == 'matrix multiplication':
        result = np.multiply(matrix_1, matrix_2)
    if operation == 'element by element multiplication':
        result = np.multiply(matrix_1, matrix_2)
    return result

def get_phone():
    '''ask user for phone number and validate input is a phone number'''
    phone_format = False
    while not phone_format:
        fone = input('Enter your phone number (XXX-XXX-XXXX):\n')
        #regular expression author: Don Johnston on www.regexlib.com
        if re.fullmatch(r'^(?:\([2-9]\d{2}\)\ ?|[2-9]\d{2}(?:\-?|\ ?))[2-9]\d{2}[- ]?\d{4}$', fone):
            phone_format = True
        else:
            print('Your phone number is not in correct format. Please re-enter.')

def get_zipcode():
    ''''ask user for zipcode and validate input is a zipcode'''
    zip_format = False
    while not zip_format:
        zipcode = input('Enter your zipcode (XXXXX-XXXX):\n')
        #regular expression author Justin Elsburry on www.regexlib.com
        if re.fullmatch(r'^(?!0{5})(\d{5})(?!-?0{4})(-?\d{4})?$', zipcode):
            zip_format = True
        else:
            print('Your zipcode is not in correct format. Please re-enter.')

def get_matrix(number):
    '''ask user for matrix 1 and validate input for matrix'''
    while True:
        try:
            print('Enter the ' + number + ' 3 x 3 matrix: ')

            #row_1 transformation from string>list of strings>array of strings>int array
            row_1 = input()
            row_1 = row_1.split(' ')
            #validate row has 3 values
            while len(row_1) != 3:
                print('Invalid entry. Please reenter (X X X).')
                row_1 = input()
                row_1 = row_1.split(' ')
            row_1 = np.array(row_1)
            row_1 = row_1.astype(np.int)

            #row_2 transformation from string>list of strings>array of strings>int array
            row_2 = input()
            row_2 = row_2.split(' ')
            #validate row has 3 values
            while len(row_2) != 3:
                print('Invalid entry. Please reenter (X X X).')
                row_2 = input()
                row_2 = row_2.split(' ')
            row_2 = np.array(row_2)
            row_2 = row_2.astype(np.int)

            #row_3 transformation from string>list of strings>array of strings>int array
            row_3 = input()
            row_3 = row_3.split(' ')
            #validate row has 3 values
            while len(row_3) != 3:
                print('Invalid entry. Please reenter (X X X).')
                row_3 = input()
                row_3 = row_3.split(' ')
            row_3 = np.array(row_3)
            row_3 = row_3.astype(np.int)
            break
        except ValueError:
            print('Invalid entry. Please reenter.')

    # create first matrix with extra precaution for array type
    matrix = np.array([row_1, row_2, row_3], dtype=int)
    return matrix

def print_matrix(number, matrix):
    ''''print out matrix '''
    print(number + ' 3 x 3 matrix is: ')
    for row in matrix:
        for column in row:
            print(column, end=' ')
        print()

def get_operation():
    '''menu for matrix operation'''
    print('Select a Matrix Operation from the list below: \n\
            a. Addition\n\
            b. Subtraction\n\
            c. Matrix Multiplication\n\
            d. Element by element multiplication\n')
    matrix_op = input()

    #check valid entry
    while matrix_op not in ('a', 'b', 'c', 'd'):
        print('Invalid Entry.')
        matrix_op = (input('Enter a, b, c, or d: '))

    #transform input to operation name for print output and calculation
    if matrix_op == 'a':
        matrix_op = 'addition'
    if matrix_op == 'b':
        matrix_op = 'subtraction'
    if matrix_op == 'c':
        matrix_op = 'matrix multiplication'
    if matrix_op == 'd':
        matrix_op = 'element by element multiplication'
    return matrix_op

def matrix_game():
    '''User to enters their phone number and zipcode+4, which is validated. Then the user
    will enter values of two, 3x3 matrices and then select from options including, addition,
    subtraction, matrix multiplication, and element by element multiplication. The program should
    compute the appropriate results and return the results, the transpose of the results, the mean
    of the rows for the results, and the mean of the columns for the results.'''

    get_phone()
    get_zipcode()
    matrix_1 = get_matrix('first')
    print_matrix('Your first', matrix_1)
    matrix_2 = get_matrix('second')
    print_matrix('Your second', matrix_2)
    matrix_op = get_operation()

    #CALCULATIONS
    main_result = calculation(matrix_1, matrix_2, matrix_op)
    #takes resulting matrix and transposes
    t_result = main_result.T
    #takes resulting matrix and calculates the mean of the row
    row_mean = main_result.mean(axis=1)
    #takes resulting matrix and calculates the mean of the column
    column_mean = main_result.mean(axis=0)

    print('You selected ' + matrix_op + '. The results are:')
    #print out main_result
    for row in main_result:
        for column in row:
            print(column, end=' ')
        print()

    #print out the transpose of main_result
    print('\nThe Transpose is:')
    for row in t_result:
        for column in row:
            print(column, end=' ')
        print()

    #print out the row and column mean values
    print('\nThe row and column mean values of the results are: \nRow: ')
    for value in row_mean:
        print(f'{value:.2f}', end='  ')
    print('\nColumn: ')
    for value in column_mean:
        print(f'{value:.2f}', end='  ')
    print()
    print()
#matrix_game()

def exit_matrix():
    '''exit message'''
    print('Thank you for visiting the Python Matrix Application. Good day.')


def main():
    '''MAIN: calls menu() until user chooses '5' to exit'''
    print('\n' + '*' * 10 + 'WELCOME TO THE PYTHON MATRIX APPLICATION' + '*' *10 + '\n')
    choice = menu()
    while choice != 'no':
        matrix_game()
        choice = menu()
    if choice == 'no':
        exit_matrix()

    #recursive call for menu()
    #choice = menu()

#call to run main function
if __name__ == "__main__":
    main()
