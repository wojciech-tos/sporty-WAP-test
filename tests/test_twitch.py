"""
Test Twitch
"""
from pages.cookies_popups import CookiesPopups
from pages.search import Search
from utils.misc import Misc
from utils.webdriver import Webdriver

TWITCH_URL='https://www.twitch.tv/'
SEARCH_PHRASE='Starcraft II'

class TestTwitch:
    @staticmethod
    def test_chrome():
        driver = Webdriver.get_webdriver(TWITCH_URL)
        TestTwitch.main_test_twitch(driver)

    def main_test_twitch(driver):
        TestTwitch._close_cookies_and_privacy_popups(driver)
        TestTwitch._search_for_phrase(driver, SEARCH_PHRASE)
        Misc.scroll_down(driver)
        Search.choose_channel(driver)
        Misc.save_screenshot(driver)

    def _search_for_phrase(driver, search_phrase):
        Search.click_search_button(driver)    
        Search.input_text_into_search_bar(driver, search_phrase)
        Search.click_first_search_suggestion_link(driver)
        Search.click_show_all_link(driver)
        Search.wait_for_channels_list_to_load(driver)

    def _close_cookies_and_privacy_popups(driver):
        CookiesPopups.close_cookies_consent_if_visible(driver)
        CookiesPopups.close_privacy_info_popup_if_visible(driver)
