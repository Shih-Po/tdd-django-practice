from selenium import webdriver
# for firefox 47.0
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest

from selenium.webdriver.common.keys import Keys

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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She creates one thing that she has todo by the invitation
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She inputs 'Buy a basketball'
        input_box.send_keys('Buy a basketball')

        # While she presses enter, website renews and lists out:
        # 1. Buy a basketball
        input_box.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy a basketball' for row in rows),
            "new to-do item did not appear in table"
        )

        # Now there still has an text bar to let her add other todos
        # She inputs 'Call friends to play basketball'

        # Website renews again, now she has 2 todo lists

        # Emily dosen't know if this website can remember her todos
        # She sees this website send an unique URL to her
        # Website give some description for this feature

        # She goes to this URL - Her todos still there.

        # She quits happily
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')