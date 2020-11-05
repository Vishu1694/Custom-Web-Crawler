from tkinter import *
import tkinter
from PIL import ImageTk, Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as soup
import time
import csv

crawler_window = tkinter.Tk()

# CheckVar1 = IntVar()
# C1 = tkinter.Checkbutton(text = "The target account is private", variable = CheckVar1, onvalue = 1, offvalue = 0, height=5, width = 20)
# C1.pack()
p1 = PhotoImage(file='flipkart.png')
crawler_window.iconphoto(False, p1)
crawler_window.title("Flipkart Scraper")
path = "flipkart2.png"
img = ImageTk.PhotoImage(Image.open(path).resize((240,70),Image.ANTIALIAS))
panel = Label(crawler_window, image = img)
panel.grid(pady=2,columnspan=2)


label = Label(text="Product Name:")
label.grid(row=1,column=0,pady=5)
entry1 = Entry(crawler_window)
entry1.grid(row=1,column=1,pady=5)

def begin():
    link = f'https://flipkart.com/search?q={entry1.get()}'
    chrome_driver_path = 'chromedriver'

    global webdriver
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    webdriver = webdriver.Chrome(
        executable_path=chrome_driver_path, options=chrome_options
    )

    with webdriver as driver:
        driver.get(link)
        time.sleep(2)
        page_soup = soup(driver.page_source, "html.parser")
        product_name = page_soup.findAll("a", {"class": "_2mylT6"})
        product_price = page_soup.findAll("div", {"class": "_1vC4OE"})

        fields = ['Product Name', 'Price']
        rows = []
        for i in range(0, len(product_name)):
            temp_list = []
            temp_list.append(product_name[i].text)
            temp_list.append(product_price[i].text)
            rows.append(temp_list)

        with open("flipkart-data.csv", 'w', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            csvwriter.writerows(rows)
        print(rows)

btn = Button(text="Begin Scraping!",bg='#D2EFA0',command=begin)
btn.grid(row=3,columnspan=2,pady=5)




crawler_window.mainloop()
