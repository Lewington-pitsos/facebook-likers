import time
import random
import accounts.actions as actions

def idly_click_around(driver, database, times: int):
    for i in range(times):
        for i in range(2):
            actions.navigate_somewhere(driver, database)
            actions.scroll_down(driver)
            time.sleep(random.randint(20, 50))

            actions.navigate_somewhere(driver, database)
            time.sleep(random.randint(20, 50))
        
        actions.scroll_down(driver)
        actions.like_some_things(driver, database)
        time.sleep(random.randint(9, 30))

def upload_profile_pic(driver, picture_path):
    actions.visit_profile(driver)
    actions.click_upload_profile_link(driver)
    actions.upload_and_confirm(driver, picture_path)



