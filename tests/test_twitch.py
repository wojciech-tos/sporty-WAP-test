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
    def setup_class(cls):
        cls.driver = Webdriver.get_webdriver(TWITCH_URL)
        cls.cookies = CookiesPopups(cls.driver)
        cls.search = Search(cls.driver)
        cls.misc = Misc(cls.driver)

    def test_chrome(self):
        self.main_test_twitch()

    def main_test_twitch(self):
        self._close_cookies_and_privacy_popups()
        self._search_for_phrase(SEARCH_PHRASE)
        self.misc.scroll_down()
        self.search.choose_channel()
        self.misc.save_screenshot()

    def _search_for_phrase(self, search_phrase):
        self.search.click_search_button()
        self.search.input_text_into_search_bar(search_phrase)
        self.search.click_first_search_suggestion_link()
        self.search.click_show_all_link()
        self.search.wait_for_channels_list_to_load()

    def _close_cookies_and_privacy_popups(self):
        self.cookies.close_cookies_consent_if_visible()
        self.cookies.close_privacy_info_popup_if_visible()
