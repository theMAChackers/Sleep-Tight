import pickle
from firebase import firebase
import pyautogui
import time

def join():
    id2 = pickle.load(open("jesi","rb"))
    X = firebase.get('/sleep-tight-8a6df/jssion/'+ str(id2) , 'X' )
    Y = firebase.get('/sleep-tight-8a6df/jssion/'+ str(id2) , 'Y' )
    pyautogui.click(X, Y)
    time.sleep(3)
    id2 = pickle.load(open("jesin","rb"))
    X = firebase.get('/sleep-tight-8a6df/jssion1/'+ str(id2) , 'X' )
    Y = firebase.get('/sleep-tight-8a6df/jssion1/'+ str(id2) , 'Y' )
    pyautogui.click(X, Y)

def space(sppp):
    for k in range(0, sppp):
         pyautogui.scroll(-100)

def slass(st):
    id2 = pickle.load(open(st+"1","rb"))
    CX = firebase.get('/sleep-tight-8a6df/'+st+'/'+ str(id2) , 'X' )
    CY = firebase.get('/sleep-tight-8a6df/'+st+'/'+ str(id2) , 'Y' )
    pyautogui.click(CX, CY)

firebase = firebase.FirebaseApplication('https://sleep-tight-8a6df.firebaseio.com/', None)


id2 = pickle.load(open("chrome","rb"))
X = firebase.get('/sleep-tight-8a6df/Chrome/'+ str(id2) , 'CX' )
Y = firebase.get('/sleep-tight-8a6df/Chrome/'+ str(id2) , 'CY' )
pyautogui.click(X, Y)

time.sleep(7)
pyautogui.write('https://cuchd.blackboard.com/ultra/course')
pyautogui.keyDown('enter')

time.sleep(10)
id2 = pickle.load(open("sign","rb"))
X = firebase.get('/sleep-tight-8a6df/signin/'+ str(id2) , 'SX' )
Y = firebase.get('/sleep-tight-8a6df/signin/'+ str(id2) , 'SY' )
pyautogui.click(X, Y)

time.sleep(15)

for j in range(0,3):
    if j == 0:
        st = "ELT"
    elif j==1:
        st="ELP"
    elif j==2:
        st="UCT"
    i = pickle.load(open(st,"rb"))
    sppp=int(i)
    space(sppp)
    time.sleep(2)
    slass(st)
    time.sleep(4)
    join()
    time.sleep(35)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(2)
    pyautogui.hotkey('alt', 'left')
    time.sleep(10)








