"""
Webdriver utils
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class Webdriver:
    def get_chrome_driver():
        mobile_emulation = { "deviceName": "iPhone X" }
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        return driver

    def get_firefox_driver():
        opts = webdriver.FirefoxOptions()
        opts.set_capability("deviceName", "iPhone 11 Pro")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=opts)
        return driver

    def get_webdriver(url, browser='chrome', implicit_wait=3):
        driver = None
        if browser == 'chrome':
            driver = Webdriver.get_chrome_driver()
        elif browser == 'firefox':
            driver = Webdriver.get_firefox_driver()
        driver.implicitly_wait(implicit_wait)
        driver.get(url)
        return driver
