import time
import random
import accounts.actions as actions



from details import details

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
    time.sleep(random.randint(12, 20))
    print("asdasd")
    actions.click_upload_profile_link(driver)
    actions.upload_and_confirm(driver, picture_path)


def add_random_friend(driver):
    friend_name = details.random_name_string()
    actions.search_for(driver, friend_name)
    actions.click_friend_request_button(driver)
    actions.navigate_home(driver)

def add_some_friends(driver, database, times: int = 5):
    for i in range(times):
        idly_click_around(driver, database, 3)
        add_random_friend(driver)