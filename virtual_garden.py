'''
Julissa Paramo
November, 2023
Virtual Garden
'''

# Project for CIS121 , completed with Adelynn Vang and Adriana Seda
# future updates : more exception handling, errors , and infinite game mode


def Greeting():
    '''This function greets the user with a message'''
    msg = "Welcome to your virtual garden.\nLet's get planting!\n"
    ASCII_line1 = '         wWWWw               wWWWw'
    line2 = '   vVVVv (___) wWWWw         (___)  vVVVv'
    line3 = '   (___)  ~Y~  (___)  vVVVv   ~Y~   (___)'
    line4 = '    ~Y~  \\.|    ~Y~   (___)    |/    ~Y~'
    line5 = '   \\.|   \\ |/  \\.| /  \\~Y~/  \\.|    \\ |/'
    line6 = '   \\ |// \\ |// \\ |/// \\ |//  \\ |//  \\ |///'
    line7 = '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'
    return f'{msg}\n{ASCII_line1}\n{line2}\n{line3}\n{line3}\n{line4}\n{line5}\n{line6}\n{line7}'

def Season_Plant():
    '''This function gets the season and plant from user'''
    season_dict = {"Spring":['Tulip', 'Rosemary', 'Carrot'], # dictionary holding which plant grows during which season
              "Summer": ['Rose', 'Thyme', 'Bokchoy'],
              "Autumn": ['Sunflower', 'Parsley', 'Corn'],
              "Winter": ['Iris', 'Sage', 'Spinach']}
    global season # variables added to global space
    global user_plant
    season = input('What season would you like to grow in?\nSpring, Summer, Autumn, Winter: ') # user's choice of season
    for key, value in season_dict.items():
        if key == season: # finds user's season choice in the keys
            options = '\nYour planting options are: ' # str statement with user options
            for plant in value: # iterates through elements in the value list
                if plant == season_dict[key][2]: # condition for the last element in list (returns no comma at the end)
                    options += plant # adds each plant name to the str variable options
                else:
                    options += plant + ', '
            user_plant = input(f'{options}\nPick one: ') # user's choice of plant
            return "\nLet's add SUN and WATER!"
   
def Sunshine_Water():
    '''This function gets sunshine and water amount from user'''
    global water # variables added to global space
    global sunshine 
    water = int(input('How many water drops?: '))
    sunshine = int(input('How many rays of sunshine?: '))
    return ''

plant_information = {"Rose": [2,5], "Sunflower":[2,4], "Tulip":[3,3], "Iris":[4,2], # dicionary holds the growth requirements for each plant
                    "Thyme":[3,2], "Rosemary":[2,5], "Parsley":[5,4], "Sage":[2,3], # index 0 : drops of water required to fully grow
                    "Carrot":[5,2], "Corn":[4,3], "Bokchoy":[2,4], "Spinach":[3,3]} # index 1 : rays of sunlight required to fully grow

class Plant():
    def __init__(self,Name,Season,Water,Sunshine):
        self.Name = Name
        self.Season = Season
        self.Water = Water
        self.Sunshine = Sunshine
    def get_Name(self):
        return self.Name
    def get_Season(self):
        return self.Season
    def get_Water(self):
        return self.Water
    def get_Sunshine(self):
        return self.Sunshine
    def __str__(self):
        return f'\nCongratulations! You planted: {self.Name} in {self.Season}.\nGrowth Stats\n-------------\n{self.Water} drops of water\n{self.Sunshine} rays of sunlight'
    def Calc_Water(self):
        '''This class method prompts user to adjust water amount if needed for full growth'''
        for key,value in plant_information.items():
            if key == self.Name: # finds the plant in the dictionary
                status = False
                while status == False:
                    if self.Water == plant_information[key][0]:# finds index 0 of the list in the plant_information dictionary
                        print('\nNICE! Perfect amount of water has been added . . .\n') 
                        status = True # loops ends if sufficient water has been added
                    elif self.Water > plant_information[key][0]: 
                        self.Water = int(input('Too much water! Try again.\nHow many drops of water?: ')) # sets the class attribute Water to the new amount
                    elif self.Water < plant_information[key][0]:
                        self.Water = int(input('Not enough water! Try again.\nHow many drops of water?: '))
                return None
    def Calc_Sunshine(self):
        '''This class method prompts user to adjust sunshine amount if needed for full growth'''
        for key,value in plant_information.items():
            if key == self.Name: # finds the plant in the dictionary
                status = False
                while status == False:
                    if self.Sunshine == plant_information[key][1]:# finds index 1 of the list in the plant_information dictionary
                        print('\nAWESOME! Perfect amount of sunshine has been added . . .')
                        status = True # loops end if sufficient sunshine has been added
                    elif self.Sunshine > plant_information[key][1]:
                        self.Sunshine = int(input('Too much sunlight! Try again.\nHow many rays of sunshine?: ')) # sets the class attribute Sunshine to the new amount
                    elif self.Sunshine < plant_information[key][1]:
                        self.Sunshine = int(input('Not enough sunshine! Try again.\nHow many rays of sunshine?: '))
                return None
    def Report_Stats(self):
        '''This class method writes user's data to a new csv file'''
        import csv
        report_stats = input('\nWould you like a copy of your data? Y/N: ')
        if report_stats == 'Y' or report_stats == 'y': # condition if user wants their data written to a new file
            row1 = ['plant','season','water','sunshine']
            row2 = [self.Name,self.Season,self.Water,self.Sunshine]
            with open ('GardenStats.csv','w') as GardenStats: # creates new csv file GardenStats
                GardenStatswriter = csv.writer(GardenStats)
                GardenStatswriter.writerows([row1,row2]) # writes each row variable to the new csv file
            print('Your data has been saved. Thanks for playing!')
        else:
            print('Thanks for playing!')
        
print(Greeting())
print(Season_Plant())
print(Sunshine_Water())
plant_object = Plant(user_plant,season,water,sunshine) # creates Plant object from the global variables 
plant_object.Calc_Water()
plant_object.Calc_Sunshine()
print(plant_object)
plant_object.Report_Stats()
