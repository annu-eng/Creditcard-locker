import pyttsx3
speaker=pyttsx3.init()
import json

dict={}
def magic_no(ohi):
    aya=ohi*3.33432346634
    aya/=4
    ayk=int(aya)
    #lst.append(ayk)
    return ayk
def fetcher(name):
    speaker.say('hope you are having an amazing day,here are your details')
    speaker.runAndWait()
    #print("welcome back :)")
    for keyy,value in dict.items():
        if value==name:
            print(keyy)
    adf = int(input("enter any number(1 to 10) if done"))
    speaker.say('Thanks for using our service,see you soon')
    speaker.runAndWait()
    for l in range(1000000):
        print()
    speaker.say('please wait')

    for l in range(1000000):
        print()
    speaker.say('welcome to our private vault,please enter your name')
    speaker.runAndWait()
    name = str(input('enter your secret username'))
    for ser in dict.values():
        if name == ser:
            fetcher(name)
    return()

lst = []
for ik in range(0,10):
    speaker.say('welcome to our private vault,please enter your name')
    speaker.runAndWait()

    name = str(input('enter your secret username'))
    for ser in dict.values():
        if name == ser:
            fetcher(name)
    for ij in range(0, 1):
        speaker.say('please get ready with your car details')
        speaker.runAndWait()
        oki = int(input('enter card number'))
        lst.append(oki)
        ogi = int(input('enter mobile number'))
        lst.append(ogi)
        ohi = int(input('enter CVV'))
        lst.append(ohi)
        ad=magic_no(ohi)
        print('your number is ' + str(ad))
        speaker.say('your credit card details are secured with us')
        speaker.runAndWait()
        done = int(input("enter any number(1 to 10) if done "))
        speaker.say('Thanks for using our service, have a great day')
        speaker.runAndWait()

    hash = json.dumps(lst)
    dict[hash]=name
    #print(dict)
    lst.clear()
    for l in range(1000000):
        print()
    speaker.say('please wait')
    speaker.runAndWait()
    for l in range(1000000):
        print()




