from tkinter import *


root = Tk()
root.title("CUSTOM WEB CRAWLER")
# root.geometry('510x400')
root.configure(bg="#282828")
p1 = PhotoImage(file = 'C:/Users/HP/OneDrive/Documents/webcrawler.png')
root.iconphoto(False, p1) 
# scrollbar = Scrollbar(root)
# scrollbar.grid( sticky=E)


frames = []
widgets = []
var1 = IntVar()
var2 = IntVar()
var3=  IntVar()

def createwidgets():

    # frame = Frame(root, borderwidth=2)

    frame = LabelFrame(root,bg="#282828",bd=1,relief=SUNKEN)
    frames.append(frame)

    frame.grid(columnspan=4,padx=10,pady=10)

    
    widget = Entry(frame,width =50,borderwidth=3)

    widgets.append(widget)

    widget.grid(row=1,padx=20,pady=10,columnspan=3)

    widget1 = Radiobutton(frame, text="First20", variable=var2, value=1)        #add command to this after creating function
    widgets.append(widget1)
    widget2 = Radiobutton(frame, text="ALL", variable=var2, value=2)           #add command to this after creating function
    widgets.append(widget2)
    
    widget1.grid(pady=5,row=3,column=0)
    widget2.grid(pady=5,row=4,column=0)
    widget3 = Radiobutton(frame, text="CLASS", variable=var3, value=1)        #add command to this after creating function
    widgets.append(widget3)
    widget4 = Radiobutton(frame, text="   ID ", variable=var3, value=2)           #add command to this after creating function
    widgets.append(widget4)
    
    widget3.grid(pady=5,row=3,column=1)
    widget4.grid(pady=5,row=4,column=1)



frame = LabelFrame(root,bg="#282828",bd=1,relief=SUNKEN)
frame.grid(columnspan=4,padx=10,pady=10)


label = Label(frame,text="Enter URL Here")

label.grid(row=0,pady=10)
e=Entry(frame,width =73,borderwidth=3)
e.grid(row=1,padx=20,pady=10)

button1 = Button(root,text="Default Search",bg="#FFAE42")
button2 = Button(root,text="Amazon",bg="#FFAE42")
button3 = Button(root,text="Flipkart",bg="#FFAE42")
button4 = Button(root,text="Instagram",bg="#FFAE42")


button1.grid(row=2,column=0,pady=30,padx=5)
button2.grid(row=2,column=1,pady=30,padx=5)
button3.grid(row=2,column=2,pady=30,padx=5)
button4.grid(row=2,column=3,pady=30,padx=5)

c1 = Checkbutton(root, text='Save Crawled Data as CSV',variable=var1, onvalue=1, offvalue=0)         #add command to this after creating function
c1.grid(row=3,padx=20,pady=15)

button5 = Button(root,text="Add",bg="#FFAE42",command=createwidgets,anchor=W)
button5.grid()


frame = LabelFrame(root,bg="#282828",bd=1,relief=SUNKEN)
frame.grid(columnspan=4,padx=10,pady=10)

e=Entry(frame,width =50,borderwidth=3)
e.grid(padx=20,pady=10,columnspan=3)

w1 = Radiobutton(frame, text="First20", variable=var2, value=1)
w2 = Radiobutton(frame, text="ALL", variable=var2, value=2) 
w3 = Radiobutton(frame, text="CLASS", variable=var3, value=1) 
w4 = Radiobutton(frame, text="   ID ", variable=var3, value=2) 


w1.grid(pady=5,row=3,column=0)
w2.grid(pady=5,row=4,column=0)
w3.grid(pady=5,row=3,column=1)
w4.grid(pady=5,row=4,column=1)

# mylabel = Label(root,text="COPYRIGHT ©  Team VKS")
# mylabel.grid(row=10)



root.mainloop()