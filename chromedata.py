from firebase import firebase
import pyautogui
import pickle
import time


firebase = firebase.FirebaseApplication('https://sleep-tight-8a6df.firebaseio.com/', None)
pyautogui.alert('After clicking ok move your mouse on chrome and wait for another prompt.')
time.sleep(4)
currentMouseX, currentMouseY = pyautogui.position()


pyautogui.alert('Done!!!')

data =  { 
    'CX': currentMouseX,
    'CY': currentMouseY
    }
result = firebase.post('/sleep-tight-8a6df/Chrome/',data)
final = ''.join(key + str(val) for key, val in result.items())
data = str(final)
proxy = data[4:24]
pickle.dump(proxy, open("chrome","wb"))
pyautogui.alert('Now Run test.py using the command given in github README.md file.')
