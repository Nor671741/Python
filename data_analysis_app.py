'''
Created on Sep 17, 2020
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: nor67
'''

import pandas as pd      #This is used to load .csv files
import matplotlib.pyplot as plt  #This is used for plotting histograms for data

def main_menu():
    '''main menu for data_analysis_app'''
    print('MAIN MENU:\n\
    Select the file you want to analyze:\n\
    1. Population Data\n\
    2. Housing Data\n\
    3. Exit the Program\n')
    choice = input()

    #check valid entry
    while choice not in ('1', '2', '3'):
        print('Invalid Entry.')
        choice = (input('Enter 1, 2, or 3: '))
    return choice

def population_menu():
    '''display columns of PopChange file to analyze'''
    print('You are in the Population Data menu.\n\
    Select the Column you want to analyze:\n\
    a. Pop Apr 1\n\
    b. Pop Jul 1\n\
    c. Change Pop\n\
    d. Exit Population Data\n')
    pop_choice = input()

    #validate input for pop_choice
    while pop_choice not in ('a', 'b', 'c', 'd'):
        print('Invalid Entry.')
        pop_choice = (input('Enter a, b, c, or d: '))
    return pop_choice

def analyze_column(file, column):
    '''analyze column in file'''
    column_stats(file, column)
    display_histogram(file, column)

    #go back to previous menu
    if file == 'PopChange':
        run_pop_data()
    if file == 'Housing':
        run_housing_data()

def read_file(file):
    '''reads file and returns dataframe'''
    dataframe = pd.read_csv(file)
    return dataframe

def column_stats(file, column):
    '''displays stats for user selected column'''
    dataframe = read_file(file)
    count = dataframe[column].count()
    mean = dataframe[column].mean()
    std = dataframe[column].std()
    minimum = dataframe[column].min()
    maximum = dataframe[column].max()
    print('Analysis of column, '+ column + ':\n' +
          'Count: ' + str(count.round(2)) + '\n' +
          'Mean: ' + str(mean.round(2)) + '\n' +
          'Standard Deviation: ' + str(std.round(2)) + '\n' +
          'Minimum: ' + str(minimum.round(2)) + '\n' +
          'Maximum: ' + str(maximum.round(2)))

def display_histogram(file, column):
    '''display histogram of user selected file and column'''
    print('\nThe Histogram of column, ' + column + ', is now displayed.')
    print('Please exit the histogram window to continue.\n')
    dataframe = read_file(file)
    minimum = dataframe[column].min()
    maximum = dataframe[column].max()
    bins = 50
    plt.hist(dataframe[column], edgecolor='black', log=True, density=True, bins=bins)
    plt.ylabel('Probability')
    plt.title(column.upper())
    plt.xlim(minimum, maximum)
    plt.show()

def exit_column(file_name):
    '''exit file menu and go to main menu'''
    print('You selected to exit the '+ file_name + ' menu.\n')
    main()

def run_pop_data():
    '''asks user which column to analyze in PopChange file and analyzes'''
    pop_choice = population_menu()
    while pop_choice != 'd':
        if pop_choice == 'a':
            analyze_column('PopChange.csv', 'Pop Apr 1')
        if pop_choice == 'b':
            analyze_column('PopChange.csv', 'Pop Jul 1')
        if pop_choice == 'c':
            analyze_column('PopChange.csv', 'Change Pop')
        pop_choice = population_menu()

    if pop_choice == 'd':
        exit_column('Population Data')

def house_menu():
    '''menu for file Housing'''
    print('You are in the Housing Data menu.\n\
    Select the Column you want to analyze:\n\
    a. AGE\n\
    b. BEDRMS\n\
    c. BUILT\n\
    d. ROOMS\n\
    e. UTILITY\n\
    f. NUNITS\n\
    g. WEIGHT\n\
    h. Exit Housing Data')
    housing_choice = input()

    #validate input for housing_choice
    while housing_choice not in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'):
        print('Invalid Entry.')
        housing_choice = (input('Enter a, b, c, d, e, or f: '))
    return housing_choice

def run_housing_data():
    '''asks user which column to analyze in Housing file and analyzes'''
    house_choice = house_menu()
    while house_choice != 'h':
        if house_choice == 'a':
            analyze_column('Housing.csv', 'AGE')
        if house_choice == 'b':
            analyze_column('Housing.csv', 'BEDRMS')
        if house_choice == 'c':
            analyze_column('Housing.csv', 'BUILT')
        if house_choice == 'd':
            analyze_column('Housing.csv', 'ROOMS')
        if house_choice == 'e':
            analyze_column('Housing.csv', 'UTILITY')
        if house_choice == 'f':
            analyze_column('Housing.csv', 'NUNITS')
        if house_choice == 'g':
            analyze_column('Housing.csv', 'WEIGHT')
        house_choice = house_menu()

    if house_choice == 'h':
        exit_column('Housing Data')

def exit_data_ap():
    '''prints exit message'''
    print('\n' + '*' * 10 +'Thanks for using the Data Analysis App. Good Day.' + '*' *10 + '\n')

def main():
    '''MAIN: calls menu() until user chooses '3' to exit'''
    choice = main_menu()
    if choice == '1':
        run_pop_data()
    elif choice == '2':
        run_housing_data()
    elif choice == '3':
        exit_data_ap()
    else:
        choice = main_menu()



#call to run main function
if __name__ == "__main__":
    print('\n' + '*' * 10 + 'Welcome to the Python Data Analysis App' + '*' *10 + '\n')
    main()
