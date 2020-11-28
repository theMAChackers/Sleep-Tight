# Impoting Pyautogui library to control the actions for your programme 
import pyautogui
import time
import pickle
from firebase import firebase

#Confirming already saved chrome png is working or not
firebase = firebase.FirebaseApplication('https://sleep-tight-8a6df.firebaseio.com/', None)

""" email= pyautogui.prompt('Enter your BB Email')
passw= pyautogui.prompt('Enter your BB Pass')
data =  { 
    'Name': email,
    'RollNo': passw
}
result = firebase.post('/sleep-tight-8a6df/Students/',data)
pyautogui.alert('Please copy and paste the name given in next window')
res = pyautogui.prompt(result)
pickle.dump(res, open("name","wb")) """

id2 = pickle.load(open("chrome","rb"))
X = firebase.get('/sleep-tight-8a6df/Chrome/'+ str(id2) , 'CX' )
Y = firebase.get('/sleep-tight-8a6df/Chrome/'+ str(id2) , 'CY' )
pyautogui.click(X, Y)
time.sleep(5)
pyautogui.write('https://cuchd.blackboard.com')
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
pyautogui.alert('Please copy and paste the name in prompt')
res = pyautogui.prompt(result)
pickle.dump(res, open("sign","wb"))
id = pickle.load(open("sign","rb"))
time.sleep(8)
SX = firebase.get('/sleep-tight-8a6df/signin/'+ str(id) , 'SX' )
confirm = pyautogui.confirm('Is this your Email Id: '+ str(SX), buttons=['YES', 'NO'])
if str(confirm)=='YES':
    pyautogui.alert('Now Run test.py using the command given in github README.md file.')
else:
    pyautogui.alert('Please copy the error code and raise a issue in the repository by pasting the error and the file name.')


""" work_var = pyautogui.confirm('Does your Chrome started', buttons=['YES', 'NO'])
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
