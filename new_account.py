import time
import sys
import accounts.procs as procs
import help.writer as writer
import lep.selenium.setup as setup
from accounts import create, mail
from details import details

driver = setup.moz()
user_details = details.new()

print(user_details)

fails = 0

while True:
    try:
        email = mail.email_name(driver)

        user_details["mail"] = email
        print(email)

        create.fill_details(driver, user_details)
        time.sleep(9)

        code = mail.emailed_code(driver)
        create.enter_email_code(driver, code)

        break
    except Exception as e:
        print(e)
        print("something went wrong with the account creation process, trying again")
        fails += 1
        if fails > 6:
            print("We have failed {} times, the problem is probably chronic. Exiting scrape".format(fails))
            sys.exit(0)

writer.save_details(user_details)