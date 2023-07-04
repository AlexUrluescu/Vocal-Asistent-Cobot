"""File that contains the vocal assitant class"""
from time import sleep
import speech_recognition as sr
import pyttsx3
import task 
import logging

from pymodbus.client import ModbusTcpClient

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

# Adresa IP și portul serverului Modbus TCP/IP
SERVER_IP = '192.168.0.40'
SERVER_PORT = 502

# Creează un client Modbus TCP/IP
client = ModbusTcpClient(SERVER_IP, SERVER_PORT)

# cream clasa Asistent
class Assistent():
    def __init__(self, name: str, gender: str, speech_speed: int = 100):
        self.name = name
        self.gender = gender
        self.speech_speed = speech_speed
        self.engine_speak = pyttsx3.init()
        # self.voice = self.engine_speak.getProperty('voices')
        # self.engine_speak.setProperty('voice', self.voice[1].id)
        self.engine_speak.setProperty('rate', self.speech_speed)
        self.task_manager = task.Task(self.name.lower())

    
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
                self.speak("Sorry, could not undersand you")

        return said
    
    
    def get_name(self):
        return self.name
    

    def run_task(self, task_index, text):
        if task_index == 0:
            self.speak('What can I do for you?')

        
        if task_index == 1:
            # cream conexiune
            client.connect()

            # Scrierea unei valori în registrele robotului
            result = client.write_registers(address= 130, values= 1, unit=1)
            done = client.write_registers(address=133, values=0, unit=1)
            logging.debug(result)
            logging.debug(done)

            # citim valori din registrele robotului
            done_cobot = client.read_input_registers(address=134, count=1, unit=1)

            while(done_cobot == 0):
                done_cobot = client.read_input_registers(address=134, count=1, unit=1)


            done = client.write_registers(address=133, values=1, unit=1)

            sleep(5)
            self.task_manager.apple()
            self.speak("I finish the task")

            # inchidem conexiunea
            client.close()

        
        if task_index == 2:

            # cream conexiune
            client.connect()

            # Scrierea unei valori în registrele robotului
            result = client.write_registers(address= 130, values= 2, unit=1)
            done = client.write_registers(address=133, values=0, unit=1)

            # citim valori din registrele robotului
            done_cobot = client.read_input_registers(address=134, count=1, unit=1)


            while(done_cobot == 0):
                done_cobot = client.read_input_registers(address=134, count=1, unit=1)

            # citim valori din registrele robotului
            done = client.write_registers(address=133, values=1, unit=1)
            
            sleep(5)
            self.task_manager.apple()
            self.speak("I finish the task")

            # inchidem conexiunea
            client.close()

        
        if task_index == 3:

            # cream conexune
            client.connect()

            # Scrierea unei valori în registrele robotului
            result = client.write_registers(address= 130, values= 3, unit=1)
            done = client.write_registers(address=133, values=0, unit=1)

            # citim valori din registrele robotului
            done_cobot = client.read_input_registers(address=134, count=1, unit=1)


            while(done_cobot == 0):
                done_cobot = client.read_input_registers(address=134, count=1, unit=1)


            done = client.write_registers(address=133, values=1, unit=1)

            sleep(5)
            self.task_manager.apple()
            self.speak("I finish the task")

            # inchidem conexiunea
            client.close()


        if task_index == 4:
            self.task_manager.goodbye()
            self.speak("Goodbye")
