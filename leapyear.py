

#Instructions:
#The code will ask for a year, assume that it's an integer, and tell you if it is a leap year or not.
#The code will not function with inputs that are not integers. To test the code, I ran it using the debugger under the Project tab on Visual Studio.

#Definition that attempts to convert the user input from a string to an int.
#This catches all inputs containing decimals and non numerical characters.
#If the string can be converted, it will return True. If not, False.
def is_int(user_input):
    try:
        int(user_input)
        return True
    except ValueError:
        return False

def leapyear(input_year):
    


    #converts input to integer if the input is such
    if is_int(input_year) == True:
        input_year = int(input_year)
    
        #Checks to see if the input is negative.
        if(input_year < 0):
            print("Your year is negative!")

        #Checks if the year is divisable by 4 with no remainder
        elif input_year % 4 == 0:

           #checks if the year is divisable by 4 and 100 with no remainder
           if input_year % 100 == 0:
    
               #if the year is divisible by 4, 100, and 400, the year is a leap year.
               if input_year % 400 == 0:
                   return "Leap year"
    
               #if the year is divisible by 4 and 100 but not 400, it is not a leap year.
               else: 
                   return "Not a leap year"

           #if the year is divisible by 4 but not by 100, the year is a leap year.
           else:
               print("Your inputted year: ", input_year, " is a leap year.")

        #if the year is not divisible by 4, we know that it is not a leap year.
        else:
            print("Your inputted year: ", input_year, " is not a leap year.")

    else:
        print("Your input is invalid.")