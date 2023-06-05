from tkinter import *
import math
def leftClickButton(event):
    bmiCal = float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2)
    textResult.configure(text=bmiCal)

    if bmiCal >= 30:
        showResult.configure(text='อ้วนมาก', fg='red')
    elif bmiCal >= 25:
        showResult.configure(text='อ้วน', fg='orange')
    elif bmiCal >= 23:
        showResult.configure(text='น้ำหนักเกิน', fg='tomato')
    elif bmiCal >= 18.6:
        showResult.configure(text='น้ำหนักปกติ', fg='blue2')
    elif bmiCal <= 18.5:
        showResult.configure(text='ผอมเกินไป', fg='green')

mainWindow = Tk()
textHeight = Label(mainWindow, text='ส่วนสูง(cm.)', width=10, height=2)
textHeight.grid(row=0, column=0)
textBoxHeight = Entry(mainWindow)
textBoxHeight.grid(row=0, column=1)

textWeight = Label(mainWindow, text='น้ำหนัก(Kg.)', width=10, height=2)
textWeight.grid(row=1, column=0)
textBoxWeight = Entry(mainWindow)
textBoxWeight.grid(row=1, column=1)

button = Button(mainWindow, text='คำนวณ', width=10, height=2)
button.grid(row=3, column=0)
button.bind('<Button-1>', leftClickButton)

textResult = Label(mainWindow, text='ผลลัพธ์')
textResult.grid(row=2, column=1)

showResult = Label(mainWindow)
showResult.grid(row=3, column=1)

mainWindow.mainloop()