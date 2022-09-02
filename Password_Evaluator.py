'''
Project 2 - Password Evaluator - Spring 2021
Author: Matthias Cannon matthiasc@vt.edu

Passwod Evaluator

I have neither given or received unauthorized assistance on this assignment.
Signed:  Matthias Cannon
'''


def check_length(password):
    passlength = len(password) #checks length
    
    if passlength < 8: #if the passlength is less than 8 then return a 1
        return 1
    if passlength >= 8 and passlength <= 11: # if greater than or equal to 8 but less than equal to 11 return a 2
        return 2
    if passlength >= 12: #everything greater than or equal to  12 receives a 3
        return 3
    
    
def check_case(password): #checks case sense whether letter is upper/lower case
    
    if password.isdigit(): #if all characters are digits returns 2
        return 2 
    
    if password.isupper() or password.islower(): #upper or lowercase return 1
        return 1
    else:
        return 2
    
    
    
def check_content(password): #this function checks for any digits within the password 

    if password.isalpha():
        return 1 #this specifically tells the program to return a 1 if all the characters are alphabetical  
    elif password.isalnum():
        return 2 #returns a 2 if its numerical and alphabetical 
    else:
        return 3 #returns a three for anything else 
    
def main(): #contains the loop in order to run any amount of passwords without issues
    print('Welcome to the Password Evaluator!')
    print()
    userinput = ''
    while 1: #the loop that is being run 
        userinput = input('Enter a password or "q" to quit: ')
        if userinput == 'q':
            print()
            print('Thanks for using the Password Evaluator!')
            break #will print the above statement and break the loop if the userinput is 'q'
        lengthscore = check_length(userinput)
        casescore = check_case(userinput) #stored the value as casescore
        contentscore = check_content(userinput)
        
        totalscore = lengthscore + casescore + contentscore #formula to give back total score of password in order to evaluate whether its strong, weak or acceptable  
        
        print('Score = ' + str(totalscore))
        if totalscore <= 5:
            print('That password is weak!')
        elif totalscore < 8:
            print('This password is acceptable.')
        else:
            print('This password is strong!')
        
        print()

    
    
if __name__ == '__main__': #call to the if statement in order to keep program from running when initially imported to WebCat
    main()