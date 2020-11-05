from tkinter import *
import tkinter
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as soup
import time

chrome_driver_path = 'chromedriver'

chrome_options = Options()
# chrome_options.add_argument('--headless')
# webdriver = webdriver.Chrome(
#   executable_path=chrome_driver_path, options=chrome_options
# )

root = tkinter.Tk()
root.title("CUSTOM WEB CRAWLER")
root.geometry('470x400')
root.configure(bg="#f7f7f7")
p1 = PhotoImage(file='icon.png')
root.iconphoto(False, p1)
root.attributes("-transparentcolor", "red")
# root.attributes("-transparentcolor", "red")
# scrollbar = Scrollbar(root)
# scrollbar.grid( sticky=E)


# frames = []
# widgets = []
var1 = IntVar()
var2_arr = []
var3_arr = []
first_how_entry_arr = []
element_arr = []
class_id_entry_arr = []


def open_app(app_no):
    if app_no == 0:
        os.system('python web-crawler.py')
    elif app_no == 1:
        os.system('python flipkart.py')
    elif app_no == 2:
        os.system('python amazon.py')
    else:
        pass


photo1 = PhotoImage(file="flipkart.png").subsample(10,10)
photo2 = PhotoImage(file="amazon.png").subsample(10,10)
photo3 = PhotoImage(file="instagram.png").subsample(10,10)


