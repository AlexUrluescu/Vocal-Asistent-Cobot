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

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

class Task():

    def __init__(self, assistant_name):
        self.task_list = [assistant_name, "open my presentation", "next", "previous", "weather", "time", "date", 'thank you', "minimize", "close", "open", "focus", "maximize", "mode", "finish", "say", "goodbye"]
        self.assistant_name = assistant_name
        self.keyboard = Controller()

        self.task_list2 = [assistant_name, "open my presentation", "next", "previous", "weather"]
        

    def identify_task(self, text: str) -> int:
        logging.debug("I am here")
        logging.debug(text)
        logging.debug(self.task_list)
        for task_index, task in enumerate(self.task_list):
            if task in text:
                return task_index
        
        return -127
    
       
    def loadwindowslist(self, hwnd, topwindows):
        topwindows.append((hwnd, win32gui.GetWindowText(hwnd)))
        
    
    def findandshowwindow(self, swinname, bshow, bbreak):
        topwindows = []

        win32gui.EnumWindows(self.loadwindowslist, topwindows)

        for hwin in topwindows:
            sappname = str(hwin[1])
            if swinname in sappname.lower():
                nhwnd = hwin[0]
                logging.debug(type(nhwnd))
                logging.debug(">>> Found: " + str(nhwnd) + ": " + sappname)
                if(bshow):
                    win32gui.ShowWindow(nhwnd, 5)
                    shell = win32com.client.Dispatch("WScript.Shell")
                    shell.SendKeys('%')
                    win32gui.SetForegroundWindow(nhwnd)
                if(bbreak):
                    break


    def focus(self, string):
        string = string.split(" ")[-1]
        lista = []

        windows = Desktop(backend="uia").windows()

        for w in windows:
            lista.append(w.window_text().lower())
            logging.debug(w.window_text())

        logging.debug(f"{lista} nr 1")
        logging.debug(string)

        # ---------- change the name of word and powerpoint -----------
        i=0

        while i < len(lista):
            logging.debug("a intrat in while")
            if("powerpoint" in lista[i]):
                lista[i] = "powerpoint"
                logging.debug("am gasit powerpoint")

            if("word" in lista[i]):
                lista[i] = "word"
                logging.debug("am gasit word")

            if("visual studio code" in lista[i]):
                lista[i] = "code"
                logging.debug("am gasit visual studio code")

            if("edge" in lista[i]):
                lista[i] = "microsoft"
                logging.debug("am gasit edge")

            if("WhatsApp" in lista[i]):
                lista[i] = "whatsapp"
                logging.debug('am gasit whatsapp')
        
            i=i+1

        # ---------------------------------------------------

        logging.debug(f"{lista} nr 2")

        if string in lista:
            self.findandshowwindow(string, True, True)
            logging.debug(f"{string} exist")

        else:
            logging.debug("doesn't exist")

    
    def open(self, string):
        
        string = string.split(" ")[-1]
        logging.debug("se executa functia open")

        if(string == "powerpoint"):
            logging.debug("a intrat in powerpoint")
            os.system("start powerpnt")

        if(string == "word"):
            logging.debugnt("a intrat in word")
            os.system("start winword")

        if(string == "microsoft"):
            logging.debug("a intrat in microsoft")
            os.system("start msedge")

        else:
            logging.debug(f"a intrat in {string}")
            run(string)
            logging.debug("notepad")


    def minimise(self):
        pyautogui.keyDown("win")
        pyautogui.keyDown("down")
        pyautogui.keyUp("down")
        pyautogui.keyUp("win")   
    

    def maximise(self):
        pyautogui.keyDown("win")
        pyautogui.keyDown("up")
        pyautogui.keyUp("up")
        pyautogui.keyUp("win")


    def open_my_presentation(self):
        logging.debug("open_mt_presentation is activ")

        path = "C:\projectsPowerPoint"
        files = os.listdir(path)
        lista = []

        for file in files:
            size = len(file)
            file = file[:size - 5]
            logging.debug(file)
            if "_" in file:
                file = file.replace("_", " ")
            lista.append(file)

        logging.debug(files)
        logging.debug(lista)

        return lista, path, files
    

    def presentation_mode(self):
        pyautogui.keyDown("win")
        pyautogui.keyDown("f5")
        pyautogui.keyUp("f5")
        pyautogui.keyUp("win")

    
    def finish_presentation(self):
        pyautogui.keyDown("esc")
        pyautogui.keyUp("esc")
        logging.debug("finish a mers")

    
    def close_file(self):
        logging.debug("Se executa functia close_file")
        sleep(1)

        # combination = {Key.alt, Key.f4}
        logging.debug("se inchide")
        self.keyboard.press(Key.alt)
        self.keyboard.press(Key.f4)
        self.keyboard.release(Key.alt)
        self.keyboard.release(Key.f4)
        logging.debug("s-a inchis")

    
    def next_slide(self):
        logging.debug("Se executa functia next_slide")
        # sleep(1)
        
        self.keyboard.press(Key.down)
        self.keyboard.release(Key.down)


    def previous_slide(self):
        logging.debug("Se executa functia previous_slide")
        # sleep(1)
        self.keyboard.press(Key.up)
        self.keyboard.release(Key.up)

    
    def weather(self, string):
        try:

            city = string.split(" ")[-1]
            logging.debug(f"Weather in {city}")

            api_key = "55c8bfaf9fff464f3bf6f3c283186dc6"
            weather_data = requests.get(
                    f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")
                
            weather_data.raise_for_status()
        
            weather_data = weather_data.json()

            logging.debug(weather_data)
            
            return weather_data

        except requests.exceptions.RequestException as error:
            logging.debug(f'HTTP error occurred: {error}')

        except Exception as error:
            logging.debug(f'Other error occurred: {error}')

    
    def time(self):
        logging.debug("Se executa functia time")
        now = datetime.now()
        ora = now.strftime("%H:%M")

        return ora
    

    def date(self):
        logging.debug("Se executa functia date")
        data = date.today()

        return data

    
    def thank_you(self):
        logging.debug("Se executa functia thank you")

    
    def say_something(self):
        logging.debug("Se executa functia say")
        run("notepad")

        sleep(2)

        pyautogui.keyDown("T")
        pyautogui.keyUp("T")
        pyautogui.keyDown("h")
        pyautogui.keyUp("h")
        pyautogui.keyDown("a")
        pyautogui.keyUp("a")
        pyautogui.keyDown("n")
        pyautogui.keyUp("n")
        pyautogui.keyDown("k")
        pyautogui.keyUp("k")
        pyautogui.keyDown(" ")
        pyautogui.keyUp(" ")
        pyautogui.keyDown("y")
        pyautogui.keyUp("y")
        pyautogui.keyDown("o")
        pyautogui.keyUp("o")
        pyautogui.keyDown("u")
        pyautogui.keyUp("u")
        pyautogui.keyDown(" ")
        pyautogui.keyUp(" ")
        pyautogui.keyDown("f")
        pyautogui.keyUp("f")
        pyautogui.keyDown("o")
        pyautogui.keyUp("o")
        pyautogui.keyDown("r")
        pyautogui.keyUp("r")
        pyautogui.keyDown(" ")
        pyautogui.keyUp(" ")
        pyautogui.keyDown("w")
        pyautogui.keyUp("w")
        pyautogui.keyDown("a")
        pyautogui.keyUp("a")
        pyautogui.keyDown("t")
        pyautogui.keyUp("t")
        pyautogui.keyDown("c")
        pyautogui.keyUp("c")
        pyautogui.keyDown("h")
        pyautogui.keyUp("h")
        pyautogui.keyDown("i")
        pyautogui.keyUp("i")
        pyautogui.keyDown("n")
        pyautogui.keyUp("n")
        pyautogui.keyDown("g")
        pyautogui.keyUp("g")
        pyautogui.keyDown(" ")
        pyautogui.keyUp(" ")
        pyautogui.keyDown("m")
        pyautogui.keyUp("m")
        pyautogui.keyDown("e")
        pyautogui.keyUp("e")
        pyautogui.keyDown(".")
        pyautogui.keyUp(".")
        pyautogui.keyDown(" ")
        pyautogui.keyUp(" ")
        pyautogui.keyDown("I")
        pyautogui.keyUp("I")
        pyautogui.keyDown(" ")
        pyautogui.keyUp(" ")
        pyautogui.keyDown("s")
        pyautogui.keyUp("s")
        pyautogui.keyDown("e")
        pyautogui.keyUp("e")
        pyautogui.keyDown("e")
        pyautogui.keyUp("e")
        pyautogui.keyDown(" ")
        pyautogui.keyUp(" ")
        pyautogui.keyDown("y")
        pyautogui.keyUp("y")
        pyautogui.keyDown("o")
        pyautogui.keyUp("o")
        pyautogui.keyDown("u")
        pyautogui.keyUp("u")
        pyautogui.keyDown(" ")
        pyautogui.keyUp(" ")
        pyautogui.keyDown("n")
        pyautogui.keyUp("n")
        pyautogui.keyDown("e")
        pyautogui.keyUp("e")
        pyautogui.keyDown("x")
        pyautogui.keyUp("x")
        pyautogui.keyDown("t")
        pyautogui.keyUp("t")
        pyautogui.keyDown(" ")
        pyautogui.keyUp(" ")
        pyautogui.keyDown("y")
        pyautogui.keyUp("y")
        pyautogui.keyDown("e")
        pyautogui.keyUp("e")
        pyautogui.keyDown("a")
        pyautogui.keyUp("a")
        pyautogui.keyDown("r")
        pyautogui.keyUp("r")
        pyautogui.keyDown("!")
        pyautogui.keyUp("!")

    
    def goodbye(self):
        logging.debug("Se executa functia goodbye")