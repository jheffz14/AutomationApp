import subprocess
import time
import pyautogui

print("1. Python started")



print("2. PyAutoGUI imported")

subprocess.Popen("notepad.exe")

print("3. Notepad opened")

time.sleep(2)

print("4. Typing...")

pyautogui.write("Hello World!")

print("5. Done")