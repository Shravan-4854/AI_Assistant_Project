import os# importing os module
import pyttsx3# importing pyttsx3 for text to speech
import speech_recognition as sr# importing speech recognition module
import webbrowser# importing webbrowser module
import datetime # importing datetime module
import pyjokes  # importing pyjokes module

def sptext():# function to convert speech to text
    r = sr.Recognizer() # initialize recognizer
    with sr.Microphone() as source: # use microphone as source
        print("Listening...")   
        r.adjust_for_ambient_noise(source)  # adjust for ambient noise
        audio = r.listen(source)    # listen for audio
        try:# try to recognize the audio   
            return r.recognize_google(audio)    # use google to recognize the audio
        except:# if error occurs
            return ""   # return empty string

def speech_txt(text):   # function to convert text to speech
    engine = pyttsx3.init() # initialize the pyttsx3 engine
    engine.setProperty("rate", 150) # set speech rate
    engine.say(text)    # say the text
    engine.runAndWait() # run the engine

def process_command(data):  # function to process the command
    data = data.lower()  # convert the command to lower case
    while True:
        if "hey alexa" in data: 
            reply = "Hello Shravan, how can I help you today?"

        elif "tell me about yourself" in data:
            reply = "I am your personal assistant created by you to help you with various tasks."

        elif "what is your name" in data:
            reply = "My name is Alexa, your personal assistant."

        elif "tell me your features" in data:
            reply = "I can help you with various tasks like telling time, date, opening websites, and even telling jokes,et cetera."

        elif "tell me all commands" in data:
            commands = [
                    "tell about yourself",
                    "what's time",
                    "what's date",
                    "shut down my system",
                    "restart my system",
                    "sleep my system",
                    "open w3schools",
                    "open facebook",
                    "open youtube",
                    "open google",
                    "what is your name",
                    "tell me a joke",
                    "alexa exit",
                    "alexa stop"
                ]
            print("{commands}\t")
            reply = "Here are all the commands you can use: " + ", ".join(commands)
            
        elif "what's time" in data:
            reply = datetime.datetime.now().strftime("Time is %H:%M:%S")

        elif "what's date" in data:
            reply = datetime.datetime.now().strftime("Today's date is %d-%m-%Y")

        elif "open google" in data:
            webbrowser.open("https://www.google.com")
            reply = "Opening Google"

        elif "open youtube" in data:
            webbrowser.open("https://www.youtube.com")
            reply = "Opening YouTube"

        elif "open chatgpt" in data:
            webbrowser.open("https://chat.openai.com")
            reply = "Opening ChatGPT"

        elif "open facebook" in data:
            webbrowser.open("https://www.facebook.com")
            reply = "Opening Facebook"

        elif "open w3schools" in data:
            webbrowser.open("https://www.w3schools.com")
            reply = "Opening W3Schools"

        elif "tell me a joke" in data:
            speech_txt("sure shravan, I have a joke for you.")
            speech_txt("let's go.")
            reply = pyjokes.get_joke()

        elif "shut down my system" in data:
            os.system("shutdown /s /t 1")
            reply = "Shutting down the system"

        elif "restart my system" in data:
            os.system("shutdown /r /t 1")
            reply = "Restarting the system"

        elif "sleep my system" in data:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            reply = "Putting the system to sleep"

        elif "alexa exit" in data or "alexa stop" in data:
            reply = "okay shravan thank you!"
            break

        else:
            reply = "Sorry shravan, I didn't understand. can you please repeat?"

        speech_txt(reply)   # convert the reply to speech
        return reply    # return the reply
