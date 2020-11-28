from firebase import firebase
import pyautogui
import pickle
import time

def space(str, i):
    opt = pyautogui.confirm('Is ' + str + ' Visbile?? And please dont scroll', buttons=['YES', 'NO'])
    if str(opt) == 'YES':
        return i
    else:
        i=i+1
        pyautogui.keyDown("down")
        space(str, i)

def classes(str):
    pyautogui.alert('After clicking ok without scrolling move your mouse on ' + str + ' and wait for another prompt.')
    time.sleep(4)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.alert('Done!!!')

    data =  { 
        'X': currentMouseX,
        'Y': currentMouseY
        }
    result = firebase.post('/sleep-tight-8a6df/'+str+'/',data)
    final = ''.join(key + str(val) for key, val in result.items())
    data = str(final)
    proxy = data[4:24]
    pickle.dump(proxy, open(str,"wb"))

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


i=0
str = "ELT"
sp = space(str, i)
pickle.dump(sp, open(str,"wb"))
classes(str)

i=0
str = "ELP"
sp = space(str, i)
pickle.dump(sp, open(str,"wb"))
classes(str)

i=0
str = "UCT"
ELTPSP = space(str, i)
pickle.dump(sp, open(str,"wb"))
classes(str)

i=0
str = "UCP"
ELTPSP = space(str, i)
pickle.dump(sp, open(str,"wb"))
classes(str)

i=0
str = "SMT"
ELTPSP = space(str, i)
pickle.dump(sp, open(str,"wb"))
classes(str)

i=0
str = "MEP"
ELTPSP = space(str, i)
pickle.dump(sp, open(str,"wb"))
classes(str)

i=0
str = "ECP"
ELTPSP = space(str, i)
pickle.dump(sp, open(str,"wb"))
classes(str)

i=0
str = "UCY"
ELTPSP = space(str, i)
pickle.dump(sp, open(str,"wb"))
classes(str)

i=0
str = "CST"
ELTPSP = space(str, i)
pickle.dump(sp, open(str,"wb"))
classes(str)

pyautogui.alert('Now Run calendar.py using the command given in github README.md file.')



    

