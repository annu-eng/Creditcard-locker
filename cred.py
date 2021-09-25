import pyttsx3           #pyttsx3 is a text-to-speech conversion library in Python
speaker=pyttsx3.init()   #initialing the text to speech package



dict={}                     #initializing our dictionary



def terminal_clearer():      #declaaring a function which clears the terminal for the next user                          
    for l in range(100):      #printing blank space so that previous user's data is hidden
        print()
    speaker.say('please wait')
    for l in range(100):
        print()
    return()
  

def fetcher(name):           #initializing a function which gets the details of existing customers

    speaker.say('hope you are having an amazing day,here are your details')  #Calling the function say to speak the text
   
    speaker.runAndWait()      #This function will make the speech audible in the system
  
    for keyy,value in dict.items():        #looping through each items in dictionary
        
        if value==name:                    #we print "key" of an item whose "value" is matched with input.(normally it is value is printed if key is matched)
            print(keyy)
    
    adf = int(input("enter any number(1 to 10) if done"))        #Clearing the terminal for next user.
    
    speaker.say('Thanks for using our service,see you soon')
    
    speaker.runAndWait()
   
    terminal_clearer()
    
    speaker.say('welcome to our private vault,please enter your name')   #for next user after an existing users details are shown.
    
    speaker.runAndWait()
    
    name = str(input('enter your secret username'))
    
    for ser in dict.values():
        
        if name == ser:
            
            fetcher(name)                # here we didnt use else becasue lets say there are 3 positions A,B,C and out details are stored in C
                                         # then after not finding the details in A, else will be executed hence treating the existing user as new user, which is undesirable.
    
    return(name)                                            #returning name to the main program incase the user in a new one.



#############  Main program execution begins  ###########


lst = []                     #declaring a list

for ik in range(0,10):                                              
    
    speaker.say('welcome to our private vault,please enter your name')  #Welcoming line
    
    speaker.runAndWait()

    name = str(input('enter your secret username'))         #typecasted input to string type
    
    for ser in dict.values():                               #iterating through values of a dictionaries
        
        if name == ser:
           
            name=fetcher(name)    
            '''
incase 'else' was used after if statement then the details of a 
 new user wouldn't have been possible to store after details of an exiting client is shown
as else part wont be executed after the fetcher function returns name of a new user.
'''                          
    
    for ij in range(0, 1):
    
        speaker.say('please get ready with your car details')
    
        speaker.runAndWait()
    
        oki = int(input('enter card number'))
    
        lst.append(oki)
    
        ogi = int(input('enter mobile number'))
    
        lst.append(ogi)
    
        ohi = int(input('enter CVV'))
    
        lst.append(ohi)
    
        speaker.say('your credit card details are secured with us')
    
        speaker.runAndWait()
    
        done = int(input("enter any number(1 to 10) if done "))
    
        speaker.say('Thanks for using our service, have a great day')
    
        speaker.runAndWait()


    hash = str(lst)                #stroing a list as 'key' in our dictionary

    dict[hash]=name                #assigning 'value' to the 'key' as name
   
    lst.clear()                    #clearing the list to store input of next/new user.

    terminal_clearer()

