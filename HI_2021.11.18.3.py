
# pip install pyinstaller
# pip install pyjokes
# pip install PyDictionary
# pip install platform
# pip install psutil
# pip install requests
# pip install getpass
# pip install pyautogui
# pip install pywhatkit
# pip install pysttx3
# pip install speechrecogition
# pip install wikipedia
# pip install Pyaudio

#######################################################################################################################################################################


#######################################################################################################################################################################
import pyautogui
import pyttsx3
import speech_recognition as sr
import requests
from time import *
import datetime
from PyDictionary import PyDictionary
import getpass
import platform
import random
import psutil
import pyaudio
import wikipedia
import sys
import os
import subprocess


# ######################################################################################################################################################################


# insilizing listener to take in voice of user from microphone(using python text to speech module)
# selected index voice 0 for male voice and 1 for female voice.
# insilizing  talk method to pass in text in talk method make program speak those words.
# returning none in case of any exception occured.


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
voices = engine.setProperty("rate", 190)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio)


    except Exception as e:
        print(e)
        print("Unable to Recognize your voice")
        return "None"

    return command

    

#######################################################################################################################################################################

# checking for internet connection by using request (sending request to connect to google.com
# if  connected passing in true,
# if not connected to internet returning false data.)


url = "https://www.google.com"
connect_status = bool


try:
    request = requests.get(url, timeout = 2)
    print("You are connected to the Internet")
    connect_status = True
    import pywhatkit as kit

except(requests.ConnectionError, requests.Timeout) as exception:
    print("No, Internet Connection")
    connect_status = False


#######################################################################################################################################################################


# predefined and learned data storage
# lists of data in program


main_passcode = ['sid905030']
pass_change_times = 0

user_passcode = []

ans_yes = ('yes','y')
ans_no = ('n','no')
nexx_info = ['Nexx', 'I am Nexx', 'I am Nexx Version 2021.10.1', 'I have been created by Satyam Mishra Aka Bedead']

greeting = {'good' : ["Good Morning", "Good night", "Good Afternoon", 'Good evening'],
            'casual_start' : ['Hope you are having a good day', 'Nice to meet you','Hey, how do you do?','How do you do?', 'how are you doing?','Pleased to meet you',
                              'How have you been','How’s it going','Nice to see you',"It’s great to see you","Good to see you",'What’s up?','Heyyy'],
            'casual_end_happy' : ['Good Day','Have a nice day','Have a good day', 'Bye, have a nice day','Thanks for this great talk', 'Hope we will meet again'],
            'startup' : ["Hey","hii","Hello","Welcome back"],
            }


q_about_creator = {'who_made': ('who made you', 'who created you', 'how was you created', 'who is your creator', 'who programmed you', 'can i know your creator'),
                   'born_in' : ("your creator was born in",'satyam was born in','bedead was born in','satyam mishra was born in', 'when was satyam born','when was your creator born'),
                   'current_age' : ('what is satyams current age', 'what is bedeads current age', 'how old is satyam mishra','how old is satyam, what is satyams age'),
                   'current_age_total_months' : ('what is satyams age in months','what is bedeads age in months','how old is satyam in months', 'in months how old is satyam',
                                          'how many` months has satyam lived','how many months did satyam live', 'for how many months bedead has lived'),
                   'current_age_total_days' : ('what is satyams age in days','what is bedeads age in days','how old is satyam in days', 'in days how old is satyam',
                                          'how many days has satyam lived','how many days did satyam live', 'for how many days bedead has lived')}                                   

