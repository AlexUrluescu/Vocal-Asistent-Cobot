"""Class that models the tasks the assistant can do"""

from AppOpener import run
from pynput.keyboard import Key, Controller
from time import sleep
import os
from pywinauto import Desktop
import win32gui, win32com.client
import pyautogui
import requests
import os.path
from datetime import date, datetime
import logging
# from vocal_assistant import Assistent

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


class Task():

    def __init__(self, assistant_name):
        self.task_list = [assistant_name, "hey", "mouse", "apple", "goodbye"]
        self.assistant_name = assistant_name
        self.keyboard = Controller()

        # self.vocal_asistent = Assistent()
        

    def identify_task(self, text: str) -> int:
        logging.debug("I am here")
        logging.debug(text)
        logging.debug(self.task_list)
        for task_index, task in enumerate(self.task_list):
            if task in text:
                return task_index
        
        return -127


    def hei(self):
        print("Hey")
        # self.vocal_asistent.speak("Hey")
    

    def test(self):
        print("Mouse")
        # self.vocal_asistent.speak("Mouse")

    
    def apple(self):
        print("Apple")
        # self.vocal_asistent.speak("Apple")
    

    def goodbye(self):
        print("Goodbye")
        # self.vocal_asistent.speak("Goodbye")