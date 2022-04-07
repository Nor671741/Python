'''
Created on Sep 4, 2020

@author: nor67
'''
import matplotlib.pyplot as plt
from PIL import Image



#LIST OF US STATES
us_states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado',
             'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho',
             'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana',
             'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
             'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',
             'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma',
             'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
             'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia',
             'Wisconsin', 'Wyoming']

#dictionary of US Capitals
us_capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona':'Phoenix',
    'Arkansas':'Little Rock',
    'California': 'Sacramento',
    'Colorado':'Denver',
    'Connecticut':'Hartford',
    'Delaware':'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinios': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Monies',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Neveda': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhoda Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakoda': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}

#dictionary of us states and populations
us_population = {
    'Alabama': 4908620,
    'Alaska': 734002,
    'Arizona': 7378490,
    'Arkansas': 3039000,
    'California': 39937500,
    'Colorado': 5845530,
    'Connecticut': 3563080,
    'Delaware':982895,
    'Florida': 21993000,
    'Georgia': 10736100,
    'Hawaii': 1412690,
    'Idaho': 1826160,
    'Illinios': 12659700,
    'Indiana': 6745350,
    'Iowa': 3179850,
    'Kansas': 2910360,
    'Kentucky': 4499690,
    'Louisiana': 4645180,
    'Maine': 1345790,
    'Maryland': 6803807,
    'Massachusetts': 6976600,
    'Michigan': 10045000,
    'Minnesota': 5700670,
    'Mississippi': 2989260,
    'Missouri': 6169270,
    'Montana': 1086760,
    'Nebraska': 1952570,
    'Neveda': 3139660,
    'New Hampshire': 1371250,
    'New Jersey': 8936570,
    'New Mexico': 2096640,
    'New York': 19440500,
    'North Carolina': 10611900,
    'North Dakota': 761723,
    'Ohio': 11747700,
    'Oklahoma': 3954820,
    'Oregon': 4301090,
    'Pennsylvania': 12820900,
    'Rhoda Island': 1056160,
    'South Carolina': 5210100,
    'South Dakoda': 903027,
    'Tennessee': 6897580,
    'Texas': 29472300,
    'Utah': 3282120,
    'Vermont': 628061,
    'Virginia': 8626210,
    'Washington': 7797100,
    'West Virginia': 1778070,
    'Wisconsin': 5851750,
    'Wyoming': 567025
}

#dictionary of us states and flowers
us_flowers = {
    'Alabama':'Camellia',
    'Alaska':'Forget Me Not',
    'Arizona':'Saguaro Cactus Blossom',
    'Arkansas':'Apple Blossom',
    'California': 'California Poppy',
    'Colorado':'White and Lavender Columbine',
    'Connecticut':'Mountain Laurel',
    'Delaware':'Peach Blossom',
    'Florida': 'Orange Blossom',
    'Georgia': 'Cherokee Rose',
    'Hawaii': 'Hibiscus',
    'Idaho': 'Syringa',
    'Illinios': 'Purple Violet',
    'Indiana': 'Peony',
    'Iowa': 'Wild Prairie Rose',
    'Kansas': 'Sunflower',
    'Kentucky': 'Goldenrod',
    'Louisiana': 'Magnolia',
    'Maine': 'White Pine Cone and Tassel',
    'Maryland': 'Black-Eyed Susan',
    'Massachusetts': 'Mayflower',
    'Michigan': 'Apple Blossom',
    'Minnesota': 'Pink and White Lady Slipper',
    'Mississippi': 'Magnolia',
    'Missouri': 'White Hawthorn Blossom',
    'Montana': 'Bitterroot',
    'Nebraska': 'Goldenrod',
    'Neveda': 'Sagebrush',
    'New Hampshire': 'Purple Lilac',
    'New Jersey': 'Violet',
    'New Mexico': 'Yucca Flower',
    'New York': 'Rose',
    'North Carolina': 'Dogwood',
    'North Dakota': 'Wild Prairie Rose',
    'Ohio': 'Scarlet Carnation',
    'Oklahoma': 'Mistletoe',
    'Oregon': 'Oregon Grape',
    'Pennsylvania': 'Mountain Laurel',
    'Rhoda Island': 'Violet',
    'South Carolina': 'Yellow Jessamine',
    'South Dakoda': 'Pasque Flower',
    'Tennessee': 'Iris',
    'Texas': 'Bluebonnet',
    'Utah': 'Sego Lily',
    'Vermont': 'Red Clover',
    'Virginia': 'Dogwood',
    'Washington': 'Pink Rhododendron',
    'West Virginia': 'Rhododendron',
    'Wisconsin': 'Wood Violet',
    'Wyoming': 'Indian Paintbrush'
}

