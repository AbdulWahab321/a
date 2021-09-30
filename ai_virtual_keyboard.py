
import os
def install(package):
    os.system(f"pip install {package}")

try:
    import cv2
    from tkinter import *
    from cvzone.HandTrackingModule import HandDetector
    from time import sleep
    import numpy as np
    import cvzone

    from pynput.keyboard import Controller, Key
    from pynput import keyboard as KEYBOARD
except:
    print("Installing Dependencies Please wait")

try:
    import tkinter
except:
    install("tkinter")

try:
    import cv2
except:
    install("cv2")

try:
    import cvzone
except:
    install("cvzone")

try:
    import time
except:
    install("time")

try:
    import numpy
except:
    install("numpy")

try:
    import pynput
except:
    install("pynput")

try:
    import cv2
    from tkinter import *
    from cvzone.HandTrackingModule import HandDetector
    from time import sleep
    import numpy as np
    import cvzone

    from pynput.keyboard import Controller,Key
    from pynput import keyboard as KEYBOARD
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)

    initial_colour =  (240,230,320)

    colour_when_clicked = (255,85,75)

    text_initial_colour = (90,95,100)

    text_clicked_colour = (95,90,105)


    detector = HandDetector(detectionCon=0.8)
    keys = [
            ["Tab"],["Backspace"],["Exit"],
            ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
            ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
            ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"],
            ["Space"],
           ]
    finalText = ""

    keyboard = Controller()

    def drawAll(img, buttonList):
        for button in buttonList:
            if button.text != "Space":
                x, y = button.pos
                w, h = button.size
                cvzone.cornerRect(img, (button.pos[0], button.pos[1], button.size[0], button.size[1]),
                                  20, rt=0)

                cv2.rectangle(img, button.pos, (x + w, y + h), initial_colour, cv2.FILLED)
                cv2.putText(img, button.text, (x + 20, y + 65),
                        cv2.FONT_HERSHEY_PLAIN, 4, text_initial_colour, 4)
            elif button.text == "Tab":
                keyboard.tap(Key.tab)
                cv2.rectangle(img, button.pos, (x + w, y + h+15), initial_colour, cv2.FILLED)
                cv2.putText(img, button.text, (x + 20, y + 75),
                        cv2.FONT_HERSHEY_PLAIN, 4,text_clicked_colour, 4)
            elif button.text == "Backspace":
                keyboard.tap(Key.backspace)
                cv2.rectangle(img, button.pos, (x + w, y + h+15), initial_colour, cv2.FILLED)
                cv2.putText(img, button.text, (x + 20, y + 75),
                        cv2.FONT_HERSHEY_PLAIN, 4,text_clicked_colour, 4)
            else:
                x, y = button.pos
                w, h = button.size
                cvzone.cornerRect(img, (button.pos[0], button.pos[1], button.size[0], button.size[1]),
                                  20, rt=0)
                cv2.rectangle(img, button.pos, (x + w, y + h), initial_colour, cv2.FILLED)
                cv2.putText(img, button.text, (x + 400, y + 65),
                        cv2.FONT_HERSHEY_PLAIN, 4, text_initial_colour, 4)
        return img


    class Help:
        def __init__(self):
            pass
        def show(self):
            from tkinter import Button as Btn
            root = Tk(className="Help Window")


            Label(text='To Press A key Knock your middle finger and index finger').pack()
            Label(text='To adjust the distance between them you can go to Settings').pack()
            def destroyAndstart():
                root.destroy()
                Start()
            Btn(command = lambda:    destroyAndstart(),text="Continue",bg="white",fg="black").pack()

            root.mainloop()
    class Button():
        def __init__(self, pos, text, size=[85, 85]):
            if text == "Space":
                self.pos = pos
                self.text = text
                self.size = [975,85]
            elif text == "Tab":
                self.pos = pos
                self.text = text
                self.size = [305,85]
            elif text == "Backspace":
                self.pos = [370,50]
                self.text = text
                self.size = [360,85]
            elif text == "Exit":
                self.pos = [750,50]
                self.text = text
                self.size = [360,85]
            else:
                self.pos = pos
                self.size = size
                self.text = text

    buttonList = []
    for i in range(len(keys)):
        for j, key in enumerate(keys[i]):
            buttonList.append(Button([100 * j + 50, 100 * i + 50], key))
    class Start:

        def __init__(self):
            exitProgram = False
            if exitProgram == False:
                while True:
                    success, img = cap.read()
                    cv2.flip(img,1)
                    img = detector.findHands(img)
                    lmList, bboxInfo = detector.findPosition(img)
                    img = drawAll(img, buttonList)

                    if lmList:
                        for button in buttonList:
                            x, y = button.pos
                            w, h = button.size

                            if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:

                                l, _, _ = detector.findDistance(8, 12, img, draw=False)


                                ## when clicked
                                if l < 28:
                                    if button.text == "Space":
                                        keyboard.tap(Key.space)
                                        cv2.rectangle(img, button.pos, (x + w, y + h), colour_when_clicked, cv2.FILLED)
                                        cv2.putText(img, button.text, (x + 400, y + 65),
                                                cv2.FONT_HERSHEY_PLAIN, 4, text_clicked_colour, 4)
                                    elif button.text == "Tab":
                                        keyboard.tap(Key.tab)
                                        cv2.rectangle(img, button.pos, (x + w, y + h+15), colour_when_clicked, cv2.FILLED)
                                        cv2.putText(img, button.text, (x + 20, y + 75),
                                                cv2.FONT_HERSHEY_PLAIN, 4,text_clicked_colour, 4)
                                    elif button.text == "Backspace":
                                        keyboard.tap(Key.backspace)
                                        cv2.rectangle(img, button.pos, (x + w, y + h), colour_when_clicked, cv2.FILLED)
                                        cv2.putText(img, button.text, (x + 20, y + 75),
                                                cv2.FONT_HERSHEY_PLAIN, 4,text_clicked_colour, 4)
                                    elif button.text == "Exit":
                                        exitProgram = True
                                        raise Exception("Exiting Program")
                                    else:
                                        keyboard.tap(button.text)
                                        cv2.rectangle(img, button.pos, (x + w, y + h+15), colour_when_clicked, cv2.FILLED)
                                        cv2.putText(img, button.text, (x + 20, y + 65),
                                                cv2.FONT_HERSHEY_PLAIN, 4,text_clicked_colour, 4)

                                    sleep(0.20)

                                else:
                                    if button.text == "Space":
                                        cv2.rectangle(img, button.pos, (x + w + 5, y + h + 5), initial_colour, cv2.FILLED)
                                        cv2.putText(img, button.text, (x + 405, y + 70),
                                                cv2.FONT_HERSHEY_PLAIN, 4,text_initial_colour, 4)
                                    else:
                                        cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), initial_colour, cv2.FILLED)
                                        cv2.putText(img, button.text, (x + 25, y + 70),
                                        cv2.FONT_HERSHEY_PLAIN, 4, text_initial_colour, 4)

                    cv2.imshow("Keyboard By Abdulwahab", img)
                    cv2.waitKey(1)
            else:
                os.system("exit")

    Help.show(Help)
except:
    print("Sorry! The Program is Unable to Run The Program.....")