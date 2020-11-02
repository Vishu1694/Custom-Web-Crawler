from tkinter import *
import tkinter
import os

root = tkinter.Tk()
root.title("CUSTOM WEB CRAWLER")
root.geometry('450x400')
root.configure(bg="#f7f7f7")
p1 = PhotoImage(file='icon.png')
root.iconphoto(False, p1)
root.attributes("-transparentcolor", "red")
# scrollbar = Scrollbar(root)
# scrollbar.grid( sticky=E)


# frames = []
# widgets = []
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

# def createwidgets():
#
#     # frame = Frame(root, borderwidth=2)
#
#     frame = LabelFrame(root,bg="#282828",bd=1,relief=SUNKEN)
#     frames.append(frame)
#
#     frame.grid(columnspan=4,padx=10,pady=10)
#
#
#     widget = Entry(frame,width =50,borderwidth=3)
#
#     widgets.append(widget)
#
#     widget.grid(row=1,padx=20,pady=10,columnspan=3)
#
#     widget1 = Radiobutton(frame, text="First20", variable=var2, value=1)        #add command to this after creating function
#     widgets.append(widget1)
#     widget2 = Radiobutton(frame, text="ALL", variable=var2, value=2)           #add command to this after creating function
#     widgets.append(widget2)
#
#     widget1.grid(pady=5,row=3,column=0)
#     widget2.grid(pady=5,row=4,column=0)
#     widget3 = Radiobutton(frame, text="CLASS", variable=var3, value=1)        #add command to this after creating function
#     widgets.append(widget3)
#     widget4 = Radiobutton(frame, text="   ID ", variable=var3, value=2)           #add command to this after creating function
#     widgets.append(widget4)
#
#     widget3.grid(pady=5,row=3,column=1)
#     widget4.grid(pady=5,row=4,column=1)


def open_insta():
    os.system('python webcrawler.py')


C = Canvas(0, bg="blue", height=0, width=0)
bg = PhotoImage(file='bg_image.png')
bg_label = Label(0, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
C.grid()

l1 = Label(bg="#EFAEA0", fg='#000', text='Some Pre-made Crawlers: ')
l1.grid(row=1, column=1, sticky=W)
start_insta = Button(text="Instagram Crawler", bg='#EFAEA0', command=open_insta, border=3)
start_flipkart = Button(text='Flipkart Crawler', bg='#EFAEA0', border=3)
start_amazon = Button(text='Amazon Crawler', bg='#EFAEA0', border=3)

start_insta.grid(row=2, column=1, pady=12,padx=15)
start_flipkart.grid(row=2, column=2, pady=12,padx=15)
start_amazon.grid(row=2, column=3, pady=12,padx=15)

l2 = Label(bg="#D2EFA0", fg='#000', text='Custom Crawler:')
l2.grid(row=3, column=2, pady=20, padx=15)


frame = LabelFrame(root, bd=1, bg="#D2EFA0", relief=SUNKEN, border=0)
frame.grid(columnspan=4, padx=10, pady=10)


label = Label(frame, bg="#D2EFA0", fg="#000", text="Enter URL Here")

label.grid(row=0)
e=Entry(frame, width =65, borderwidth=2)
e.grid(row=1, padx=20, pady=10)


frame_options = LabelFrame(frame, bd=1, bg="#D2EFA0", relief=SUNKEN, border=0)
frame_options.grid(columnspan=5, padx=6, pady=5)

label_select = Label(frame_options, bg="#D2EFA0", fg="#000", text="Select: ")
label_select.grid(row=1, column=1)

w1 = Radiobutton(frame_options, bg="#D2EFA0", fg="#000", text="First", variable=var2, value=1)
w2 = Radiobutton(frame_options, bg="#D2EFA0", fg="#000", text="ALL", variable=var2, value=2)

w1.grid(pady=5,row=1,column=2)
w2.grid(pady=5,row=2,column=2)

first_how_entry = Entry(frame_options, width=5, borderwidth=2)
first_how_entry.grid(row=1, column=3)

elements = ['a', 'p', 'li', 'ol', 'ul', 'span', 'div', ]
element = StringVar(frame_options)
element.set(elements[0])

dropdown = OptionMenu(frame_options, element, *elements)
dropdown.grid(row=1, column=4, padx=8)

# spinbox = Spinbox(frame_options, values=elements, width=5)
# spinbox.grid(row=1, column=4, padx=8)

label_with = Label(frame_options, bg="#D2EFA0", fg="#000", text="with: ")
label_with.grid(row=1, column=5, padx=5)

w3 = Radiobutton(frame_options, bg="#D2EFA0", fg="#000", text="class", variable=var3, value=1)
w4 = Radiobutton(frame_options, bg="#D2EFA0", fg="#000", text="id", variable=var3, value=2)

w3.grid(padx=5,row=1,column=6)
w4.grid(padx=5,row=2,column=6)

class_id_entry = Entry(frame_options, width=8, borderwidth=2)
class_id_entry.grid(row=1, column=7, padx=6)

frame_last = LabelFrame(frame, bd=1, bg="#D2EFA0", relief=SUNKEN, border=0)
frame_last.grid(columnspan=1, padx=15, pady=5)

c1 = Checkbutton(frame_last, bg="#D2EFA0", fg="#000", text='Save Crawled Data as CSV', variable=var1, onvalue=1, offvalue=0)         #add command to this after creating function
c1.grid(row=1)

start_crawler = Button(frame_last, text='Begin Crawling', bg='#EFE3A0')
start_crawler.grid(row=2, pady=5)

root.mainloop()