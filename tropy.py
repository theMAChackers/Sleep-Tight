import pickle
from firebase import firebase
import pyautogui
import time

def cross():
    button9location = pyautogui.locateOnScreen("img/cross.png")
    button9location
    buttonx, buttony = pyautogui.center(button9location)
    buttonx, buttony
    pyautogui.click(buttonx, buttony)

def join():
    id2 = pickle.load(open("jesi","rb"))
    X = firebase.get('/sleep-tight-8a6df/jssion/'+ str(id2) , 'X' )
    Y = firebase.get('/sleep-tight-8a6df/jssion/'+ str(id2) , 'Y' )
    pyautogui.click(X, Y)

    id2 = pickle.load(open("jesin","rb"))
    X = firebase.get('/sleep-tight-8a6df/jssion1/'+ str(id2) , 'X' )
    Y = firebase.get('/sleep-tight-8a6df/jssion1/'+ str(id2) , 'Y' )
    pyautogui.click(X, Y)

def leave():
    button1234location = pyautogui.locateOnScreen("img/for leave.png")
    button1234location
    buttonx, buttony = pyautogui.center(button1234location)
    buttonx, buttony
    pyautogui.click(buttonx, buttony)

    time.sleep(3)
    button2345location = pyautogui.locateOnScreen("img/leave session.png")
    button2345location
    buttonx, buttony = pyautogui.center(button2345location)
    buttonx, buttony
    pyautogui.click(buttonx, buttony)

    time.sleep(2)
    button3456location = pyautogui.locateOnScreen("img/skip.png")
    button3456location
    buttonx, buttony = pyautogui.center(button3456location)
    buttonx, buttony
    pyautogui.click(buttonx, buttony)

def space(i):
    for j in range(0, i):
         pyautogui.scroll(-100)

def slass(st):
    id2 = pickle.load(open(st,"rb"))
    CX = firebase.get('/sleep-tight-8a6df/signin/'+st+'/'+ str(id2) , 'X' )
    CY = firebase.get('/sleep-tight-8a6df/signin/'+st+'/'+ str(id2) , 'Y' )
    pyautogui.click(CX, CY)

firebase = firebase.FirebaseApplication('https://sleep-tight-8a6df.firebaseio.com/', None)


id2 = pickle.load(open("chrome","rb"))
X = firebase.get('/sleep-tight-8a6df/Chrome/'+ str(id2) , 'CX' )
Y = firebase.get('/sleep-tight-8a6df/Chrome/'+ str(id2) , 'CY' )
pyautogui.click(X, Y)

time.sleep(2)
pyautogui.write('https://cuchd.blackboard.com/ultra/course')
pyautogui.keyDown('enter')

time.sleep(10)
id2 = pickle.load(open("sign","rb"))
X = firebase.get('/sleep-tight-8a6df/signin/'+ str(id2) , 'SX' )
Y = firebase.get('/sleep-tight-8a6df/signin/'+ str(id2) , 'SY' )
pyautogui.click(X, Y)

time.sleep(15)

for j in range(0,6)
    st = "ELT"
    i = pickle.load(open(st,"rb"))
    space(i)
    slass(st)
    join()
    pyautogui.hotkey('alt', 'left')








