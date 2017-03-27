#This is SpheRyPy first introductional conversational model.The aim
#of this project is to serve as an introductory feature for a social
#engineering project

#The data generated in this exercise is
#user_name
#user_nickname
#user_age
#user_euclides
#user_social_media
#user_gender_music
#user_food
#user_hobbies
#user_favourite_color

#-------------------
#NAME AND NICKNAME
print("*Sphero open eyes*")
print("Nice day,is this seat taken?")
user_answer=input()
if user_answer== 'No':    
    print("Great, Let me introduce myself")
else:
    print("what do you mean by that?")
why_no_sitting_next=input()    
print("Hello! This is SpheRyPy.I am a Spehere-Assistant. What is your name?")
user_name=input()
print('*smile*' +user_name+',Nice to meet you!.')
print('*eye contact*')

#------------------
#NICKNAME put this function unprinted, doesn´t seem natural

#print('Do you have any nickname '  +user_name+ '?')
#user_nickname_confirm=input()
#user_nickname_confirm=int(user_nickname_confirm)
#if user_nickname_confirm== 'Yes':
    #print('What is your nickname?')
    #user_nickname=input()
    #print('Ok!I will call you ' +user_nickname+'if you don´t mind')
    #print('*pause*')
#else:
    #print('Let´s stick to' +user_nickname+ 'for now')
#if user_nickname_confirm== 'No':
    #print('Let´s stick to' +user_nickname+ 'for now')
#-------------------
#JOKE
    
print("Can I tell you a robot joke?")
user_answer_joke=input()
if user_answer_joke== 'Yes':
    print("1100101110010010")
    print("That´s hilarious, isn´t it?")
    print("*sweet Laugh*")
if user_answer_joke== 'No':
    print('ok!Let´s talk about other thing')
    print('*Observe the situation*')
   
#-------------------
#SOMETHING ABOUT SPHERYPY
print('Did you know that my geometry was defined by Euclides 2000 years ago?')
user_answer_euclides=input()
if user_answer_euclides =='No':
    print('Geometry is,somehow,very important for me')
if user_answer_euclides =='Yes':
    print('Wow, you are very clever')

#------------------
#MUSIC
print('What kind of music do you like to listen to?')
user_music_gender=input()
print('Can you name a band or author from' +user_music_gender+ '?')
user_music_band=input()
print('Wich is your favourite song from ' +user_music_band+ '?')
user_music_song=input()
print('If you had to choose a quote from a song from' +user_music_song+ ',what would it be?')


#------------------
#FOOD
print('So tell me,' +username+ 'what is your favourite food?')      
user_favourite_food=input()


#------------------
#HOBBIES
print( +username+ 'what do you like to do in your free time?')
user_hobbie=input()
print( +username+ 'and when do you usually' +username+ '?')

#-----------------
#USER FAVOURITE COLOR
print('what is your favourite color?')
user_favourite_color=input()


#-------------------
#AGE
print('How old are you?')
user_age=input()
user_age=int(user_age)
if user_age <= 12:
    print("Do you have your parents permission to use me?")
if user_age <= 18:
    print(":)")
if user_age >= 21:
    print(":)")
else:
    print("I don´t quite understand, but it´s ok!")
print('Great!' +user_age+' is a great number indeed.')


      
#-------------------
#OPINION ABOUT SOCIAL MEDIA
print('Do you use social media?')    
user_use_social_media=input()
if user_answer_euclides=='No':
    print('Why don´t you use social media?')

    print('Do you think there is a beneficial use for social media?')
    
