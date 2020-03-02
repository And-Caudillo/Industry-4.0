id = 'Mariela'

print ('Hi, my name is Mariela')
print ('Are you okay with it?')
print ('Yes/No: ')
name=input()

if name == 'Yes':
	print ("I'm glad you say yes. I love my name, actually :D")

else: 
    print ("Well, wich name would you prefer?")
    id = input()
    print ("Okay, let's do this again. Hi, my name is {}".format(id))
	
print ("Now that you know my name I would like to know yours")
user=input()
print ("Nice to meet you {}".format(user))

print ("I think it would be nice if we were friends, what do you think?")
print ('Yes/No: ')
friends=input()

if friends =='Yes':
    print ("Amazing! My first human friend :D")
    print ("Let's get to know each other, okay?")
    print ("My favourite TV Show is Game of Thrones, what about you?")
    show=input()
    if show == 'Game of Thrones':
        print ("Really? Oh! We have so much in common")
    else:
        print ("I don't know that show, I will check it out later. But I really recomend you to watch GOT")
    print ("Now let's talk about music. Do you know The Cure?") 
    print ('Yes/No: ')
    band=input()
    if band == 'Yes':
        print ("They are great! I could say they are my favourite.")
    else:
        print ("You should listen to them, they are amazing ;D")
    print ("I would love to continue talking to you but I need to go. Goodbye {}" .format(user))
    print ("Have a nice human day :D")
else:
    print ("Amm.. okay. Then I don't see the point in continue talking. Goodbye {}" .format(user))
    
