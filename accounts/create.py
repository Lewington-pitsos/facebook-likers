import time
import random
from selenium import webdriver
from lep.selenium import utils 

def fill_details(driver, details):
    driver.get("https://www.facebook.com")
    
    utils.slow_fill(
        driver.find_element_by_xpath("//input[@name='firstname']"),     
        details["first_name"]
    )

    utils.slow_fill(
        driver.find_element_by_xpath("//input[@name='lastname']"), 
        details["last_name"]
    )

    utils.slow_fill(
        driver.find_element_by_xpath("//input[@name='reg_email__']"), 
        details["mail"]
    )

    utils.slow_fill(
        driver.find_element_by_xpath("//input[@name='reg_passwd__']"), 
        details["password"]
    )

    driver.find_element_by_xpath("//select[@name='birthday_day']//option[contains(text(), '{}')]".format(details["birth_day"])).click()
    time.sleep(0.3)

    driver.find_element_by_xpath("//select[@name='birthday_month']//option[text()='{}']".format(details["birth_month"])).click()
    time.sleep(0.3)

    driver.find_element_by_xpath("//select[@name='birthday_year']//option[text()='{}']".format(details["birth_year"])).click()
    time.sleep(0.3)

    gender_string = "Male" if details["male"] else "Female"  
    driver.find_element_by_xpath("//label[text()='{}']".format(gender_string)).click()

    utils.slow_fill(
        driver.find_element_by_xpath("//input[@name='reg_email_confirmation__']"),
         details["mail"]
    )

    time.sleep(0.2)    
    driver.find_element_by_xpath("//button[@name='websubmit']").click()

def enter_email_code(driver, code):
    utils.slow_fill(
        driver.find_element_by_id("code_in_cliff"),
        code
    )
    time.sleep(0.765)
    
    driver.find_element_by_xpath("//button[@name='confirm']").click()
    time.sleep(0.144)
    driver.find_element_by_xpath("//button[@name='confirm']").click()
    time.sleep(random.randint(6, 12))

    driver.find_element_by_xpath("//a[text()='OK']").click()
    time.sleep(7.3)


def complete_signup(driver, profile_pic_path):
    driver.find_element_by_xpath("//a[text()='Next']").click()
    time.sleep(6.2)

    confirm = driver.find_elements_by_xpath("//a[text()='Skip Step']")
    if len(confirm) > 0:
        confirm[0].click()
        time.sleep(6.6)

    driver.find_element_by_xpath("//input[@title='Choose a file to upload']").send_keys(profile_pic_path)

