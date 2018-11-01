import time
import random

def like_some_things(driver, db=None):
    like_links = driver.find_elements_by_xpath("//a[contains(@class, 'UFILikeLink')]") + driver.find_elements_by_xpath("//button[contains(@class, 'PageLikeButton')]")

    for link in like_links[:8]:
        try:
            link.click()
            if db is not None:
                db.save_link(link.get_attribute("outerHTML"), link_type="like")
            time.sleep(random.randint(5, 18))

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

def scroll_down(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight + 1000);")
    time.sleep(random.randint(3, 12))
   
def visit_profile(driver):
    try:
        driver.find_element_by_xpath("//img[contains(@id, 'profile_pic_header')]/parent::span/parent::a").click()
    except:
        pass

def click_upload_profile_link(driver):
    # The text of this link is different if it is your first time uploading
    # a file. The text is still the best thing to go off probably because all
    # the other identifiers seem pretty wack.
    links = driver.find_elements_by_xpath("//div[@id='fbProfileCover']//a[text()='Add Photo']")

    if len(links) == 0:
        links = driver.find_elements_by_xpath("//div[@id='fbProfileCover']//a[text()='Upload']")
    
    links[0].click()
    time.sleep(5)


def upload_and_confirm(driver, picture_path: str):
    # Actually uploads the file
    driver.find_element_by_xpath("//input[@title='Choose a file to upload']").send_keys(picture_path)
    time.sleep(30)

    # Confirms the upload
    driver.find_element_by_xpath("//button[text()='Post']").click()
    time.sleep(6)

def search(driver, term: str):
    # slow type to search thingo
    # press eneter
    time.sleep(random.randint(7, 23))