import keyboard
import mouse
import time
import sys

def info():
    print("Начальное значение CPS: 25")
    print("Нажми на Alt чтобы включить и выключить")
    print("Нажми на r + t  чтобы изменить CPS")
    return

isClicking = False
cps_click = 0.070

def cps():
    global cps_click
    print("Если ввести значение больше 50 CPS, то автокликер будет выдавать 110 CPS")
    
    while True:
        try:
            value = int(input("Введите CPS значение: "))
            break
        except ValueError:
            print("Ошибка попробуйте ещё раз!")
    
    if value >= 50:
        cps_click = 0.015
        print("CPS изменен. Можно запускать автокликер")
        return
    elif (value >= 45) and (value < 50):
        cps_click = 0.040
        print("CPS изменен. Можно запускать автокликер")
        return
    elif (value >= 40) and (value < 45):
        cps_click = 0.043
        print("CPS изменен. Можно запускать автокликер")
        return
    elif (value >= 35) and (value < 40):
        cps_click = 0.050
        print("CPS изменен. Можно запускать автокликер")
        return
    elif (value >= 30) and (value < 35):
        cps_click = 0.060
        print("CPS изменен. Можно запускать автокликер")
        return
    elif (value >= 25) and (value < 30):
        cps_click = 0.070
        print("CPS изменен. Можно запускать автокликер")
        return
    elif (value >= 20) and (value < 25):
        cps_click = 0.080
        print("CPS изменен. Можно запускать автокликер")
        return
    elif (value >= 15) and (value < 20):
        cps_click = 0.090
        print("CPS изменен. Можно запускать автокликер")
        return
    elif (value > 10) and (value < 15):
        cps_click = 0.1
        print("CPS изменен. Можно запускать автокликер")
        return
    elif value == 10:
        cps_click = 0.19
        print("CPS изменен. Можно запускать автокликер")
        return
    elif (value > 5) and (value < 10):
        cps_click = 0.27
        print("CPS изменен. Можно запускать автокликер")
        return
    elif value <= 5:
        cps_click = 0.38
        print("CPS изменен. Можно запускать автокликер")
        return

def set_clicker():
    global isClicking
    if isClicking:
        isClicking = False
        print("откл.") 
    else:
        isClicking = True
        print('вкл.')
        
info()
keyboard.add_hotkey("r + t", cps)

keyboard.add_hotkey("Alt", set_clicker)
keyboard.add_hotkey("Alt + w", set_clicker)
keyboard.add_hotkey("Alt + w + Ctrl", set_clicker)
keyboard.add_hotkey("Alt + w + Shift + Ctrl", set_clicker)
keyboard.add_hotkey("Alt + w + Shift + d + Ctrl", set_clicker)
keyboard.add_hotkey("Alt + w + Shift + a + Ctrl", set_clicker)

   
while True:
    if isClicking:
        mouse.double_click(button= "left")
        time.sleep(cps_click)