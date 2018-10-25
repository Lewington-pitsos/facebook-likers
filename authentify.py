import sys
import accounts.procs as procs
import help.database as database
import help.setup as setup

user_name = sys.argv[1]
user_password = sys.argv[2]

driver = setup.chrome()
database = database.db()
setup.login(driver, user_name, user_password)

procs.idly_click_around(driver, database)

