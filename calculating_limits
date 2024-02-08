'''
Julissa Paramo
2/7/2023
Limit of a polynomial
'''
  
'''
This program helps a user calculates the limit of a polynomial function
'''

# currently working 


def userPolynomialProperties():
    ''' This function collects the properties of the polynomial function from the user'''
    global degree # variables belongs to global space 
    global terms_list # all the terms of the polynomial are held here
    degree = int(input("What degree is your polynomial function?: ")) # variable for the degree of the polynomial
    status = False # boolean to check proper amount of coefficients
    terms_list = [] # this is where all terms of polynomial will be held 
    while status == False:
        coefficients = input("Please list coefficients of the polynomial in order: ")
        for i in (coefficients.split()): # loops through a list of splitted input
            terms_list.append(int(i)) # appends each term in the list as an int to terms list
        count = 0
        for i in terms_list: # calculates length to check how many 
            count += 1
        if degree==count:
            status=True # if degree matches amount of coefficients , loop exits
        elif  ( degree < count or degree > count): # if they do not match there is an error
            print(f"Error: Amount of coefficients does not match the degree of the polynomial\nPlease enter {degree} coefficients\n")
    constant = int(input("What is the constant term: "))
    terms_list.append(constant)
    return terms_list

def xValue():
    global x 
    while True:
        try:
            x = int(input("What is x approaching?: "))
            break
        except ValueError:
            print("Oops! that is not an integer. Try again.")
    return x
def calcLimit(terms_list):
    count = degree
    sum_limit = 0
    for i in terms_list:
        if count >= 1:
            sum_limit += (x**count) * i
            print(sum_limit)
            count -= 1
        else:
            sum_limit += i
    return sum_limit

class Polynomial():
    def __init__(self, Degree, Terms, xValue, Limit):
        self.Degree = Degree
        self.Terms = Terms
    def get_Degree(self):
        return self.Degree
    def get_Terms(self):
        return self.Terms
    def get_xValue(self):
        return self.xValue
    def get_Limit(self):
        return self.Limit
    def __str__(self):
        return f'Degree : {self.Degree}'
    
        
terms = userPolynomialProperties() 
print(terms) # terms are held in variable after function call
xValue()
print(calcLimit(terms))
