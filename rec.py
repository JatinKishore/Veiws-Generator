import pyautogui as pg
import time
import webbrowser


link =input("Put your link here")
a=int(input("Enter how much veiws you need"))
webbrowser.open(link)
i = 0
while i<a:
    time.sleep(35)
    pg.click(104,62)
    i += 1



