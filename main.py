# import Clasa Asistent 
from vocal_assistant import *

# importam biblioteca logging pentru a printa in terminal
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

# Cream obiectul Asistent (numw,tip,viteza vorbire)
asistent = Assistent("Helen", "female", 200)

# Folosim metoda speak ca sa vorbeasca
asistent.speak(f"Hey there, my name is {asistent.get_name()}" )

#facem o mica pauza in vorbire intre propoziti
sleep(0.5)
asistent.speak(f"Just say, Hey {asistent.get_name()}, and I'll see what I can do for you.")

task_class = 0

#ascultam in continuu pana prindem un cuvant pe care il stim 
while True:
    text = asistent.get_audio().lower()
    task_number = asistent.task_manager.identify_task(text)
    logging.debug(task_number)
    asistent.run_task(task_number, text)