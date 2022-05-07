# Menu program for Programming Final Project
# Used with Github to ensure that students know the GitHub process.

semester = "ITSE1479 - Spring 2022";

def main():
    #*****************************************************************
    # jumpTable for all functions
    # 
    # Modify your line to create a jumpTable entry for your 
    #   function.  Replace stub() with the name of your function that 
    #   you added to the end this code section.
    #
    # Notes:
    #    jumpTables hold the name of a function, not the variables
    #       that are passed to it.  See smileyFunction for a way
    #       to pass variables manually, 
    #       OR create your own inputs inside of your function to 
    #           collect user input.
    #   Use the following code at the end of your function to 
    #       pause the program
    #           print()
    #           print("Press ENTER to return to the menu")
    #           input()
    #   DO NOT TRASH THE CALL TO main() at the end.  Thanks.
    #*****************************************************************
    jumpTable = {}
    jumpTable['1'] = smileyFunction       # Smiley - call to function goes here
    jumpTable['2'] = stub                 # Alvarez - call to function goes here
    jumpTable['3'] = stub                 # Appiah - call to function goes here
    jumpTable['4'] = stub                 # Balderas - call to function goes here
    jumpTable['5'] = stub                 # Butler - call to function goes here
    jumpTable['6'] = stub                 # Kennedy - call to function goes here
    jumpTable['7'] = stub                 # Long - call to function goes here
    jumpTable['8'] = stub                 # Nguyen - call to function goes here
    jumpTable['9'] = stub                 # Overby - call to function goes here
    jumpTable['10'] = stub                # Robarge - call to function goes here
    jumpTable['11'] = stub                # Roeper - call to function goes here
    jumpTable['12'] = stub                # Subba - call to function goes here
    jumpTable['13'] = stub                # Thorne - call to function goes here
    jumpTable['14'] = stub                # Thurman - call to function goes here
    jumpTable['15'] = stub                # Valdez - call to function goes here

    chrChoice = ""      # To hold a menu choice

    # Constants for the menu choices
    EXIT = '0';

    while chrChoice != '0':
        # Display the menu and get the user's choice.
        showMenu();
        
        chrChoice = input("Enter your selection (0 to exit): ")
        
        if(chrChoice.isdigit() and int(chrChoice) < (len(jumpTable) + 1)):
            # Validate the menu selection.
            if chrChoice == EXIT:
                print()
                print("Thank for using the", semester, "Menu Program. ")
                print("Have a nice day.")
            else:
                jumpTable[chrChoice]()
        else:
            print("Please enter one of the numeric values from the menu.  Thanks")
            print("Press ENTER to continue.")
            input()    

            

#*****************************************************************
# Definition of function showMenu which displays the menu.       *
#*****************************************************************

def showMenu():
    print("*******************************************************************")
    print("*   Welcome to the ", semester, " Program!")
    print("*      Make a selection from the list below to see student output *")
    print("*                                                                 *")
    print("*      Enter 0 and press Enter to Quit.                           *")
    print("*******************************************************************")

    print("1.  Smiley")
    print("2.  Alvarez")
    print("3.  Appiah")
    print("4.  Balderas")
    print("5.  Butler")
    print("6.  Kennedy")
    print("7.  Long")
    print("8.  Nguyen")
    print("9.  Overby")
    print("10. Robarge")
    print("11. Roeper")
    print("12. Subba")
    print("13. Thorne")
    print("14. Thurman")
    print("15. Valdez")
    print()

# *****************************************************************************************
# Function Definitions Section
# *****************************************************************************************
# Add your function below.
txtDict = {}
txtDict["LOL"] = "LOL: acronym for 'Laughing out loud'"
txtDict["BTW"] = "BTW: acronym for 'By the way'"
txtDict["IDK"] = "IDK: acronym for 'I don't know'"
txtDict["AFAIK"] = "AFAIK: acronym for 'As far as I know'"
txtDict["POV"] = "POV: acronym for 'Point of view'"
txtDict["DM"] = "DM: acronym for 'Direct message'"
txtDict["AFK"] = "AFK: acronym for 'Away from keyboard'"
txtDict["BC"] = "BC: short for 'Because'"
txtDict["OMG"] = "OMG: acronym for 'Oh my god'"
txtDict["OP"] = "OP: acronym for 'Original post/Original poster'"
txtDict["FTW"] = "FTW: acronym for 'For the win'"
txtDict["TY"] = "TY: acronym for 'Thank you'"
txtDict["IMO"] = "IMO: acronym for 'In my opinion'"
txtDict["IRL"] = "IRL: acronym for 'In real life'"
txtDict["ROFL"] = "ROFL: acronym for 'Rolling on the floor laughing'"
txtDict["YOLO"] = "YOLO: acronym for 'You only live once'"
txtDict["YEET"] = "YEET: To throw something, focusing on distance rather than accuracy"
txtDict["PWN"] = "PWN: Used in gaming to describe beating another player. A misspelling of the word 'own'"
txtDict["LEET"] = "LEET: Used to describe something spectacular. Derived from 'elite'"
txtDict["1337"] = "1337: Alternate version of 'LEET'"
txtDict["HAX"] = "HAX: Used to imply hacking, typically as a joke among gamers"
    
def txtFunction():
    print("~*~*~*~ Text Messaging for Old People ~*~*~*~")
    print("Learn the hip SMS (short message service) lingo!")
    next = input("Please enter a text shortcut or press 'x' to exit: ")
    next = next.upper()
    while next != "X":
        if next in txtDict:
            print(txtDict[next])
        else:
            print("Sorry, that is not in our hip SMS dictionary.")
        
        next = input("Please enter a text shortcut or press 'x' to exit: ")
        next = next.upper()
        
txtFunction()
# FunctionName:  RobargeFunction()
# *****************************************************************************************

# *****************************************************************************************
# FUNCTION:         stub (default for menu)
# DESCRIPTION:      stub function created to print a single message: Not Implemented Yet
# OUTPUT EXAMPLE:   User enters any jumpTable entry that has not been created yet
# *****************************************************************************************
def stub():
    print()
    print()

    print("Not implemented at this time.  Check back later.")
    print("Press ENTER to continue.")
    input()    

# *****************************************************************************************
# FUNCTION:         smileyFunction
# DESCRIPTION:      calls SmileyFib with a parameter of 11
#                   prints the Fibonacci series as defined by the input value
# OUTPUT EXAMPLE:   User enters 11
#                   Program outputs the following:
#                      Fibonacci Sequence (9 iterations): 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# *****************************************************************************************
def smileyFunction():
    smileyFib(11)
    print("Press ENTER to continue.")
    input()    

def smileyFib(numberOfTimes):
    current = 0
    nextOne = 1
    nextTerm = 0

    print()
    print()
    print("Fibonacci Sequence (", str(numberOfTimes)," iterations)")

    for i in range(0, numberOfTimes):
        if (i == 1):                    # Prints the first term
            print(str(current), end= '')

        elif (i == 2):                 # Prints the second term
            print(str(nextOne), end = '')
        else:                          # Prints all subsequent terms
            nextTerm = current + nextOne;
            current = nextOne;
            nextOne = nextTerm;

            print(str(nextTerm), end = '')

        if (i + 1) < numberOfTimes:
            print(", ", end = '')

    print()
    print()

#*****************************************************************
# Please leave me alone,
#   Sincerely,
#       main()
#*****************************************************************
main()
