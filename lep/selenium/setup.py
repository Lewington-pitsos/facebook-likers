from selenium import webdriver

def chrome(images=True):
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-extensions')
    options.add_argument("-incognito")
    options.add_argument("--disable-popup-blocking")
    prefs = {
        'disk-cache-size': 4096,
    }

    if not images:
        prefs["profile.managed_default_content_settings.images"] = True

    options.add_experimental_option("prefs", prefs)

    return webdriver.Chrome(chrome_options=options)

def moz(images=True):
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
    firefox_profile.set_preference("dom.webnotifications.enabled", False)

    if not images:
        firefox_profile.set_preference('permissions.default.image', 2)

    return webdriver.Firefox(firefox_profile=firefox_profile)