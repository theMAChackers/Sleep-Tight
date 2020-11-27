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
pyautogui.alert('Please copy and paste the name in prompt')
res = pyautogui.prompt(result)
pickle.dump(res, open("name","wb"))
id = pickle.load(open("name","rb"))
time.sleep(8)
email = firebase.get('/sleep-tight-8a6df/Students/'+ str(id) , 'Name' )
pyautogui.alert(email)
