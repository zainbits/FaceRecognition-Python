from tkinter import *
import pyfiglet
import code

def recognize():
    code.getimage(imagename.get())

window=Tk()
window.title("FaceRecognition-By Zain")
window.geometry('500x500')
window['bg'] = '#FFDE03'
imagename=StringVar()
out = pyfiglet.figlet_format("Face Recognition")
coart = Label(window,text=out)
coart.place(y=50, width=500)
coart.config(bg="#FFDE03", foreground='blue')
e1=Entry(window, textvariable=imagename, width=30)
e1.place(x=150,y=200,height=50)
l1=Label(window,text="Enter Name of Photo with Extention")
l1.place(x=145,y=240)
b1=Button(window, text="Recognize",command=recognize, width=25, height=2,bg='#0336FF',foreground='white')
b1.place(x=150,y=260)
credit=Label(text="Made By: Zain Shaikh",bg="black",foreground="white")
credit.place(x=370,y=470)

window.mainloop()