import time
from lep.selenium import utils

def email_name(driver):
    driver.get("https://temp-mail.org/en/")
    email = driver.find_element_by_id("mail").get_attribute("value")
    driver.back()
    return email

def emailed_code(driver):
  driver.get("https://temp-mail.org/en/")
  code_text = driver.find_elements_by_xpath("//a[@class='title-subject']")[0].text
  code = code_text.split(" ")[0]
  driver.back()
  return code