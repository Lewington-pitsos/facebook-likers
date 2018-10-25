from selenium import webdriver

def chrome():
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-extensions')
    options.add_argument("-incognito")
    options.add_argument("--disable-popup-blocking")
    prefs = {
        'profile.managed_default_content_settings.images':2,
        'disk-cache-size': 4096,
    }
    options.add_experimental_option("prefs", prefs)

    return webdriver.Chrome(chrome_options=options)

def moz():
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference('permissions.default.image', 2)
    firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
    firefox_profile.set_preference("dom.webnotifications.enabled", False)

    return webdriver.Firefox(firefox_profile=firefox_profile)

def login(driver, user_email: str, user_password: str) -> dict:
    driver.get("https://www.facebook.com")
    
    email = driver.find_element_by_id("email")
    password = driver.find_element_by_id("pass")
    submit = driver.find_element_by_id("loginbutton")

    email.send_keys(user_email)
    password.send_keys(user_password)
    submit.click()