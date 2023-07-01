from vocal_assistant import *
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

x = Assistent("Helen", "female", 200)

x.speak(f"Hey there, my name is {x.get_name()}" )

sleep(0.5)
x.speak(f"Just say, Hey {x.get_name()}, and I'll see what I can do for you.")

task_class = 0

while True:
    text = x.get_audio().lower()
    task_number = x.task_manager.identify_task(text)
    logging.debug(task_number)
    x.run_task(task_number, text)