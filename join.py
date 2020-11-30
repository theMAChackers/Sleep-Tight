import pickle
from firebase import firebase
import pyautogui
import time

def space(saq):
    for j in range(0, saq):
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

time.sleep(5)
pyautogui.write('https://cuchd.blackboard.com/ultra/course')
pyautogui.keyDown('enter')

time.sleep(10)
id2 = pickle.load(open("sign","rb"))
X = firebase.get('/sleep-tight-8a6df/signin/'+ str(id2) , 'SX' )
Y = firebase.get('/sleep-tight-8a6df/signin/'+ str(id2) , 'SY' )
pyautogui.click(X, Y)

time.sleep(15)

st = "ELT"
i = pickle.load(open(st,"rb"))
saq = int(i)
space(saq)
slass(st)

pyautogui.alert('After clicking ok move your mouse on join session and wait for another prompt.')
time.sleep(4)
currentMouseX, currentMouseY = pyautogui.position()


pyautogui.alert('Done!!!')
time.sleep(2)
pyautogui.click(currentMouseX, currentMouseY)

data =  { 
    'X': currentMouseX,
    'Y': currentMouseY
    }
result = firebase.post('/sleep-tight-8a6df/jssion/',data)
final = ''.join(key + str(val) for key, val in result.items())
data = str(final)
proxy = data[4:24]
pickle.dump(proxy, open("jesi","wb"))



pyautogui.alert('After clicking ok move your mouse on course room and wait for another prompt.')
time.sleep(4)
currentMouseX, currentMouseY = pyautogui.position()


pyautogui.alert('Done!!!')
time.sleep(2)

data =  { 
    'X': currentMouseX,
    'Y': currentMouseY
    }
result = firebase.post('/sleep-tight-8a6df/jssion1/',data)
final = ''.join(key + str(val) for key, val in result.items())
data = str(final)
proxy = data[4:24]
pickle.dump(proxy, open("jesin","wb"))
pyautogui.alert('Now Run tropy.py using the command given in github README.md file.')