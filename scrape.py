import sys
import time
import steps
from selenium import webdriver

page_id = 1951319155178263

if page_id is None:
    raise ValueError("No page_id provided.")

user_email = "sallymuntzy@outlook.com"
user_password = "r34hge%V&BF3ghf"

likers_url = "https://www.facebook.com/search/{}/likers".format(page_id)

options = webdriver.ChromeOptions()
options.add_argument('--disable-extensions')
options.add_argument("-incognito")
options.add_argument("--disable-popup-blocking")

driver = webdriver.Chrome(chrome_options=options)
steps.login(driver, user_email, user_password)

driver.get(likers_url)

steps.keep_scrolling(driver)

steps.write_likers_file(driver)

print("Hell yeah")

