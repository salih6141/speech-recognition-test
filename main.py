import speech_recognition as speechR
import pyttsx3

#initializing speech recogniser
r = speechR.Recognizer()

#Function for speech to text conversion
#speech 
def Speak(command):
    #we need to initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

#speak
#we need to loop indefinitely to allow the user to speak freely
while(1):
    try:
        with speechR.Microphone() as source:
            #we need to provide a second for the recognizer to adjust to background noise
            r.adjust_for_ambient_noise(source,duration=0.2)

            #listen user input
            audio = r.listen(source)

            #use google to recognize audio
            MyText = r.recognize_google(audio)
            MyText = MyText.lower()
            print(MyText)
            Speak(MyText)

    except speechR.RequestError as e:
        print('Could not request text; {0}'.format(e))
    
    except speechR.UnknownValueError:
        print("unknown error")