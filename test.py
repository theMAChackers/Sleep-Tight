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

pyautogui.alert('Take a screenshot of chrome and save and replace it in the img folder by chrome.png name, and also pin the chrome to taskbar!!! After saving chrome.png press ok')
buttonx, buttony = pyautogui.locateCenterOnScreen('img/chrome.png') 
pyautogui.click(buttonx, buttony)
time.sleep(5)
work_var = pyautogui.confirm('Does your Chrome started', buttons=['YES', 'NO'])
if str(work_var) == 'YES':
    pyautogui.write('https://cuchd.blackboard.com')
    pyautogui.keyDown('enter')
    working = pyautogui.confirm('Does your blackboard started', buttons=['YES', 'NO'])
    if str(working) == 'YES':
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
        