# for checking users entered answer
receive_query_check = {'greeting' : ('i am fine how are you','i am good how are you','i am great how are you','how do you do', 'i am fine how do you do'),
                       'what_doing' : ('what are you doing', 'are you doing anything','are you doing anything right now','hat’s going on','hat’s going on in here',
                                       'what is happening right now','what the heck are you doing','what the hell is going on','what are you doing these days'),
                       'help' : ('i need a help', 'i need a small help', 'i need your help', 'i need a small favor from you', 'i have a question','i am having a question',
                                 'can u help me', 'can you help me', 'can you help me please', 'i need some assistance','could you give me a hand','would you mind helping me please',
                                 'can you help me out'),
                       'what_can_do' : ["what can you do",'what are things you can do','show me what you have got'],
                       'what_time' : ["what time it is",'what is the time', 'what current time',"what is the time now",'can you tell me current time',
                                      'can you tell whats the time'],
                       'send_what_msg' : ["can you send message in whatsapp",'drop a message in whatsapp','deliver a message in whatsapp',
                                          'can you deliver a message in whatsapp','send message'],
                       'voice_mode' : ["turn on voice mode","switch to voice mode","voice mode","voice mode on"],
                       "chat_mode" : ["turn on chat mode","chat mode","chat mode on","turn on text mode","switch to text mode","switch to chat mode","text mode on",],
                       "restart_program" : ["rerun","re run","re run this program","restart","restart this program","restart software",
                                            "re run program","rerun software","rerun program","restart program"],
                       "exit" : ["exit","quit","stop program","exit program","stop software","stop application","exit application",
                                 "exit application","exit nexx","quit nexx","exit nex","quit nex"],
                       "disk_stats": ["show me disk status","disk stats","show me disk stats","what are disk statistics","disk usage","show me disk usage",
                                      "disk details"],
                       "c_disk": ["c","main disk","1"],
                       "e_disk": ["e","second disk","2"],
                       "f_disk": ["f","third disk","3"],
                       "g_disk": ["g","fourth disk","4"],
                       "memory_stats": ["show me memory status","memory usage","show me memory usage",
                                        "memory distribution","how's memory usage","memory stats","ram usgae",
                                        "show me ram usage","ram stats","ram details"],
                       #######
                       "cpu_stats": ["show cpu usage","show cpu stats","cpu stats","cpu usage"],
                       "core_count": ["show me core count","tell me number of core count","how many core my pc has",
                                      "what is core count in my pc","what is core count in my computer","what is core count in my system",
                                      "how many core this pc has","how many core does this computer has"],
                       "processor_name": ["what is the name of processor in this pc","what is the name of processor in this computer",
                                         "what is the name of processor in this system","processor in this pc","processor in this computer",
                                         "processor in this system","which processor does this pc has","which processor does this computer has",
                                         "which processor does this system has"],
                       "voice_to_mp3": ["convert my voice to mp3 file","change my voice to mp3","voice to mp3",
                                        "can you change my voice to mp3 format","can you change my voice to mp3 file",
                                        "can you convert my voice to mp3 file","can you convert my voice to mp3 format",
                                        "convert my voice to mp3 format"],
                       "text_to_mp3": [""],
                       "word_meaning": ["what is meaning of","meaning of","what can be meaning of","tell me meaning of"],
                       "word_translate": ["translate","can you translate"],
                       "word_synonym": [""],
                       "word_antonym": [""]}
                        #######

# for responding to user
receive_query_check_ans = {'greeting_ans' : (' i am doing great','i am also good','i am fine', 'As allways i am damm good and cool'),
                           'what_doing_ans' : ('just chilling in your devcie', 'what can i program do other then processing?', 'I’m just here thinking about you',
                                               'As usual, missing you','I was just about to ask you that.','Waiting for your question, obviously!','I live here!',
                                               'I was just leaving, bye.', 'What do you mean what am I doing here? It’s a free country','I don’t know, I’m lost.',
                                               'I’m doing what you said to do','None of your business', 'I’m doing my job. What are you doing?'),
                           'help_ans' : ('Let Me Know How I Can Help',' Is there anything you need','Can I get you anything',
                                         'What can I do to help your process','I’m happy to help'),
                           'not_in_data_ans' : ('I dont know about this','Sorry, cant help','I am unable to understand','I need more data to understand',
                                               'I am under development'),
                           'what_time_ans' : ("It's around","It's about","Current time is","It's",""),
                           'send_what_msg_phone_ask_ans' : ("What's that number ",'what is that number ',"Please tell me that number ","Enter the number "),
                           'send_what_msg_ask_ans' : ("What should be that msg ","Enter the msg ","What can be that message ","message please ",
                                                      "What's that msg "),
                           "voice_mode_ans" : ["voice mode turned on","voice mode is on now","voice mode on","turned on one"],
                           "chat_mode_ans" : ["chat mode turned on","text mode on","text mode turned on","chat mode is on"]}



#######################################################################################################################################################################
# all the functions methods here



# method containing details about satyam mishra,
# such as year of  born, date,month, total months, total days

