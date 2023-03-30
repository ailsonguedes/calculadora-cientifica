import math
import tkinter as tk
from tkinter import *
from tkinter import filedialog, Widget

field_text = ""

def add_to_field(sth):
    global field_text
    field_text=field_text+str(sth)
    field.delete("1.0","end")
    field.insert("1.0",field_text, 'tag-right')

def calculate():
    global field_text
    result = str(eval(field_text))
    field.delete("1.0", "end")
    field.insert("1.0", result, 'tag-right')

def clear():
    global field_text
    field_text = ""
    field.delete("1.0", "end")

def square_root():
    global field_text
    res = float(field_text)
    resSqrt = math.sqrt(res)
    str(resSqrt)
    field.delete("1.0", "end")
    field.insert("1.0", resSqrt, 'tag-right')
   
def pi():
    global field_text
    resPi = math.pi
    str(resPi)
    field.delete("1.0", "end")
    field.insert("1.0", resPi, 'tag-right')  

def cos():
    global field_text
    res = float(field_text)
    resCos = math.cos(res)
    print(resCos)
    str(resCos)
    field.delete("1.0", "end")
    field.insert("1.0", resCos, 'tag-right')

def log():
    global field_text
    res = float(field_text)
    resLog = math.log10(res)
    field.delete("1.0", "end")
    field.insert("1.0", resLog, 'tag-right')

def tan():
    global field_text
    res = float(field_text)
    resTan = math.tan(res)
    print(resTan)
    field.delete("1.0", "end")
    field.insert("1.0", resTan, 'tag-right')

def sin():
    global field_text
    res = float(field_text)
    resSin = math.sin(res)
    print(resSin)
    field.delete("1.0", "end")
    field.insert("1.0", resSin, 'tag-right')
    
def euler():
    global field_text
    res = float(field_text)
    resEu = math.e * res
    print(resEu)
    field.delete("1.0", "end")
    field.insert("1.0", resEu, 'tag-right') 
    
def factori():
    global field_text
    res = float(field_text)
    resFactori = math.factorial(res)
    field.delete("1.0", "end")
    field.insert("1.0", resFactori, 'tag-right') 
    
color1 = "#BBB09B" #Khaki
color2 = "#D7BBA8" #Desert Sand
color3 = "#EFA8B8" #Cherry Blossom Pink
color4 = "#E26D5A" #Burned Sienna
color5 = "#3E2A35" #Dark Purple

mainScreen = Tk()

mainScreen.title("Calculadora Py")
mainScreen.geometry("650x400")
mainScreen.config(bg=color2)
mainScreen.resizable(width=False, height=False)

field=tk.Text(mainScreen,height=5,width=45,font=("Times New Roman",20), relief='sunken')
field.tag_configure('tag-right', justify='right')
field.place(x=8, y=15)

# primeira fileira dos botoes numericos
button0 = Button(mainScreen, width=8, height=2, text="0", command= lambda: add_to_field(0), relief='raised', bg=color1)
button0.place(x=250, y=320)
buttonPoint = Button(mainScreen, width=8, height=2, text=".", command= lambda: add_to_field("."), relief='raised', bg=color1)
buttonPoint.place(x=320, y=320)
buttonErasy = Button(mainScreen, width=8, height=2, text="⌫", command= lambda: clear(), relief='raised', bg=color1)
buttonErasy.place(x=390, y=320)
# segunda fileira dos botoes numericos
button1 = Button(mainScreen, width=8, height=2, text="1", command= lambda: add_to_field(1), relief='raised', bg=color1)
button1.place(x=250, y=275)
button2 = Button(mainScreen, width=8, height=2, text="2", command= lambda: add_to_field(2), relief='raised', bg=color1)
button2.place(x=320, y=275)
button3 = Button(mainScreen, width=8, height=2, text="3", command= lambda: add_to_field(3), relief='raised', bg=color1)
button3.place(x=390, y=275)
# terceira fileira dos botoes numericos
button4 = Button(mainScreen, width=8, height=2, text="4", command= lambda: add_to_field(4), relief='raised', bg=color1)
button4.place(x=250, y=230)
button5 = Button(mainScreen, width=8, height=2, text="5", command= lambda: add_to_field(5), relief='raised', bg=color1)
button5.place(x=320, y=230)
button6 = Button(mainScreen, width=8, height=2, text="6", command= lambda: add_to_field(6), relief='raised', bg=color1)
button6.place(x=390, y=230)
# quarta fileira dos botoes numericos
button7 = Button(mainScreen, width=8, height=2, text="7", command= lambda: add_to_field(7), relief='raised', bg=color1)
button7.place(x=250, y=185)
button8 = Button(mainScreen, width=8, height=2, text="8", command= lambda: add_to_field(8), relief='raised', bg=color1)
button8.place(x=320, y=185)
button9 = Button(mainScreen, width=8, height=2, text="9", command= lambda: add_to_field(9), relief='raised', bg=color1)
button9.place(x=390, y=185)

