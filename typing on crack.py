from pynput.keyboard import Controller, Key, Listener
from pynput import mouse
import time
import pyscreenshot
import pytesseract
import keyboard
import winsound

pytesseract.pytesseract.tesseract_cmd = r'E:\tesseract\tesseract.exe'
#getting the area for the screenshot
keyboard.wait("esc")


frequency = 300   # Set Frequency To 2500 Hertz
duration = 250  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)
def on_click(x, y, button, pressed):
    if pressed:
        on_click.px = x
        on_click.py = y
    else:
        on_click.rx = x
        on_click.ry = y
    
    if not pressed:
        return False


with mouse.Listener(on_click=on_click) as listener:
    listener.join()

img = pyscreenshot.grab(bbox = (on_click.px, on_click.py, on_click.rx, on_click.ry))
img.save("img.png")

txt = str(pytesseract.image_to_string(img, lang = "eng")).replace("|", "I")
txt.replace("‘", "'")
txt = " ".join(txt.splitlines())
print(txt)
winsound.Beep(frequency, duration)
keyboard = Controller()


#typing when numlock is pressed
def on_press(key): 

    if key == Key.num_lock:
        winsound.Beep(frequency, duration)
        for i in txt:
            keyboard.press(i)
            keyboard.release(i)
            time.sleep(0.05)
    

with Listener(on_press=on_press) as listener:
    listener.join()
