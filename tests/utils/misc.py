"""
Misc utils
"""
from time import sleep

class Misc:
    def __init__(self, driver):
        self.driver = driver

    def save_screenshot(self):
        self.driver.save_screenshot('./screenshot.png')

    def scroll_down(self):
        self.driver.execute_script('window.scrollTo(0, 2000);')
        sleep(2) # temporary solution for infinite scroll check
        self.driver.execute_script('window.scrollTo(0, 4000);')