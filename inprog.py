import pyautogui
import time
import calendar
import datetime

def findDay(date): 
    day, month, year = (int(i) for i in date.split(' '))     
    dayNumber = calendar.weekday(year, month, day) 
    days =["Monday", "Tuesday", "Wednesday", "Thursday", 
                        "Friday", "Saturday", "Sunday"] 
    return (days[dayNumber]) 

def ELT():
    pyautogui.moveTo(300, 450)
    pyautogui.click()
    time.sleep(4)
    pyautogui.moveTo(200, 500)
    pyautogui.click()
    pyautogui.moveTo(200, 530)
    pyautogui.click()

def ELP():
    pyautogui.moveTo(700, 450)
    pyautogui.click()
    time.sleep(4)
    pyautogui.moveTo(200, 500)
    pyautogui.click()
    pyautogui.moveTo(200, 530)
    pyautogui.click()

def UCT():
    pyautogui.moveTo(1100, 450)
    pyautogui.click()
    time.sleep(4)
    pyautogui.moveTo(200, 500)
    pyautogui.click() 
    pyautogui.moveTo(200, 530)
    pyautogui.click() 

def space1():
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")

def UCP():
    pyautogui.moveTo(300, 450)
    pyautogui.click()
    time.sleep(4)
    pyautogui.moveTo(200, 500)
    pyautogui.click()
    pyautogui.moveTo(200, 530)
    pyautogui.click()

def SMT():
    pyautogui.moveTo(700, 450)
    pyautogui.click()
    time.sleep(4)
    pyautogui.moveTo(200, 500)
    pyautogui.click()
    pyautogui.moveTo(200, 530)
    pyautogui.click()

def MEP():
    pyautogui.moveTo(1100, 450)
    pyautogui.click()
    time.sleep(4)
    pyautogui.moveTo(200, 500)
    pyautogui.click() 
    pyautogui.moveTo(200, 530)
    pyautogui.click() 

def space2():
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")

def ECP():
    pyautogui.moveTo(300, 450)
    pyautogui.click()
    time.sleep(4)
    pyautogui.moveTo(200, 500)
    pyautogui.click()
    pyautogui.moveTo(200, 530)
    pyautogui.click()

def UCY():
    pyautogui.moveTo(700, 450)
    pyautogui.click()
    time.sleep(4)
    pyautogui.moveTo(200, 500)
    pyautogui.click()
    pyautogui.moveTo(200, 530)
    pyautogui.click()

def CST():
    pyautogui.moveTo(1100, 450)
    pyautogui.click()
    time.sleep(4)
    pyautogui.moveTo(200, 500)
    pyautogui.click() 
    pyautogui.moveTo(200, 530)
    pyautogui.click()  

def space3():
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")
    pyautogui.keyDown("down")

def CSP():
    pyautogui.moveTo(300, 450)
    pyautogui.click()
    time.sleep(4)
    pyautogui.moveTo(200, 500)
    pyautogui.click()
    pyautogui.moveTo(200, 530)
    pyautogui.click()

def SPT():
    pyautogui.moveTo(700, 450)
    pyautogui.click()
    time.sleep(4)
    pyautogui.moveTo(200, 500)
    pyautogui.click()
    pyautogui.moveTo(200, 530)
    pyautogui.click()

def SPP():
    pyautogui.moveTo(1100, 450)
    pyautogui.click()
    time.sleep(4)
    pyautogui.moveTo(200, 500)
    pyautogui.click() 
    pyautogui.moveTo(200, 530)
    pyautogui.click()  

current_time = datetime.datetime.now()
year = str(current_time.year)
month = str(current_time.month)
day = str(current_time.day)
date = (day+' '+month+' '+year)
#date = '03 02 2019'
#print(findDay(date)) 
time.sleep(3)
pyautogui.moveTo(160, 870)
pyautogui.click()
pyautogui.keyDown('c')
pyautogui.keyDown('u')
pyautogui.keyDown('c')
pyautogui.keyDown('h')
pyautogui.keyDown('d')
time.sleep(1)
pyautogui.keyDown("return")
time.sleep(2)
pyautogui.keyDown("down")
pyautogui.keyDown("return")
pyautogui.keyDown("return")
time.sleep(5)
n= input()
timetable={}
for i in range(n):
    name = input()
    data = input()
    timetable[name] = data

for name, data in timetable.items():
    if data == date:
        print(data)

for i in range(date)
    if date == data:
        ELT()