#dictionary of images of flowers
flower_img = {
    'Alabama': 'alabamba_camellia.jpg',
    'Alaska': 'alaska_forgetmenot.jpg',
    'Arizona':'arizona_saguarocactusblossom.jpg',
    'Arkansas':'arkansas_appletreeblossomflower.jpg',
    'California': 'california_californiapoppy.jpg',
    'Colorado':'colorado_columbine.jpg',
    'Connecticut':'connecticut_mountainlaural.jpg',
    'Delaware':'delaware_peachblossom.jpg',
    'Florida': 'florida_0rangeblossom.jpg',
    'Georgia': 'georgia_cherokeerose.jpg',
    'Hawaii': 'hawaii_hibiscus.jpg',
    'Idaho': 'idaho_syringa.jpg',
    'Illinios': 'illinois_purpleviolet.jpg',
    'Indiana': 'indiana_peony.jpg',
    'Iowa': 'iowa_wildprairierose.jpg',
    'Kansas': 'kansas_sunflower.jpg',
    'Kentucky': 'kentuky_goldenrod.jpg',
    'Louisiana': 'louisiana_magnolia.jpg',
    'Maine': 'maine_whitepineconeandtassel.jpg',
    'Maryland': 'maryland_black-eyedsusan.jpg',
    'Massachusetts': 'massachusettes_mayflower.jpg',
    'Michigan': 'michigan_appleblossom.jpg',
    'Minnesota': 'minnesota_pinkwhiteladyslipper.jpg',
    'Mississippi': 'mississippi_magnolia.jpg',
    'Missouri': 'missouri_whitehawthornblossom.jpg',
    'Montana': 'montana_bitterroot.jpg',
    'Nebraska': 'nebraska_goldenrod.jpg',
    'Neveda': 'nevada_sagebrush.jpg',
    'New Hampshire': 'newhampshire_purplelilac.jpg',
    'New Jersey': 'newjersey_violet.jpg',
    'New Mexico': 'newmexico_yucca.jpg',
    'New York': 'newyork_rose.jpg',
    'North Carolina': 'northcarolina_dogwood.jpg',
    'North Dakota': 'northdakota_wildprairierose.jpg',
    'Ohio': 'ohio_scarleycarnation.jpg',
    'Oklahoma': 'oklahoma_mistletoe.jpg',
    'Oregon': 'oregon_oregongrape.jpg',
    'Pennsylvania': 'pennsylvania_mountainlaurel.jpg',
    'Rhoda Island': 'rhodeisland_violet.jpg',
    'South Carolina': 'southcarolina_yellowjessamine.jpg',
    'South Dakoda': 'southdakota_pasqueflower.jpg',
    'Tennessee': 'tennessee_iris.jpg',
    'Texas': 'texas_bluebonnet.jpg',
    'Utah': 'utah_segolily.jpg',
    'Vermont': 'vermont_redclover.jpg',
    'Virginia': 'virginia_dogwood.jpg',
    'Washington': 'washington_pinkrhododendron.jpg',
    'West Virginia': 'westvirginia_rhododendron.jpg',
    'Wisconsin': 'wisconsin_woodviolet.jpg',
    'Wyoming': 'wyoming_indianpaintbrush.jpg'
}

