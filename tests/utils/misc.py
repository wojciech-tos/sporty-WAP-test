"""
Misc utils
"""
import os
from time import sleep

class Misc:
    def save_screenshot(driver):
        driver.save_screenshot('./screenshot.png')

    def scroll_down(driver):
        driver.execute_script('window.scrollTo(0, 2000);')
        sleep(2) # temporary solution for infinite scroll check
        driver.execute_script('window.scrollTo(0, 4000);')