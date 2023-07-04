# import Clasa Asistent 
from vocal_assistant import *

# importam biblioteca logging pentru a printa in terminala
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

# Cream obiectul Asistent
asistent = Assistent("Helen", "female", 200)

# Folosim metoda speak ca sa vorbeasca
asistent.speak(f"Hey there, my name is {asistent.get_name()}" )

sleep(0.5)
asistent.speak(f"Just say, Hey {asistent.get_name()}, and I'll see what I can do for you.")

task_class = 0

while True:
    text = asistent.get_audio().lower()
    task_number = asistent.task_manager.identify_task(text)
    logging.debug(task_number)
    asistent.run_task(task_number, text)