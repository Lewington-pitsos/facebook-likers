import time
import sys
import accounts.procs as procs
import help.database as database
from lep.selenium import setup, utils
from accounts import create, mail
from details import details

params = sys.argv

if len(params) == 2 and params[1] == 'moz':
    driver = setup.moz()
    browser = "moz"
else:
    driver = setup.chrome()
    browser = "chrome"

db = database.db()
user_details = details.new()
user_details["browser"] = browser

print(user_details)

success, email = utils.attempt(mail.email_name, driver)
user_details["mail"] = email
print(email)

if success:
    success, _ = utils.attempt(create.fill_details, driver, user_details)

if success:
    time.sleep(9)
    db.save_user(user_details)
    profile_pic = details.random_image()
    success, code = mail.emailed_code(driver)

if success:
    success, _ = utils.attempt(create.enter_email_code, driver, code)

if success:
    success, _ = utils.attempt(create.complete_signup, driver, profile_pic)

if success:
    details.mark_as_used(profile_pic)

for _ in range(2):
    if success:
        success, _ = utils.attempt(procs.add_random_friend, driver)