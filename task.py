"""Class that models the tasks the assistant can do"""
from pynput.keyboard import Controller
from time import sleep
import os
from pywinauto import Desktop
import os.path
import logging
# from vocal_assistant import Assistent

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


class Task():
    #setare cuvinte pentru actiunile cobotului 
    def __init__(self, assistant_name):
        self.task_list = [assistant_name, "hey", "car", "apple", "goodbye"]
        self.assistant_name = assistant_name

        # self.vocal_asistent = Assistent()
        

    def identify_task(self, text: str) -> int:
        logging.debug("I am here")
        logging.debug(text)
        logging.debug(self.task_list)
        for task_index, task in enumerate(self.task_list):
            if task in text:
                return task_index
        
        return -127