#FUNCTIONS
def menu():
    '''presents user options and returns their choice.'''
    print('\nWELCOME TO THE US POPULATION PROGRAM\n\n\
1. Display all U.S. States in Alphabetical order along with the \
Capital, State Population, and Flower.\n\
2. Search for a specific state and display the Capital \
name, State Population, and photograph of the State Flower.\n\
3. Display a Bar graph of the top 5 populated States showing their \
overall population.\n\
4. Update the overall state population for a specific state.\n\
5. Exit the program\n\n')
    choice = str(input('Enter the number of the task to perform: '))

    #check valid entry
    while choice not in ('1', '2', '3', '4', '5'):
        print('Invalid Entry.')
        choice = (input('Enter 1, 2, 3, 4, or 5: '))
    return choice

def display_us():
    '''Display all U.S. States in Alphabetical order along with the
    Capital, State Population, and Flower'''
    #format to align title
    fmt = '{:<18}{:<18}{:<15}{:<30}'
    print(fmt.format('STATE', 'CAPITAL', 'POPULATION', 'FLOWER'))
    print('~' * 80)

    #for loop to print all info
    for i, (state, capital, population, flower) in enumerate(zip(sorted(us_capitals.keys()), \
            us_capitals.values(), us_population.values(), us_flowers.values())):
        print(fmt.format(state, capital, '{:,}'.format(population), flower))
#display_us()

def state_search():
    '''Search for a specific state and display the appropriate Capital
    name, State Population, and an image of the associated State Flower.'''
    select_state = input('Enter the US State to view information: ')
    #verify valid input
    while select_state not in us_states:
        print('Invalid Entry')
        select_state = input('Enter a US State (ex. Maryland): ')
    capital = us_capitals[select_state]
    population = us_population[select_state]
    flower = us_flowers[select_state]
    fmt = '{:<18}{:<15}{:<30}'
    print(fmt.format('CAPITAL', 'POPULATION', 'FLOWER'))
    print('~' * 80)
    print(fmt.format(capital, '{:,}'.format(population), flower))

    #get image from dictionary flower_img
    im_flower = Image.open(flower_img[select_state])
    im_flower.show()
#state_search()

def bar_graph_top5():
    '''Provide a Bar graph of the top 5 populated States showing their
    overall population.'''
    sort_pop = sorted(us_population.items(), key=lambda x: x[1], reverse=True)
    #for loop to print states with the top 5 populations
    #for i in range(5):
    #    print(sort_pop[i])

    names = [sort_pop[0][0], sort_pop[1][0], sort_pop[2][0], sort_pop[3][0], sort_pop[4][0]]
    values = [sort_pop[0][1], sort_pop[1][1], sort_pop[2][1], sort_pop[3][1], sort_pop[4][1]]
    plt.bar(names, values)
    plt.suptitle('TOP 5 POPULATED STATES')
    plt.yscale('log')
    plt.show()
#bar_graph_top5()

def update_state():
    '''Update the overall state population for a specific state.'''
    state_update = input('Enter the US State to update: ')
    #check valid input for state
    while state_update not in us_states:
        print('Invalid Entry')
        state_update = input('Enter a US State (ex. Maryland): ')
    # ask user to update population and verify input is a number
    while True:
        try:
            population_update = int(input('Enter the new population for ' +
                                          state_update + '(ex. 505050): '))
            break
        except ValueError:
            print('Invalid entry. Please enter a number.')

    #search for state to update and assign the new population
    us_population[state_update] = population_update
    print('The US State, ' + state_update + ', now has a population of ' +
          str('{:,}'.format(us_population[state_update])) + ' people.')
#update_state()

def exit_states():
    '''exit message'''
    print('Thank you for visiting the US State Population program. Good day.')

def main():
    '''MAIN: calls menu() until user chooses '5' to exit'''
    choice = menu()
    while choice != '5':
        if choice == '1':
            display_us()
        if choice == '2':
            state_search()
        if choice == '3':
            bar_graph_top5()
        if choice == '4':
            update_state()

        #recursive call for menu()
        choice = menu()

    if choice == '5':
        exit_states()

if __name__ == "__main__":
    main()