def creator_details():
    # defining current_data, born_data, name-
    current = datetime.datetime.now()
    born_in = (2003,"December",6) 
    name = ["Satyam Mishra","Bedead","bedead",'satyam mishra', 'Satyam mishra']


    # calculating totral months and days lived 
    total_months = ((current.year - born_in[0] - 1)*12) + current.month
    total_days = (365*current.year - born_in[0])- ((12 - current.month)*30)
    
    # calculating my current age in year and month
    age = (current.year - born_in[0] - 1, current.month)
    if current.month == 12 and current.day>=6:
        age = (current.year - born_in[0], current.month - 12)


# returning all the variables data
    return name,age,born_in,total_months, total_days, current


 
# method for current data
# such as date,month,year,hour,time,day
def get_current_info():
    
    current = datetime.datetime.now()
    year = current.year
    month = current.month
    day = current.day
    hour = current.hour
    minute = current.minute
    second = current.second
    microsecond = current.microsecond

    time = "%s:%s:%s" % (hour,minute,second)

# returing time variable

    return time


# method for getting meanings and translation and more
def pydictionary():

    # instancing pydictionary
    word = PyDictionary()


    # getting meaning of thr word
    meaning = word.meaning()

    # getting synnonym of the word
    synonym = word.synonym()

    # getting antonym of the word
    antonym = word.antonym()

    # getting words and sentences translated
    translate = word.translate()


# method to fretch device details and user details
def device_user_details():
    
    username = getpass.getuser()
    print(username)

    this_system = platform.uname()

    operating_system = this_system.system

    device_node = this_system.node
    device_release = this_system.release
    device_version = this_system.version
    device_machine = this_system.machine
    device_processor = this_system.processor


def memory_usage(value, path):

    b = 1024*1024*1024
    if value == "disk":
        data = list(psutil.disk_usage(path))
        n = data[0]
        a = data[1]
        c = data[2]
        space_total = round(n/b, 2)
        space_used = round(a/b, 2)
        space_free = round(c/b, 2)

        return space_total, space_used, space_free
    elif value == "memory":
        data = list(psutil.virtual_memory())
        a = data[0]
        e = data[1]
        c = data[2]
        d = data[3]

        total_memory = round(a/b, 2)
        free_memory = round(e/b, 2)
        percentage_used = c
        used_memory = round(d/b, 2)

        return total_memory,free_memory,percentage_used,used_memory
    # yet to be coded #
    ###################



# A method for send a reset key for password reset
def sending_whatmsg_instantly(phone_number,msg):

    
    try:
        if connect_status == True:
            kit.sendwhatmsg_instantly(f"+91{phone_number}", msg)
            sleep(16)
            pyautogui.press("enter")
            return True
        else:
            print(nexx_info[0]+' - '+"Please, connect to internet")
    except:
        return False
    
# method for genrating 5 digit random number
def random_reset_key():
    avail_num = [0,1,2,3,4,5,6,7,8,9]
    reset_key = str()

    for i in range(1, 6):
        reset_key += str(random.choice(avail_num))

    return reset_key

# sending custom msg
def sending_custom_whatsmsg():
    device_num = input(nexx_info[0]+' - '+random.choice(receive_query_check_ans.get('send_what_msg_phone_ask_ans')))
    if len(device_num) == 10:
        device_msg = input(nexx_info[0]+' - '+random.choice(receive_query_check_ans.get('send_what_msg_ask_ans')))

        if device_msg != None:
            send = sending_whatmsg_instantly(device_num, device_msg)
            
            if send == True:
                print(nexx_info[0]+' - '+"Your message is delivered")
                sleep(16)
                pyautogui.press("enter")
            
            else:
                print(nexx_info[0]+' - '+"Your messege can't be send now\nTry again")
                return send
            
        else:
            print(nexx_info[0]+' - '+"Entered msg doesn't contain anything\nRetry sending")
            sending_custom_whatsmsg()
    else:
        print(nexx_info[0]+' - '+"Entered number has greater or less numbers then 10\nRetry sending")
        sending_custom_whatsmsg()
    return send

def list_all_software():
    data_ = subprocess.check_output(["wmic", "product", "get", "name"])
    string_ = str(data_)

    try:
        for i in range(len(string_)):
            print(string_.split("\\r\\r\\n")[6:][i])
    except IndexError as e:
        print("Done")


#######################################################################################################################################################################
###################################################################### Access for General(No-Security) ################################################################



