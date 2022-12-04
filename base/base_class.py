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
