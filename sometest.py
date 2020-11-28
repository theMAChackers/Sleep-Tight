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
    'TX': currentMouseX,
    'TY': currentMouseY
    }
result = firebase.post('/sleep-tight-8a6df/test/',data)
final = ''.join(key + str(val) for key, val in result.items())
data = str(final)
proxy = data[4:23]
pickle.dump(proxy, open("chrome","wb"))
id = pickle.load(open("chrome","rb"))
time.sleep(8)
CX = firebase.get('/sleep-tight-8a6df/test/'+ str(id) , 'TX' )
confirm = pyautogui.confirm('Is this your Email Id: '+ str(CX), buttons=['YES', 'NO'])
if str(confirm)=='YES':
    pyautogui.alert('Now Run test.py using the command given in github README.md file.')
else:
    pyautogui.alert('Please copy the error code and raise a issue in the repository by pasting the error and the file name.')
