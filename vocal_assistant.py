"""File that contains the vocal assitant class"""
from time import sleep
import speech_recognition as sr
import pyttsx3
import os
from pynput.keyboard import Key, Controller
from AppOpener import run
import task 
from datetime import date, datetime
import webbrowser
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

class Assistent():
    def __init__(self, name: str, gender: str, speech_speed: int = 100):
        self.name = name
        self.gender = gender
        self.speech_speed = speech_speed
        self.engine_speak = pyttsx3.init()
        # self.voice = self.engine_speak.getProperty('voices')
        # self.engine_speak.setProperty('voice', self.voice[1].id)
        self.engine_speak.setProperty('rate', self.speech_speed)
        self.engine_keyboard = Controller()
        self.task_manager = task.Task(self.name.lower())
        # self.task_weather_manager = weather.Weather(self.name.lower())

    
    def write(self, text):
        """function that writes a text on the screen"""
        sleep(2)
        self.engine_keyboard.type(text)


    def speak(self, text: str) -> None:
        """ Function that converts a text to speak """
        self.engine_speak.say(text)
        self.engine_speak.runAndWait()


    def get_audio(self):
        """Function that get the audio"""
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                logging.debug(said)
            except Exception as e:
                print("Exception: " + str(e))
                said = "Sorry, could not undersand you"
                # self.speak("Sorry, could not undersand you")

        return said

        
    def change_name(self, new_name):
        self.name = new_name
        return "Now the assistent's name it's " + new_name
    
    
    def get_name(self):
        return self.name
    
    
    def change_gender(self, new_gender):
        self.gender = new_gender
        logging.debug(f"The gender of the assitent was changed to {new_gender}")
    
    
    def get_gender(self):
        logging.debug(f"The gender of the assistent {self.name} is {self.gender}")
        return self.gender
    
    
    def change_speech_speed(self, new_speed):
        self.speech_speed = new_speed
        self.engine_speak.setProperty('rate', self.speech_speed)
        logging.debug(f"The speed was changet to  + {new_speed}")
    
    
    def get_speech_speed(self):
        logging.debug(f"The speed is {self.speech_speed}")
        return self.speech_speed
    

    def run_task(self, task_index, text):
        if task_index == 0:
            self.speak('What can I do for you?')
        
        if task_index == 1:
            lista, path, files = self.task_manager.open_my_presentation()
            size = len(lista)
            leter = "C"

            if size == 1:
                file = lista[0]
                self.speak(f"You have {size} file in the folder")
                self.speak(f"The name of the file is {file}")
                os.system(f"start powerpnt /{leter} {path}/{files[0]}")

            else:
                i=1
                self.speak(f"You have {size} files in the folder")
                for project in list:
                    self.speak(f"Say {i} for open {project}")
                    i = i + 1

            text = self.get_audio()
            print(type(text))
            
            if text == "1":
                self.speak(f"I will open {lista[0]}")
                os.system(f"start powerpnt /{leter} {path}/{files[0]}")
            
            if text == "2":
                self.speak(f"I will open {lista[1]}")
                os.system(f"start powerpnt /{leter} {path}/{files[1]}")

        
        if task_index == 2:
            self.task_manager.next_slide()
        
        if task_index == 3:
            self.task_manager.previous_slide()


        if task_index == 4:
            string = text.split(" ")[-1]

            weather_data = self.task_manager.weather(text)


            if(weather_data):

                temperature = round(int(((weather_data['main']['temp'])-32) * 5) / 9)
                main = weather_data['weather'][0]['main']
                if(main == "Clouds"):
                        main = "cloudy"

                elif(main == "Mist"):
                        main = "misty"

                elif(main == "Fog"):
                        main = "fogy"

                self.speak(f"In {string} the weather is {main}")
                sleep(0.5)
                self.speak(f"and are {temperature} degrees")
            
            else:
                self.speak("Sorry, I dont't find the city")


        if task_index == 5:
            ora = self.task_manager.time()
            self.speak(ora)


        if task_index == 6:
            data = self.task_manager.date()
            self.speak(data)


        if task_index == 7:
            self.speak('You welcome')
            

        if task_index == 8:
            self.speak("I will minimize the window")
            self.task_manager.minimise()
            

        if task_index == 9:
            self.speak("I will close the window")
            self.task_manager.close_file()

      
        if task_index == 10:
            self.speak("I will open the file")
            self.task_manager.open(text)


        if task_index == 11:
            self.speak("Focus active")
            self.task_manager.focus(text)


        if task_index == 12:
            self.speak("I will maximize the window")
            self.task_manager.maximise()

        if task_index == 13:
            self.speak("I will active the presentation mode")
            self.task_manager.presentation_mode() 

        if task_index == 14:
            self.speak("I will deactivate the presentation mode")
            self.task_manager.finish_presentation()

        
        if task_index == 15:
            # self.speak("I will open notepad")
            self.task_manager.say_something()

        if task_index == 16:
            self.speak("Goodbye everyone")