"""

    Scott Quashen
    London App Brewery
    100 Days of Python Code: Day 2
    April 23 2024

    ------
    Description: Tip Calculator
    ------
    
    ------
    Inputs: Total Bill, Percent Desired, Amount of people to split tip with
    ------
    
    ------
    Outputs: Tip Amount
    ------
    
    ------
    Dependencies: None.
    ------

    ------
    Assumptions: Developed and tested using Spyder 5.15.7, Python version 3.11.5 on macOS 14.4.1
    ------
    
"""

def main():
    
    """
    
    Description - Calculates tip
    ----------  
    Input - Request in console total, percent, and amount of people
    ----------                    
    Outputs - Amount each person should tip.
    -------
        
    """
    
    print( 'Tip Bot' )
    
    total = get_int( 'What is the total bill? ' )
    percent = get_int( 'What percent would you like to tip? ' )
    people = get_int( 'How many people are splitting the bill? ' )
    
    tip_contribution = ( total * ( percent / 100 ) ) / people # calculate
    
    print( f'Each person should tip: ${tip_contribution}' )
    
# close 
    
    
def get_int( prompt ):
    
    """
    
    Description - Input func modified to only accept integers
    ----------
    Parameters - Prompt
    ----------
    Output - Int
    -------

    """
    
    while True:
        
        try:
            
            num = int( input( prompt ) ) # parse string into int
            
        except ValueError:
            
            print( "Try again." )
            
            continue
        
        return num
    
# close


# run code
if __name__ == '__main__':
    main()
    
    
    