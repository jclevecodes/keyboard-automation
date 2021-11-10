'''
autotyper.py, by Joshua Cleveland, 2021-10-24
Automated keyboard typer
'''
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(5) #Alloted time to click on field where you want text placed

txtArr = [] #Empty array for storage of txt lines

'''
Initiation of file opening to store each individual line into array declared line #12.
'''
with open('file.txt') as file:
    txtArr = file.readlines()
    
counter = 0 #Incrementation variable

'''
Infinite traversion through txt file where each line is stored into "line" variable
and keystrokes for that specific word/phrase in the file are automated on the keyboard and 
placed into the text field being utilized then the enter key is being pressed to
create a new line for the next word/phrase.
'''
while True:
    for line in txtArr:
        counter += 1
        keyboard.type(line)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        #time.sleep(1) #Do not go lower than 1 second as it will most likely crash the program