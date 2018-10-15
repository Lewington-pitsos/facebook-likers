import sys
import time
import steps
import save
from selenium import webdriver

page_id = sys.argv[1]
page_name = sys.argv[2]

if page_id is None or page_name is None:
    raise ValueError("No page id or page name provided. Sort yourself out m8.")



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

save.save_likers(driver.page_source, page_name)

print("Hell yeah")

