from firebase import firebase
import pyautogui
import pickle
import time


firebase = firebase.FirebaseApplication('https://sleep-tight-8a6df.firebaseio.com/', None)
email= pyautogui.prompt('Email')
passw= pyautogui.prompt('Pass')
data =  { 
    'Name': email,
    'RollNo': passw
}
result = firebase.post('/sleep-tight-8a6df/Students/',data)
final = ''.join(key + str(val) for key, val in result.items())
data = str(final)
proxy = data[4:24]
pickle.dump(proxy, open("name","wb"))
id = pickle.load(open("name","rb"))
time.sleep(8)
email = firebase.get('/sleep-tight-8a6df/Students/'+ str(id) , 'Name' )
confirm = pyautogui.confirm('Is this your Email Id: '+ str(email), buttons=['YES', 'NO'])
if str(confirm)=='YES':
    pyautogui.alert('Now Run test.py using the command given in github README.md file.')
else:
    pyautogui.alert('Please copy the error code and raise a issue in the repository by pasting the error and the file name.')