C = Canvas(0, bg="blue", height=0, width=0)
bg = PhotoImage(file='bg_image.png')
bg_label = Label(0, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
C.grid()

l1 = Label(bg="#EFAEA0", fg='#000', text='Some Pre-made Crawlers:')
l1.grid(row=1, column=1, sticky=W)
start_insta = Button(text="Instagram Crawler", bg='#FDF5E6', command=lambda: open_app(0), border=3,image = photo3, compound=LEFT)
start_flipkart = Button(text=' Flipkart Crawler', bg='#FDF5E6', border=3,image = photo1, compound=LEFT, command=lambda: open_app(1))
start_flipkart.image = photo1
start_amazon = Button(text=' Amazon Crawler', bg='#FDF5E6', border=3,image = photo2, compound=LEFT, command=lambda: open_app(2))

start_insta.grid(row=2, column=1, pady=12,padx=12)
start_flipkart.grid(row=2, column=2, pady=12,padx=12)
start_amazon.grid(row=2, column=3, pady=12,padx=12)

l2 = Label(bg="#EFAEA0", fg='#000', text='Custom Crawler:',font=("Courier",9))
l2.grid(row=3, column=2, pady=20, padx=15)


frame = LabelFrame(root, bd=1, bg="#FFE4C4", relief=SUNKEN, border=0)
frame.grid(columnspan=4, padx=10, pady=10)


label = Label(frame, bg="#FFE4C4", fg="#000", text="Enter URL Here")

label.grid(row=0)
e=Entry(frame, width =65, borderwidth=2)
e.grid(row=1, padx=20, pady=10)

pos = 0
frame_arr = []


# https://flipkart.com/search?q=shoes
# _2mylT6
# _1vC4OE

# print('Link : ', end='')
# print(e.get())
# print('Saving data as csv: ', end='')
# print(var1.get())
# print('Selected: ', end='')
# for i in range(0, len(frame_arr)):
#     if var2_arr[i].get() == 1:
#         print('FIRST', end='')
#         print(first_how_entry_arr[i].get())
#     elif var2_arr[i].get() == 2:
#         print('all')
#     print(element_arr[i].get())
#     print('with: ', end='')
#     if var3_arr[i].get() == 1:
#         print('class: ', end='')
#     elif var3_arr[i].get() == 2:
#         print('id: ', end='')
#     print(class_id_entry_arr[i].get())

def start():
    # f = open("scraped-data.txt", "w")
    if var1 == 1:
        f = open("scraped-data.txt", "a")
        f.write("\n\n\n <====== NEW PROJECT ======> \n\n\n")
    global webdriver
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    webdriver = webdriver.Chrome(
        executable_path=chrome_driver_path, options=chrome_options
    )

    with webdriver as driver:
        driver.get(e.get())
        time.sleep(2)
        page_soup = soup(driver.page_source, "html.parser")

        for i in range(0, len(frame_arr)):
            if var2_arr[i].get() == 1:
                if var3_arr[i].get() == 1:
                    for j in range(0, int(first_how_entry_arr[i].get())):
                        element = page_soup.find(str(element_arr[i].get()), {"class": str(class_id_entry_arr[i].get())})
                        print(element.text)
                        if var1.get() == 1:
                            f.write(str(element.txt))
                if var3_arr[i].get() == 2:
                    for j in range(0, int(first_how_entry_arr[i].get())):
                        element = page_soup.find(str(element_arr[i].get()), {"id": str(class_id_entry_arr[i].get())})
                        print(element.text)
                        if var1.get() == 1:
                            f.write(str(element.txt))
            if var2_arr[i].get() == 2:
                if var3_arr[i].get() == 1:
                    element = page_soup.findAll(str(element_arr[i].get()), {"class": str(class_id_entry_arr[i].get())})
                if var3_arr[i].get() == 2:
                    element = page_soup.findAll(str(element_arr[i].get()), {"id": str(class_id_entry_arr[i].get())})
                for k in range(0, len(element)):
                    print(element[k].text)
                    if var1.get() == 1:
                        f.write(str(element[k].text))
                if var1.get() == 1:
                    print('<---------- Written All Elements -------->')
            print()
            print("<============= ELEMENT CHANGED =============>")
            print()
            if var1.get() == 1:
                f.write("\n <============= ELEMENT CHANGED =============> \n ")
            # element = WebDriverWait(driver, 50).until(
            #     EC.presence_of_element_located((By.CLASS_NAME, 'L3NKy'))
            # )
    if var1.get() == 1:
        f.close()

def add_new_frame():
    global pos

    var2 = IntVar()
    var3 = IntVar()

    frame_options = LabelFrame(frame, bd=1, bg="#FFE4C4", relief=SUNKEN, border=0)
    frame_options.grid(columnspan=5, padx=6, pady=5)

    label_select = Label(frame_options, bg="#FFE4C4", fg="#000", text="Select: ")
    label_select.grid(row=1, column=1)

    w1 = Radiobutton(frame_options, bg="#FFE4C4", fg="#000", text="First", variable=var2, value=1)
    w2 = Radiobutton(frame_options, bg="#FFE4C4", fg="#000", text="ALL", variable=var2, value=2)

    w1.grid(pady=5,row=1,column=2)
    w2.grid(pady=5,row=2,column=2)

    first_how_entry = Entry(frame_options, width=5, borderwidth=2)
    first_how_entry.grid(row=1, column=3)

    first_how_entry_arr.append(first_how_entry)

    elements = ['a', 'p', 'li', 'ol', 'ul', 'span', 'div', ]
    element = StringVar(frame_options)
    element.set(elements[0])

    element_arr.append(element)

    dropdown = OptionMenu(frame_options, element, *elements)
    dropdown.grid(row=1, column=4, padx=8)

    # spinbox = Spinbox(frame_options, values=elements, width=5)
    # spinbox.grid(row=1, column=4, padx=8)

    label_with = Label(frame_options, bg="#FFE4C4", fg="#000", text="with: ")
    label_with.grid(row=1, column=5, padx=5)

    w3 = Radiobutton(frame_options, bg="#FFE4C4", fg="#000", text="class", variable=var3, value=1)
    w4 = Radiobutton(frame_options, bg="#FFE4C4", fg="#000", text="id", variable=var3, value=2)

    w3.grid(padx=5,row=1,column=6)
    w4.grid(padx=5,row=2,column=6)

    class_id_entry = Entry(frame_options, width=8, borderwidth=2)
    class_id_entry.grid(row=1, column=7, padx=6)

    class_id_entry_arr.append(class_id_entry)

    pos += 1

    frame_arr.append(frame_options)
    var2_arr.append(var2)
    var3_arr.append(var3)


plus_button = Button(text='+', command=add_new_frame)
plus_button.grid(row=3, column=1)

start_button = Button(text='Begin Crawling', bg='green', command=start)
start_button.grid(row=3, column=3)

c1 = Checkbutton(bg="#FFE4C4", fg="#000", text='Save Crawled Data as txt', variable=var1, onvalue=1, offvalue=0)         #add command to this after creating function
c1.grid(row=3, column=2)

add_new_frame()

# frame_last = LabelFrame(frame, bd=1, bg="#FFE4C4", relief=SUNKEN, border=0)
# frame_last.grid(columnspan=1, padx=15, pady=5)
#

#
# start_crawler = Button(frame_last, text='Begin Crawling', bg='#D2EFA0')
# start_crawler.grid(row=2, pady=5)

root.mainloop()
