import datetime
import os
from pathlib import Path
class Base():
    def __init__(self, browser):
        self.browser = browser

    # Get current URL
    def get_current_url(self):
        get_url = self.browser.current_url
        print("Current URL: " + get_url)

    # Get assert word
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result, "Wrong word"

    # Get screenshot
    def get_screenshot(self, test_name):
        # screen_path = os.path.abspath("screens")
        p = Path(os.path.abspath(__file__)).parents[1]
        screen_path = str(p) + '/screens/'
        now_date = datetime.datetime.now().strftime("_%H-%M-%S.%d.%m.%y.")
        name_screenshot = test_name + now_date + "png"
        self.browser.save_screenshot(screen_path + "/" + name_screenshot)

        # Get assert url
    def assert_url(self, result):
        get_url = self.browser.current_url
        assert get_url == result, "Wrong URL"
