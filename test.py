# Impoting Pyautogui library to control the actions for your programme 
import pyautogui
import time
import pickle
from firebase import firebase

#Confirming already saved chrome png is working or not
firebase = firebase.FirebaseApplication('https://sleep-tight-8a6df.firebaseio.com/', None)

id2 = pickle.load(open("chrome","rb"))
X = firebase.get('/sleep-tight-8a6df/Chrome/'+ str(id2) , 'CX' )
Y = firebase.get('/sleep-tight-8a6df/Chrome/'+ str(id2) , 'CY' )
pyautogui.click(X, Y)
time.sleep(8)
pyautogui.write('https://cuchd.blackboard.com')
time.sleep(1)
pyautogui.keyDown('enter')
pyautogui.alert('After clicking ok move your mouse on signin and wait for another prompt.')
time.sleep(4)
currentMouseX, currentMouseY = pyautogui.position()


pyautogui.alert('Done!!!')

data =  { 
    'SX': currentMouseX,
    'SY': currentMouseY
    }
result = firebase.post('/sleep-tight-8a6df/signin/',data)
final = ''.join(key + str(val) for key, val in result.items())
data = str(final)
proxy = data[4:24]
pickle.dump(proxy, open("sign","wb"))
pyautogui.alert('Now Run test.py using the command given in github README.md file.')


""" 
if str(work_var) == 'YES':
    pyautogui.write('https://cuchd.blackboard.com')
    pyautogui.keyDown('enter')
    working = pyautogui.confirm('Does your blackboard started', buttons=['YES', 'NO'])    if str(working) == 'YES':
        id = pickle.load(open("name","rb"))
        email = firebase.get('/sleep-tight-8a6df/Students/'+ str(id) , 'Name' )
        pyautogui.write(email)
        password = firebase.get('/sleep-tight-8a6df/Students/'+ str(id) , 'RollNo' )
        pyautogui.keyDown('tab')
        pyautogui.write(password)
        pyautogui.keyDown('enter')
        pyautogui.alert('Your test file ends here')
    else:
        pyautogui.alert('Please pin chrome to taskbar and run the Programme.')
else:
    check = pyautogui.confirm('Is your chrome pinned to taskbar?', buttons=['YES', 'NO'])
    if str(check) == 'YES':
        print("okk")
    else:
        pyautogui.alert('Please pin chrome to taskbar and run the Programme once again.')
         """
