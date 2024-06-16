"""
Cookies popups page
"""
from selenium.webdriver.common.by import By

COOKIES_POPUP_CSS = '.consent-banner'
COOKIES_ACCEPT_BUTTON_CSS = f'{COOKIES_POPUP_CSS} button[data-a-target="consent-banner-accept"]'
PRIVACY_POPUP_CSS = f'.tw-modal'
PRIVACY_POPUP_BUTTON_CSS = f'{PRIVACY_POPUP_CSS} button'

class CookiesPopups:
    def get_cookies_popup(driver):
        return driver.find_element(By.CSS_SELECTOR, COOKIES_POPUP_CSS)

    def click_accept_cookies(driver):
        return driver.find_element(By.CSS_SELECTOR, COOKIES_ACCEPT_BUTTON_CSS).click()

    def click_close_privacy_info(driver):
        return driver.find_element(By.CSS_SELECTOR, PRIVACY_POPUP_BUTTON_CSS).click()

    def cookies_consent_workaround(driver):
        popup = CookiesPopups.get_cookies_popup(driver)
        driver.execute_script('arguments[0].setAttribute("style", "display: none;")', popup)

    def close_cookies_consent_if_visible(driver):
        elements = driver.find_elements(By.CSS_SELECTOR, COOKIES_POPUP_CSS)
        if len(elements) > 0:
            CookiesPopups.click_accept_cookies(driver)
            CookiesPopups.cookies_consent_workaround(driver)

    def close_privacy_info_popup_if_visible(driver):
        elements = driver.find_elements(By.CSS_SELECTOR, PRIVACY_POPUP_CSS)
        if len(elements) > 0:
            CookiesPopups.click_close_privacy_info(driver)