# primeira fileira dos botoes simbolicos
buttonSum = Button(mainScreen, width=8, height=2, text="+", command= lambda: add_to_field("+"), relief='raised', bg=color4)
buttonSum.place(x=470, y=320)
buttonEqual = Button(mainScreen, width=8, height=2, text="=", command= lambda: calculate(), relief='raised', bg=color3)
buttonEqual.place(x=540, y=320)
# segunda fileira dos botoes simbolicos
buttonSubtraction = Button(mainScreen, width=8, height=2, text="-", command= lambda: add_to_field("-"), relief='raised', bg=color4)
buttonSubtraction.place(x=470, y=275)
buttonRemainder = Button(mainScreen, width=8, height=2, text="%", command= lambda: add_to_field("%"), relief='raised', bg=color4)
buttonRemainder.place(x=540, y=275)
# terceira fileira dos botoes simbolicos
buttonMultiplication = Button(mainScreen, width=8, height=2, text="x", command= lambda: add_to_field("*"), relief='raised', bg=color4)
buttonMultiplication.place(x=470, y=230)
buttonParentheses = Button(mainScreen, width=3, height=2, text="(", command= lambda: add_to_field("("), relief='raised', bg=color4)
buttonParentheses.place(x=540, y=230)
buttonParentheses = Button(mainScreen, width=3, height=2, text=")", command= lambda: add_to_field(")"), relief='raised', bg=color4)
buttonParentheses.place(x=575, y=230)
# terceira fileira dos botoes simbolicos
buttonDivison = Button(mainScreen, width=8, height=2, text="÷", command= lambda: add_to_field("/"), relief='raised', bg=color4)
buttonDivison.place(x=470, y=185)
buttonC = Button(mainScreen, width=8, height=2, text="C", command= lambda: clear(), relief='raised', bg=color3)
buttonC.place(x=540, y=185)

# primeira fileira dos botoes de expressão
buttonEuler= Button(mainScreen, width=8, height=2, text="e", command= lambda: euler(), relief='raised', fg="white", bg=color5)
buttonEuler.place(x=30, y=320)
buttonIn= Button(mainScreen, width=8, height=2, text="In", relief='raised', fg="white", bg=color5)
buttonIn.place(x=100, y=320)
buttonLogarithm = Button(mainScreen, width=8, height=2, text="log", command= lambda: log(), relief='raised', fg="white", bg=color5)
buttonLogarithm.place(x=170, y=320)
# segunda fileira dos botoes de expressão
buttonSin= Button(mainScreen, width=8, height=2, text="sin", command= lambda: sin(), relief='raised', fg="white", bg=color5)
buttonSin.place(x=30, y=275)
buttonCos= Button(mainScreen, width=8, height=2, text="cos", command= lambda: cos(), relief='raised', fg="white", bg=color5)
buttonCos.place(x=100, y=275)
buttonTan = Button(mainScreen, width=8, height=2, text="tan", command= lambda: tan(), relief='raised', fg="white", bg=color5)
buttonTan.place(x=170, y=275)
# terceira fileira dos botoes de expressão
buttonInv = Button(mainScreen, width=8, height=2, text="INV", relief='raised', fg="white", bg=color5)
buttonInv.place(x=30, y=230)
buttonExponentiation= Button(mainScreen, width=8, height=2, text="^", command= lambda: add_to_field("**"), relief='raised', fg="white", bg=color5)
buttonExponentiation.place(x=100, y=230)
buttonFactorial = Button(mainScreen, width=8, height=2, text="!", command= lambda: factori(), relief='raised', fg="white", bg=color5)
buttonFactorial.place(x=170, y=230)
# quarta fileira dos botoes de expressão
buttonRad = Button(mainScreen, width=8, height=2, text="RAD", relief='raised', fg="white", bg=color5)
buttonRad.place(x=30, y=185)
buttonSquareRoot = Button(mainScreen, width=8, height=2, text="√", command= lambda: square_root(), relief='raised', fg="white", bg=color5)
buttonSquareRoot.place(x=100, y=185)
buttonPi = Button(mainScreen, width=8, height=2, text="π", command= lambda: pi(), relief='raised', fg="white", bg=color5)
buttonPi.place(x=170, y=185)

mainScreen.mainloop()