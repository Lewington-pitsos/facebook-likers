import sys
import accounts.procs as procs
import help.database as database
import lep.selenium.setup as setup
import lep.facebook.login as login

user_name = sys.argv[1]
user_password = sys.argv[2]

driver = setup.chrome()
database = database.db()
login.vanilla(driver, user_name, user_password)

procs.idly_click_around(driver, database, 10)
procs.upload_profile_pic(driver, "/home/lewington/Pictures/Dye-Fantasy-08.jpg")
procs.idly_click_around(driver, database, 100)
