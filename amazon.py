from tkinter import *
import tkinter
from PIL import ImageTk, Image
crawler_window = tkinter.Tk()

# CheckVar1 = IntVar()
# C1 = tkinter.Checkbutton(text = "The target account is private", variable = CheckVar1, onvalue = 1, offvalue = 0, height=5, width = 20)
# C1.pack()
p1 = PhotoImage(file='amazon.png')
crawler_window.iconphoto(False, p1)
crawler_window.title("Amazon Scraper")
path = "amazon2.png"
img = ImageTk.PhotoImage(Image.open(path).resize((240,70),Image.ANTIALIAS))
panel = Label(crawler_window, image = img)
panel.grid(pady=2,columnspan=2)

label = Label(text="Product Name:")
label.grid(row=1,column=0,pady=5)
entry1 = Entry(crawler_window)
entry1.grid(row=1,column=1,pady=5)


btn = Button(text="Begin Scraping!",bg='#D2EFA0')
btn.grid(row=3,columnspan=2,pady=5)


crawler_window.mainloop()