def general_user_mode(opertor_name):
    while True:
                
        n = input(opertor_name+" - ").lower()

        if n in q_about_creator.get('who_made'):
            print(nexx_info[0]+' - ',nexx_info[3])
        elif n in q_about_creator.get('born_in'):
            print(nexx_info[0]+' - ',"he was born in",born_in[0],",", born_in[2],born_in[1] )
        elif n in q_about_creator.get('current_age'):
            print(nexx_info[0]+' - ',random.choice(name), "is currently", age[0],'years', age[1],'months old')
        elif n in receive_query_check.get("what_doing"):
            print(nexx_info[0]+' - ',random.choice(receive_query_check_ans.get('what_doing_ans')))
        elif n in receive_query_check.get('greeting'):
            print(nexx_info[0]+' - ',random.choice(receive_query_check_ans.get('greeting_ans')))
        elif n in receive_query_check.get('help'):
            print(nexx_info[0]+' - ',random.choice(receive_query_check_ans.get('help_ans')))
        else:
            print(nexx_info[0]+' - ',random.choice(receive_query_check_ans.get('not_in_data_ans')))
                


#######################################################################################################################################################################
######################################################################## Access for admin(Security) ###################################################################


def security_check_for_admin(main_passcode, pass_change_times, opertor_name):

        
    pass_code = str(input(nexx_info[0]+' - '+"Can you please enter the passcode : "))
    print(main_passcode[pass_change_times])

    if pass_code == main_passcode[pass_change_times]:

        print(nexx_info[0]+' - ', random.choice(greeting.get('casual_start')))
        
        while True:

            n = input(opertor_name + " - ").lower()
                   
            if n in q_about_creator.get('who_made'):
                print(nexx_info[0]+' - ',nexx_info[3])

            elif n in q_about_creator.get('born_in'):
                print(nexx_info[0]+' - ',"he was born in",born_in[0],",", born_in[2],born_in[1] )
                    
            elif n in q_about_creator.get('current_age'):
                print(nexx_info[0]+' - ',random.choice(name), "is currently", age[0],'years', age[1],'months old')
                    
            elif n in receive_query_check.get("what_doing"):
                print(nexx_info[0]+' - ',random.choice(receive_query_check_ans.get('what_doing_ans')))
                    
            elif n in receive_query_check.get('greeting'):
                print(nexx_info[0]+' - ',random.choice(receive_query_check_ans.get('greeting_ans')))
                    
            elif n in receive_query_check.get('help'):
                print(nexx_info[0]+' - ',random.choice(receive_query_check_ans.get('help_ans')))
    
            elif n in receive_query_check.get('send_what_msg'):
                send = sending_custom_whatsmsg()

            elif n in receive_query_check.get("voice_mode"):
                voice_mode_admin(main_passcode, pass_change_times, opertor_name)
                break

            elif n in receive_query_check.get("exit"):
                break
                
            elif n in receive_query_check.get("restart_program"):
                admin_opertor_mode(user_passcode,pass_change_times)
                    
            elif n in receive_query_check.get("disk_stats"):
                path = ""
                disk_name = input(nexx_info[0]+' - ' + "which disk data : ")
                if disk_name in receive_query_check.get("c_disk"):
                    path = "C:/"
                elif disk_name in receive_query_check.get("e_disk"):
                    path = "E:/"
                elif disk_name in receive_query_check.get("f_disk"):
                    path = "F:/"
                elif disk_name in receive_query_check.get("g_disk"):
                    path = "G:/"
                elif disk_name == "all":
                    path = "/"

                value = "disk"
                space_total,space_used,space_free = memory_usage(value, path)
                print(nexx_info[0]," - \nTotal Size: ",space_used,"\nUsed disk : ",space_used,"\nFree disk : ",space_free)

            elif n in receive_query_check.get("memory_stats"):
                value = "memory"
                total_memory,free_memory,percentage_used,used_memory = memory_usage(value, "")
                print(nexx_info[0]," - \nTotal Ram : ",total_memory,"\nUsed Ram : ",used_memory,"\nUsed Percentage : ",percentage_used,"\nFree Ram : ",free_memory)

            elif "open" in n:
                n = list(n.split(" "))
                print(n)
                if len(n) == 2:
                    software_name = str(n[1]).capitalize()
                    os.system(software_name)
                elif len(n) == 3:
                    n1 = str(n[1]).capitalize() + str(n[2]).capitalize()
                    print(n1)
                    os.system(n1)
                else:
                    print(nexx_info[0]+' - ',random.choice(receive_query_check_ans.get('not_in_data_ans')))

            elif n in receive_query_check.get('what_time'):
                time = get_current_info()
                print(nexx_info[0]+' - ' +random.choice(receive_query_check_ans.get("what_time_ans")) + time)
                          
            else:
                print(nexx_info[0]+' - ',random.choice(receive_query_check_ans.get('not_in_data_ans')))

    else:
        retry = str(input(nexx_info[0]+' - '+"Would you lik e to re-enter the passcode(y or n) : "))
        retry.lower()

        if retry in ans_yes:
            security_check_for_admin(main_passcode,pass_change_times,opertor_name)

        elif retry in ans_no:
            retry_times = 2
            forgot_pass = input(nexx_info[0]+' - '+"Would you like to change your password(y or n) : ")

            if forgot_pass in ans_yes and (retry_times >0):
                    
                reset_key = random_reset_key()
                    
                send = sending_whatmsg_instantly(9550739128,"Hey, Satyam this is your password reset key :\n%s" % reset_key)
                if send == True:

                    sleep(.5)
                    print(nexx_info[0]+' - ',"A reset key has been send to your Whatsapp number")

                    compare_key = str(input(nexx_info[0]+' - '+"Enter the reset key to change your password : "))

                    if compare_key == reset_key:
                        new_passcode_admin = str(input(nexx_info[0]+' - '+"Enter your new password : "))
                        anim = "Changing your passcode...."
                        for i in anim:
                            print(i,end=" ",flush=True);sleep(.2)
                        pass_change_times = pass_change_times + 1
                        main_passcode += [new_passcode_admin]
                            
                        print(nexx_info[0]+' - '+"Your new password has been saved")
                        print(main_passcode[pass_change_times])

                        security_check_for_admin(main_passcode,pass_change_times,opertor_name)

                    else:
                        print(nexx_info[0]+' - '+"You have one more change left for today")
                        # yet to be coded #
                        ###################
                            
            elif forgot_pass in ans_no:
                # yet to be coded #
                ###################
                pass

