import pyautogui
import time

def cross():
    button9location = pyautogui.locateOnScreen('cross.png')
    button9location
    buttonx, buttony = pyautogui.center(button9location)
    buttonx, buttony
    pyautogui.click(buttonx, buttony)

def tab():
    time.sleep(3)
    button3333location = pyautogui.locateOnScreen('course tab.png')
    button3333location
    buttonx, buttony = pyautogui.center(button3333location)
    buttonx, buttony
    pyautogui.click(buttonx, buttony)

def join():
    time.sleep(6)
    button13location = pyautogui.locateOnScreen('join session.png')
    button13location
    buttonx, buttony = pyautogui.center(button13location)
    buttonx, buttony
    pyautogui.click(buttonx, buttony)

    time.sleep(3)
    button14location = pyautogui.locateOnScreen('course room.png')
    button14location
    buttonx, buttony = pyautogui.center(button14location)
    buttonx, buttony
    pyautogui.click(buttonx, buttony)

def leave():
    button1234location = pyautogui.locateOnScreen('for leave.png')
    button1234location
    buttonx, buttony = pyautogui.center(button1234location)
    buttonx, buttony
    pyautogui.click(buttonx, buttony)

    time.sleep(3)
    button2345location = pyautogui.locateOnScreen('leave session.png')
    button2345location
    buttonx, buttony = pyautogui.center(button2345location)
    buttonx, buttony
    pyautogui.click(buttonx, buttony)

    time.sleep(2)
    button3456location = pyautogui.locateOnScreen('skip.png')
    button3456location
    buttonx, buttony = pyautogui.center(button3456location)
    buttonx, buttony
    pyautogui.click(buttonx, buttony)

def UCT():
    time.sleep(2)
    button411location = pyautogui.locateOnScreen('pagepoint.png')
    button411location
    buttonx, buttony = pyautogui.center(button411location)
    buttonx, buttony
    pyautogui.click(buttonx, buttony)

    time.sleep(2)
    pyautogui.scroll(800)

    time.sleep(1)
    button66location = pyautogui.locateOnScreen('communication.png')
    button66location
    buttonx, buttony = pyautogui.center(button66location)
    buttonx, buttony
    pyautogui.click(buttonx, buttony)

def SPT():
    time.sleep(2)
    button41location = pyautogui.locateOnScreen('pagepoint.png')
    button41location
    buttonx, buttony = pyautogui.center(button41location)
    buttonx, buttony
    pyautogui.click(buttonx, buttony)

    time.sleep(2)
    pyautogui.scroll(-800)

    time.sleep(1)
    button42location = pyautogui.locateOnScreen('quantum.png')
    button42location
    buttonx, buttony = pyautogui.center(button42location)
    buttonx, buttony
    pyautogui.click(buttonx, buttony)
 

def ELT():
    time.sleep(2)
    button1112location = pyautogui.locateOnScreen('pagepoint.png')
    button1112location
    buttonx, buttony = pyautogui.center(button1112location)
    buttonx, buttony
    pyautogui.click(buttonx, buttony)

    time.sleep(2)
    pyautogui.scroll(250)
    time.sleep(1)
    button1222location = pyautogui.locateOnScreen('physics electronic.png')
    button1222location
    buttonx, buttony = pyautogui.center(button1222location)
    buttonx, buttony
    pyautogui.click(buttonx, buttony)

def SMT():

    time.sleep(2)
    button5location = pyautogui.locateOnScreen('maths.png')
    button5location
    buttonx, buttony = pyautogui.center(button5location)
    buttonx, buttony
    pyautogui.click(buttonx, buttony)

def MEP():
    time.sleep(2)
    button11location = pyautogui.locateOnScreen('pagepoint.png')
    button11location
    buttonx, buttony = pyautogui.center(button11location)
    buttonx, buttony
    pyautogui.click(buttonx, buttony)

    time.sleep(2)
    pyautogui.scroll(-400)

    time.sleep(1)
    button12location = pyautogui.locateOnScreen('autocad.png')
    button12location
    buttonx, buttony = pyautogui.center(button12location)
    buttonx, buttony
    pyautogui.click(buttonx, buttony)

button7location = pyautogui.locateOnScreen('chrome.png')
button7location
buttonx, buttony = pyautogui.center(button7location)
buttonx, buttony
pyautogui.click(buttonx, buttony)

time.sleep(2)
pyautogui.write('https://cuchd.blackboard.com/ultra/course')
pyautogui.keyDown('enter')

time.sleep(10)
button8location = pyautogui.locateOnScreen('signin.png')
button8location
buttonx, buttony = pyautogui.center(button8location)
buttonx, buttony
pyautogui.click(buttonx, buttony)

time.sleep(6)
cross()

time.sleep(8)
button10location = pyautogui.locateOnScreen('course.png')
button10location
buttonx, buttony = pyautogui.center(button10location)
buttonx, buttony
pyautogui.click(buttonx, buttony)

#friday

#autocad
MEP()
join()
time.sleep(15)
leave()
tab()
cross()

#maths
SMT()
join()
time.sleep(15)
leave()
tab()
cross()
 
#quantum and semiconductor
SPT()
join()
time.sleep(15)
leave()
tab()
cross()


#communication skills
UCT()
join()
time.sleep(15)
leave()
tab()
cross()

#basic electric and electronic engineering
ELT()
join()
time.sleep(15)
leave()
tab()
cross()








