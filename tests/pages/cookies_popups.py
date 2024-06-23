"""
Cookies popups page
"""
from selenium.webdriver.common.by import By

COOKIES_POPUP_CSS = '.consent-banner'
COOKIES_ACCEPT_BUTTON_CSS = f'{COOKIES_POPUP_CSS} button[data-a-target="consent-banner-accept"]'
PRIVACY_POPUP_CSS = f'.tw-modal'
PRIVACY_POPUP_BUTTON_CSS = f'{PRIVACY_POPUP_CSS} button'

class CookiesPopups:
    def __init__(self, driver):
        self.driver = driver

    def get_cookies_popup(self):
        return self.driver.find_element(By.CSS_SELECTOR, COOKIES_POPUP_CSS)

    def click_accept_cookies(self):
        return self.driver.find_element(By.CSS_SELECTOR, COOKIES_ACCEPT_BUTTON_CSS).click()

    def click_close_privacy_info(self):
        return self.driver.find_element(By.CSS_SELECTOR, PRIVACY_POPUP_BUTTON_CSS).click()

    def cookies_consent_workaround(self):
        popup = self.get_cookies_popup()
        self.driver.execute_script('arguments[0].setAttribute("style", "display: none;")', popup)

    def close_cookies_consent_if_visible(self):
        elements = self.driver.find_elements(By.CSS_SELECTOR, COOKIES_POPUP_CSS)
        if len(elements) > 0:
            self.click_accept_cookies()
            self.cookies_consent_workaround()

    def close_privacy_info_popup_if_visible(self):
        elements = self.driver.find_elements(By.CSS_SELECTOR, PRIVACY_POPUP_CSS)
        if len(elements) > 0:
            self.click_close_privacy_info()