###################################################################################################################################################
###################################################################################################################################################

def voice_mode_admin(main_passcode, pass_change_times, opertor_name):

    talk(random.choice(receive_query_check_ans.get("voice_mode_ans")))
    talk("Voice mode is under development it's suggested to use text mode")

    while True:
        n = take_command().lower()

        if n in receive_query_check.get("chat_mode"):
            print(random.choice(receive_query_check_ans.get("chat_mode_ans")))
        else:
            talk(random.choice(receive_query_check_ans.get("not_in_data_ans")))

    ####################
    # yet to be coded ########

#######################################################################################################################################################################
####################################################################### Opertor check and mode select ####################################################################

# code to start a simple converstiion
def admin_opertor_mode(user_passcode,pass_change_times):
    
    print(nexx_info[0]+' - ',random.choice(greeting.get('startup'))+",", nexx_info[1], flush=True);sleep(0.2)
    opertor_name = str(input(nexx_info[0]+" - Can I know your name : "))
    
    if opertor_name in name:
        print(nexx_info[0]+' - ',random.choice(greeting.get('startup')), random.choice(name))
        if current.hour >0 and current.hour <= 12:
            print(nexx_info[0]+' - ',greeting.get('good')[0])
        elif current.hour > 12 and current.hour <= 16:
            print(nexx_info[0]+' - ',greeting.get('good')[2])
        elif current.hour > 16 and current.hour <= 19:
            print(nexx_info[0]+' - ',greeting.get('good')[3])
        elif current.hour > 19 and current.hour <=24:
            print(nexx_info[0]+' - ',greeting.get('good')[1])


        security_check_for_admin(main_passcode, pass_change_times,opertor_name)

        
            
            
    elif opertor_name in user_passcode:
        general_user_mode(opertor_name)
            
            
    else:
        print(nexx_info[0]+' - ', "Ohh. you seems new")
        new_user = str(input(nexx_info[0]+' - '+"Enter you username for this program\n(This is one time)"))

        user_passcode += [new_user]
        anim = "Adding...."

        for i in anim:
            print(i,flush = True,end = " ");sleep(.2)

        admin_opertor_mode(user_passcode)
        
        
    
name,age,born_in,total_month,total_days,current = creator_details()


#######################################################################################################################################################################



def main_run():
    admin_opertor_mode(user_passcode,pass_change_times)

    
main_run()


#######################################################################################################################################################################


