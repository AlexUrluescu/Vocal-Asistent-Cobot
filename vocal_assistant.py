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

from pymodbus.client import ModbusTcpClient

# Adresa IP și portul serverului Modbus TCP/IP
SERVER_IP = '192.168.0.40'
SERVER_PORT = 502

# Creează un client Modbus TCP/IP
client = ModbusTcpClient(SERVER_IP, SERVER_PORT)


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
    
    
    def get_name(self):
        return self.name
    

    def run_task(self, task_index, text):
        if task_index == 0:
            self.speak('What can I do for you?')

        
        if task_index == 1:
            client.connect()

            # Scrierea unei valori în registrul de ieșire
            result = client.write_registers(address= 130, values= 1, unit=1)
            if result.isError():
                print('Eroare:', result)
            else:
                print('Valori scrise cu succes.')

            while(result == 0):
                result = client.read_input_registers(address=134, count=1, unit=1)
                if result.isError():
                    print('Eroare:', result)
                else:
                    print('Valoare citită:', result.registers)


            client.close()
            

            # here you will put the method ----------------------------
            # self.task_manager.hei()


            # ---------------------------------------------------------

        
        if task_index == 2:

            client.connect()

            # Scrierea unei valori în registrul de ieșire
            result = client.write_registers(address= 130, values= 2, unit=1)
            if result.isError():
                print('Eroare:', result)
            else:
                print('Valori scrise cu succes.')

            while(result == 0):
                result = client.read_input_registers(address=134, count=1, unit=1)
                if result.isError():
                    print('Eroare:', result)
                else:
                    print('Valoare citită:', result.registers)

            
            
            client.close()

            # here you will put the method ----------------------------
            # self.task_manager.test()


            # ---------------------------------------------------------

        
        if task_index == 3:
            # client.connect()

            # # Scrierea unei valori în registrul de ieșire
            # result = client.write_registers(address= 130, values=3, unit=1)
            # if result.isError():
            #     print('Eroare:', result)
            # else:
            #     print('Valori scrise cu succes.')

            # while(result == 0):
            #     result = client.read_input_registers(address=134, count=1, unit=1)
            #     if result.isError():
            #         print('Eroare:', result)
            #     else:
            #         print('Valoare citită:', result.registers)


            
            client.close()

            # here you will put the method ----------------------------
            self.task_manager.apple()
            self.speak("Apple")



            # ---------------------------------------------------------

        if task_index == 4:
            self.task_manager.goodbye()
            self.speak("Goodbye")
