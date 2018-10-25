import time
import random
import accounts.actions as actions

def idly_click_around(driver, database):
    for i in range(100):
        for i in range(3):
            actions.navigate_somewhere(driver, database)
            time.sleep(random.randint(2, 12))
        
        actions.like_some_things(driver, database)
        time.sleep(random.randint(0, 9))

