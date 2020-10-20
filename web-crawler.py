from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as soup
import time
import wget
from getpass import getpass
import os
from tkinter import *
import tkinter

chrome_driver_path = '/Users/Vishal/Desktop/Custom-Web-Crawler/chromedriver'

chrome_options = Options()
# chrome_options.add_argument('--headless')
webdriver = webdriver.Chrome(
  executable_path=chrome_driver_path, options=chrome_options
)


def begin_crawling(username, password, toCrawl):
    # username = input("Enter Your Instagram username: ")
    # try:
    #     password = getpass(prompt="Enter your Instagram Password: ")
    # except Exception as error:
    #     print('ERROR: ', error)
    #     os.exit(1)
    # toCrawl = input("Enter Target Username: ")
    url = f'https://www.instagram.com/{toCrawl}/'
    login_url = 'https://www.instagram.com/accounts/login/'

    # chrome_driver_path = '/Users/Vishal/Desktop/Custom-Web-Crawler/chromedriver'
    #
    # chrome_options = Options()
    # # chrome_options.add_argument('--headless')
    # webdriver = webdriver.Chrome(
    #   executable_path=chrome_driver_path, options=chrome_options
    # )



    with webdriver as driver:
        driver.get(login_url)

        element = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'L3NKy'))
        )

        # print('Submit button found')
        # page_soup = soup(driver.page_source, "html.parser")
        username_container = driver.find_element_by_name('username')
        password_container = driver.find_element_by_name("password")
        # username_container = page_soup.find("input", {"name": "username" })
        # password_container = page_soup.find("input", {"name": "password"})
        username_container.send_keys(username)
        password_container.send_keys(password)
        time.sleep(2)
        try:
            driver.find_element_by_class_name('L3NKy').click()
        except Exception:
            print('Problem clicking button')
            os._exit(-1)
        element = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'ABCxa'))
        )

        driver.get(url)

        element = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'ySN3v'))
        )

        page_soup = soup(driver.page_source, "html.parser")

        total_posts = int(page_soup.find("span", {"class": "g47SY"}).text)

        # image_containers = page_soup.findAll("div", {"class": "KL4Bh"})

        # while len(image_containers) != int(total_posts):
        #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #     image_containers = page_soup.findAll("div", {"class": "KL4Bh"})
        #     print('Still Scrolling...')

        path = f'C:\\{toCrawl}\\'
        try:
            os.mkdir(path)
        except OSError:
            pass
        os.chdir(path)

        image_list = []

        no_of_scrolls = 1
        if total_posts > 24:
            no_of_scrolls = int((total_posts - 24)/12)
            if (total_posts - 24) % 12 != 0:
                no_of_scrolls += 1

        for _ in range(no_of_scrolls):
            image_containers = page_soup.findAll("div", {"class": "KL4Bh"})
            for image_container in image_containers:
                image = image_container.find("img", {"class": "FFVAD"})
                # file_name = image['alt']+'.jpg'
                image_url = image['src']
                if image_url not in image_list:
                    image_list.append(image_url)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(8)

        for images in image_list:
            wget.download(images)

        # for image_container in image_containers:
        #     image = image_container.find("img", {"class": "FFVAD"})
        #     # file_name = image['alt']+'.jpg'
        #     image_url = image['src']
        #
        #     # Use wget download method to download specified image url.
        #     image_filename = wget.download(image_url)
        #
        #     print('Image Successfully Downloaded: ', image_filename)

crawler_window = tkinter.Tk()

# CheckVar1 = IntVar()
# C1 = tkinter.Checkbutton(text = "The target account is private", variable = CheckVar1, onvalue = 1, offvalue = 0, height=5, width = 20)
# C1.pack()

l1 = Label(text = "Username:")
l2 = Label(text = "Password:")
l3 = Label(text="Target Username: ")

l1.grid(row=0, column=0, sticky=W, pady=2)
l2.grid(row=1, column=0, sticky=W, pady=2)
l3.grid(row=3, column=0, sticky=W, pady=2)

e1 = Entry()
e2 = Entry()
e3 = Entry()

# this will arrange entry widgets
e1.grid(row=0, column=1, pady=2)
e2.grid(row=1, column=1, pady=2)
e3.grid(row=3, column=1, pady=2)

username = str(e1.get())
password = str(e2.get())
target = str(e3.get())


B = tkinter.Button(text="Start Downloading", command=lambda: begin_crawling(str(username), str(password), str(target)))

B.grid(row=5, column=0, sticky=W, pady=2)

crawler_window.mainloop()