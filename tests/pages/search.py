"""
Search page
"""
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep


FIRST_SEARCH_SUGGESTION_LINK_CSS = 'main ul li:first-of-type a.tw-link'
SHOW_ALL_CHANNELS_LINK_CSS = 'main section:first-of-type a.tw-link'
ALL_CHANNELS_LIST_CSS = 'main div[role="list"]'
ALL_CHANNELS_LIST_ELEMENT_CSS = 'main div[role="list"] a.tw-link'
SEARCH_INPUT_CSS = 'nav input[data-a-target="tw-input"]'
SEARCH_ICON_CSS = 'nav a[href="/search"]'

class Search:
    def __init__(self, driver):
        self.driver = driver

    def click_search_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, SEARCH_ICON_CSS).click()

    def input_text_into_search_bar(self, search_phrase):
        return self.driver.find_element(By.CSS_SELECTOR, SEARCH_INPUT_CSS).send_keys(search_phrase)

    def click_first_search_suggestion_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, FIRST_SEARCH_SUGGESTION_LINK_CSS).click()

    def click_show_all_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, SHOW_ALL_CHANNELS_LINK_CSS).click()

    def wait_for_channels_list_to_load(self):
        self.driver.find_element(By.CSS_SELECTOR, ALL_CHANNELS_LIST_CSS)

    def choose_channel(self):
        all_elements = self.driver.find_elements(By.CSS_SELECTOR, ALL_CHANNELS_LIST_ELEMENT_CSS)
        ActionChains(self.driver).move_to_element(all_elements[0]).click(all_elements[0]).perform()
        sleep(5) # there is no indicator/class/property that assures the video is played
        self.driver.find_element(By.CSS_SELECTOR, 'main').is_displayed()
