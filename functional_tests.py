from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest


# here we start to build a user story

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        caps = DesiredCapabilities.FIREFOX
        caps["marionette"] = True
        self.browser = webdriver.Firefox(capabilities=caps)

        # set a easy wait
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Emily heard an cool todo app
        # She checks her web
        self.browser.get('http://localhost:8000')

        # She founds "To-Do" in tile of the website
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She creates one thing that she has todo by the invitation

        # She inputs 'Buy a basketball'

        # While she presses enter, website renews and lists out:
        # 1. Buy a basketball

        # Now there still has an text bar to let her add other todos
        # She inputs 'Call friends to play basketball'

        # Website renews again, now she has 2 todo lists

        # Emily dosen't know if this website can remember her todos
        # She sees this website send an unique URL to her
        # Website give some description for this feature

        # She goes to this URL - Her todos still there.

        # She quits happily

if __name__ == '__main__':
    unittest.main(warnings='ignore')