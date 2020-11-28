from firebase import firebase
import pyautogui
import pickle
import time

def space(st, i):
    opt = pyautogui.confirm('Is ' + st + ' Visbile?? And please dont scroll', buttons=['YES', 'NO'])
    if str(opt) == 'YES':
        return i
    else:
        X = 500
        Y = 15
        pyautogui.click(X, Y)
        i=i+1
        time.sleep(2)
        pyautogui.keyDown("down")
        time.sleep(2)
        space(st, i)

def classes(st):
    pyautogui.alert('After clicking ok without scrolling move your mouse on ' + st + ' and wait for another prompt.')
    time.sleep(4)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.alert('Done!!!')

    data =  { 
        'X': currentMouseX,
        'Y': currentMouseY
        }
    result = firebase.post('/sleep-tight-8a6df/'+st+'/',data)
    final = ''.join(key + str(val) for key, val in result.items())
    data = str(final)
    proxy = data[4:24]
    pickle.dump(proxy, open(st,"wb"))

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
st = "ELT"
sp = space(st, i)
pickle.dump(sp, open(st,"wb"))
classes(st)

i=0
st = "ELP"
sp = space(st, i)
pickle.dump(sp, open(st,"wb"))
classes(st)

i=0
st = "UCT"
sp = space(st, i)
pickle.dump(sp, open(st,"wb"))
classes(st)

i=0
st = "UCP"
sp = space(st, i)
pickle.dump(sp, open(st,"wb"))
classes(st)

i=0
st = "SMT"
sp = space(st, i)
pickle.dump(sp, open(st,"wb"))
classes(st)

i=0
st = "MEP"
sp = space(st, i)
pickle.dump(sp, open(st,"wb"))
classes(st)

i=0
st = "ECP"
sp = space(st, i)
pickle.dump(sp, open(st,"wb"))
classes(st)

i=0
st = "UCY"
sp = space(st, i)
pickle.dump(sp, open(st,"wb"))
classes(st)

i=0
st = "CST"
sp = space(st, i)
pickle.dump(sp, open(st,"wb"))
classes(st)



pyautogui.alert('Now Run calendar.py using the command given in github README.md file.')



    

