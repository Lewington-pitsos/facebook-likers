import time
import random

def like_some_things(driver, db=None):
    like_links = driver.find_elements_by_xpath("//a[contains(@class, 'UFILikeLink')]") + driver.find_elements_by_xpath("//button[contains(@class, 'PageLikeButton')]")

    for link in like_links[:8]:
        try:
            link.click()
            if db is not None:
                db.save_link(link.get_attribute("outerHTML"), link_type="like")
            time.sleep(random.randint(1, 8))

        except:
            if db is not None:
                try:
                    db.save_link(link.get_attribute("outerHTML"), link_type="like", bad=True)
                except:
                    pass

def navigate_home(driver):
    driver.find_elements_by_xpath("//a[text() = 'Home']")[0].click()
    return True

def navigate_to_page_link(driver, db=None):
    links = driver.find_elements_by_xpath("//a[contains(@href, 'profile.php') or contains(@href, 'group.php') or contains(@href, 'user.php')]")

    while len(links) > 0:
        link = links.pop(random.randrange(len(links)))
        try:
            link.click()
            if db is not None:
                db.save_link(link.get_attribute("outerHTML"), link_type="nav")
            return True
        except:
            if db is not None:
                try: 
                    db.save_link(link.get_attribute("outerHTML"), link_type="nav", bad=True)
                except:
                    pass
                    
    
    return False

def navigate_somewhere(driver, db=None):
    if random.randint(0, 4) == 0:
        return navigate_home(driver)
    
    return navigate_to_page_link(driver, db)

   






